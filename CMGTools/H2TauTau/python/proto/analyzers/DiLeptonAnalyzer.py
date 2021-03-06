import operator

from itertools import product
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Lepton
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaR2

from CMGTools.H2TauTau.proto.physicsobjects.DiObject import DiObject, DirectDiTau


class DiLeptonAnalyzer(Analyzer):

    """Generic analyzer for Di-Leptons.

    Originally in RootTools, then under heppy examples,
    copied from there to not rely on an example.

    Example configuration, and list of parameters:
    #O means optional

    ana = cfg.Analyzer(
        DiLeptonAnalyzer,
        'DiLeptonAnalyzer',
        pt1=20, # pt, eta, iso cuts for leg 1
        eta1=2.3,
        iso1=None,
        pt2=20, # same for leg 2
        eta2=2.1,
        iso2=0.1,
        m_min=10, # mass range
        m_max=99999,
        from_single_objects=True, #O (default is False)
        dR_min=0.5, #O min delta R between the two legs
        allTriggerObjMatched=False,
        ignoreTriggerMatch=True, #O (default is False)
        verbose=False #from base Analyzer class
        )
    """

    # The DiObject class will be used as the di-object class
    # and the Lepton class as the lepton class
    # Child classes override this choice, and can e.g. decide to use
    # the TauMuon class as a di-object class
    DiObjectClass = DiObject
    LeptonClass = Lepton
    OtherLeptonClass = Lepton

    def beginLoop(self, setup):
        super(DiLeptonAnalyzer, self).beginLoop(setup)
        self.counters.addCounter('DiLepton')
        count = self.counters.counter('DiLepton')
        count.register('all events')
        count.register('> 0 di-lepton')
        count.register('third lepton veto')
        count.register('other lepton veto')
        if hasattr(self.cfg_ana, 'dR_min'):
            count.register('dR > {min:3.1f}'.format(min=self.cfg_ana.dR_min))
        count.register('leg1 offline cuts passed')
        count.register('leg2 offline cuts passed')
        count.register('trig matched')
        
        count.register('{min:3.1f} < m < {max:3.1f}'.format(min=self.cfg_ana.m_min,
                                                            max=self.cfg_ana.m_max))
        count.register('exactly 1 di-lepton')
        count.register('lepton accept')
        count.register('cross kinematics')

    def buildDiLeptons(self, cmgDiLeptons, event):
        '''Creates python DiLeptons from the di-leptons read from the disk.
        to be overloaded if needed.'''
        return map(self.__class__.DiObjectClass, cmgDiLeptons)

    def buildDiLeptonsSingle(self, leptons, event):
        di_objects = []
        for leg1 in leptons:
            for leg2 in leptons:
                if leg1 != leg2:
                    di_objects.append(DirectDiTau(leg1, leg2, self.handles['met'].product()[0]))
        return di_objects

    def buildLeptons(self, cmgLeptons, event):
        '''Creates python Leptons from the leptons read from the disk.
        to be overloaded if needed.'''
        return map(self.__class__.LeptonClass, cmgLeptons)

    def buildOtherLeptons(self, cmgLeptons, event):
        '''Creates python Leptons from the leptons read from the disk.
        to be overloaded if needed.'''
        return map(self.__class__.LeptonClass, cmgLeptons)

    def process(self, event, fillCounter=False):
        self.readCollections(event.input)

        if hasattr(self.cfg_ana, 'from_single_objects') and self.cfg_ana.from_single_objects:
            event.diLeptons = self.buildDiLeptonsSingle(self.handles['leptons'].product(), event)
        else:
            event.diLeptons = self.buildDiLeptons(
                self.handles['diLeptons'].product(), event)
        event.leptons = self.buildLeptons(
            self.handles['leptons'].product(), event)
        event.otherLeptons = self.buildOtherLeptons(
            self.handles['otherLeptons'].product(), event)
        return self.selectionSequence(event, fillCounter=fillCounter,
                                      leg1IsoCut=self.cfg_ana.iso1,
                                      leg2IsoCut=self.cfg_ana.iso2)

    def selectionSequence(self, event, fillCounter, leg1IsoCut=None, leg2IsoCut=None):

        if fillCounter:
            self.counters.counter('DiLepton').inc('all events')

        if len(event.diLeptons) == 0:
            return False

        if fillCounter:
            self.counters.counter('DiLepton').inc('> 0 di-lepton')

        # testing di-lepton itself
        selDiLeptons = event.diLeptons

        event.thirdLeptonVeto = False
        if self.thirdLeptonVeto(event.leptons, event.otherLeptons):
            if fillCounter:
                self.counters.counter('DiLepton').inc('third lepton veto')
            event.thirdLeptonVeto = True

        event.otherLeptonVeto = False
        if self.otherLeptonVeto(event.leptons, event.otherLeptons):
            if fillCounter:
                self.counters.counter('DiLepton').inc('other lepton veto')
            event.otherLeptonVeto = True

        # delta R cut
        if hasattr(self.cfg_ana, 'dR_min'):
            selDiLeptons = [diL for diL in selDiLeptons if
                            self.testDeltaR(diL)]
            if len(selDiLeptons) == 0:
                return False
            else:
                if fillCounter:
                    self.counters.counter('DiLepton').inc(
                        'dR > {min:3.1f}'.format(min=self.cfg_ana.dR_min)
                    )

        # testing leg1
        selDiLeptons = [diL for diL in selDiLeptons if
                        self.testLeg1(diL.leg1(), leg1IsoCut)]

        if len(selDiLeptons) == 0:
            return False
        elif fillCounter:
            self.counters.counter('DiLepton').inc('leg1 offline cuts passed')

        # testing leg2
        selDiLeptons = [diL for diL in selDiLeptons if
                        self.testLeg2(diL.leg2(), leg2IsoCut)]
        if len(selDiLeptons) == 0:
            return False
        else:
            if fillCounter:
                self.counters.counter('DiLepton').inc(
                    'leg2 offline cuts passed')

        # Trigger matching; both legs
        if len(self.cfg_comp.triggers) > 0:
            requireAllMatched = hasattr(self.cfg_ana, 'allTriggerObjMatched') \
                and self.cfg_ana.allTriggerObjMatched

            
            trigMatchDiLeptons = [diL for diL in selDiLeptons if
                            self.trigMatched(event, diL, requireAllMatched)]

            if not getattr(self.cfg_ana, 'ignoreTriggerMatch', False):
                selDiLeptons = trigMatchDiLeptons
                if len(selDiLeptons) == 0:
                    return False
                elif fillCounter:
                    self.counters.counter('DiLepton').inc('trig matched')



        # mass cut
        selDiLeptons = [diL for diL in selDiLeptons if
                        self.testMass(diL)]
        if len(selDiLeptons) == 0:
            return False
        elif fillCounter:
                self.counters.counter('DiLepton').inc(
                    '{min:3.1f} < m < {max:3.1f}'.format(min=self.cfg_ana.m_min,
                                                         max=self.cfg_ana.m_max)
                )

        selDiLeptons = [diL for diL in selDiLeptons if 
                        self.crossKinematicSelection(diL, event)]

        if len(selDiLeptons) == 0:
            return False
        elif fillCounter:
            self.counters.counter('DiLepton').inc('cross kinematics')

        # exactly one?
        if len(selDiLeptons) == 0:
            return False
        elif len(selDiLeptons) == 1 and fillCounter:
            self.counters.counter('DiLepton').inc('exactly 1 di-lepton')

        event.selDiLeptons = selDiLeptons

        event.diLepton = self.bestDiLepton(selDiLeptons)
        event.leg1 = event.diLepton.leg1()
        event.leg2 = event.diLepton.leg2()
        event.selectedLeptons = [event.leg1, event.leg2]

        event.leptonAccept = False
        if self.leptonAccept(event.leptons, event):
            if fillCounter:
                self.counters.counter('DiLepton').inc('lepton accept')
            event.leptonAccept = True

        return True

    def declareHandles(self):
        super(DiLeptonAnalyzer, self).declareHandles()
        if hasattr(self.cfg_ana, 'triggerObjectsHandle'):
            myhandle = self.cfg_ana.triggerObjectsHandle
            self.handles['triggerObjects'] = AutoHandle(
                (myhandle[0], myhandle[1], myhandle[2]),
                'std::vector<pat::TriggerObjectStandAlone>'
                )
        else:    
            self.handles['triggerObjects'] =  AutoHandle(
                'selectedPatTrigger',
                'std::vector<pat::TriggerObjectStandAlone>'
                )


    def leptonAccept(self, *args, **kwargs):
        '''Should implement a default version running on event.leptons.'''
        return True

    def thirdLeptonVeto(self, leptons, otherLeptons, isoCut=0.3):
        '''Should implement a default version running on event.leptons.'''
        return True

    def otherLeptonVeto(self, leptons, otherLeptons, isoCut=0.3):
        '''Should implement a default version running on event.leptons.'''
        return True

    def crossKinematicSelection(self, diL, event):
        '''Final cross-kinematic selection that can act on whole event'''
        return True

    def testLeg1(self, leg, isocut=None):
        '''returns testLeg1ID && testLeg1Iso && testLegKine for leg1'''
        return self.testLeg1ID(leg) and \
            self.testLeg1Iso(leg, isocut) and \
            self.testLegKine(leg, self.cfg_ana.pt1, self.cfg_ana.eta1)

    def testLeg2(self, leg, isocut=None):
        '''returns testLeg2ID && testLeg2Iso && testLegKine for leg2'''
        return self.testLeg2ID(leg) and \
            self.testLeg2Iso(leg, isocut) and \
            self.testLegKine(leg, self.cfg_ana.pt2, self.cfg_ana.eta2)

    def testLegKine(self, leg, ptcut, etacut):
        '''Tests pt and eta.'''
        return leg.pt() > ptcut and \
            abs(leg.eta()) < etacut

    def testLeg1ID(self, leg):
        '''Always return true by default, overload in your subclass'''
        return True

    def testLeg1Iso(self, leg, isocut):
        '''If isocut is None, the iso value is taken from the iso1 parameter.
        Checks the standard dbeta corrected isolation.
        '''
        if isocut is None:
            isocut = self.cfg_ana.iso1
        return leg.relIso(0.5) < isocut

    def testLeg2ID(self, leg):
        '''Always return true by default, overload in your subclass'''
        return True

    def testLeg2Iso(self, leg, isocut):
        '''If isocut is None, the iso value is taken from the iso2 parameter.
        Checks the standard dbeta corrected isolation.
        '''
        if isocut is None:
            isocut = self.cfg_ana.iso2
        return leg.relIso(0.5) < isocut

    def testMass(self, diLepton):
        '''returns True if the mass of the dilepton is between the m_min and m_max parameters'''
        mass = diLepton.mass()
        return self.cfg_ana.m_min < mass and mass < self.cfg_ana.m_max

    def testDeltaR(self, diLepton):
        '''returns True if the two diLepton.leg1() and .leg2() have a delta R larger than the dR_min parameter.'''
        dR = deltaR(diLepton.leg1().eta(), diLepton.leg1().phi(),
                    diLepton.leg2().eta(), diLepton.leg2().phi())
        return dR > self.cfg_ana.dR_min

    def bestDiLepton(self, diLeptons):
        '''Returns the best diLepton (the one with highest pt1 + pt2).'''
        return max(diLeptons, key=operator.methodcaller('sumPt'))

    def trigMatched(self, event, diL, requireAllMatched=False, ptMin=None,  etaMax=None, relaxIds=[11, 15], onlyLeg1=False, checkBothLegs=False):
        '''Check that at least one trigger object per pgdId from a given trigger 
        has a matched leg with the same pdg ID. If requireAllMatched is True, 
        requires that each single trigger object name given in the sample
        cfg has a match.'''
        matched = False
        legs = [diL.leg1(), diL.leg2()]
        diL.matchedPaths = set()

        sameFlavour = (abs(legs[0].pdgId()) == abs(legs[1].pdgId()))

        if onlyLeg1:
            legs = legs[:1]

        if hasattr(self.cfg_ana, 'filtersToMatch'):
            filtersToMatch = self.cfg_ana.filtersToMatch[0]
            leg = legs[self.cfg_ana.filtersToMatch[1] - 1]
            triggerObjects = self.handles['triggerObjects'].product()

            for item in product(triggerObjects, filtersToMatch):
                to     = item[0]
                filter = item[1]
                print to.filterLabels()[-1], to.filterLabels()[-1] != filter
                if to.filterLabels()[-1] != filter:
                    continue
#                 import pdb ; pdb.set_trace()
                if self.trigObjMatched(to, [leg]):
                    setattr(leg, filter, to)
                    
        if not self.cfg_comp.triggerobjects:
            if self.cfg_ana.verbose:
                print 'No trigger objects configured; auto-passing trigger matching'
            return True

        for info in event.trigger_infos:
            
            if not info.fired:
                continue

            matchedIds = []
            matchedLegs = []
            
            for to, to_names in zip(info.objects, info.object_names):
                if ptMin and to.pt() < ptMin:
                    continue
                if etaMax and abs(to.eta()) > etaMax:
                    continue
                toMatched, objMatchedLegs = self.trigObjMatched(to, legs, names=to_names, relaxIds=relaxIds)
                if requireAllMatched:
                    objMatchedLegs = [mleg for mleg in objMatchedLegs if set(self.cfg_comp.triggerobjects) == mleg.triggernames]

                else:
                    matchedLegs += objMatchedLegs
                if toMatched:
                    matchedIds.append(abs(to.pdgId()))

            


            if set(matchedIds) == info.objIds and \
               len(matchedIds) >= len(legs) * sameFlavour:
                if checkBothLegs:
                    if all(l in matchedLegs for l in legs):
                        matched = True
                        diL.matchedPaths.add(info.name)
                    else:
                        matched = False
                else:
                    matched = True
                    diL.matchedPaths.add(info.name)
        
        return matched

    def trigObjMatched(self, to, legs, names=None, dR2Max=0.25, relaxIds=[11, 15]):  # dR2Max=0.089999
        '''Returns true if the trigger object is matched to one of the given
        legs'''
        eta = to.eta()
        phi = to.phi()
        pdgId = abs(to.pdgId())
        to.matched = False
        matchedLegs = []
        for leg in legs:
            # JAN - Single-ele trigger filter has pdg ID 0, to be understood
            # RIC - same seems to happen with di-tau
            # JAN - If it's two triggers, there's a logical flaw in the e-tau
            # channel, so maybe we'll have to move to explicit but not very
            # general requirements (for now added option to relax explicitly)
            if pdgId == abs(leg.pdgId()) or \
               (pdgId == 0 and abs(leg.pdgId()) in relaxIds):
                if deltaR2(eta, phi, leg.eta(), leg.phi()) < dR2Max:
                    to.matched = True
                    matchedLegs.append(leg)
                    if hasattr(leg, 'triggerobjects'):
                        if to not in leg.triggerobjects:
                            leg.triggerobjects.append(to)
                    else:
                        leg.triggerobjects = [to]

                    if names:
                        if hasattr(leg, 'triggernames'):
                            leg.triggernames.update(names)
                        else:
                            leg.triggernames = set(names)

        return to.matched, matchedLegs
