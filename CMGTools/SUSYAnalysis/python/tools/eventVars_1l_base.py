import ROOT
import time
import itertools
import PhysicsTools.Heppy.loadlibs
import array
import operator

from CMGTools.TTHAnalysis.treeReAnalyzer import *
from ROOT import TLorentzVector, TVector2, std

from math import sqrt, pi

#################
### Cuts and WP
#################

## Eta requirement
centralEta = 2.4
eleEta = 2.4

###########
# Jets
###########

corrJEC = "central" # can be "central","up","down"
JECAllowedValues = ["central","up","down"]
assert any(val==corrJEC for val in JECAllowedValues)

smearJER = "None"# can be "None","central","up","down"
JERAllowedValues = ["None","central","up","down"]
assert any(val==smearJER for val in JERAllowedValues)

print
print 30*'#'
print 'Going to use', corrJEC , 'JEC and', smearJER, 'JER!'
print 30*'#'

def getRecalcMET(metp4, event, corrJEC = "central", smearJER = "None"):
    ## newMETp4 = oldMETp4 - (Sum(oldJetsP4) - Sum(newJetsP4))

    # jet pT threshold for MET
    minJpt = 15

    # don't do anything for data
    if event.isData: return metp4

    # check jets for MET exist in tree, else use normal jets collection (Jet)
    jetName = "JetForMET"
    if not hasattr(event,"n"+jetName): jetName = "Jet"

    # get original jets used for MET:
    oldjets = [j for j in Collection(event,jetName,"n"+jetName)]
    # new jets will be old ones for now
    newjets = [j for j in Collection(event,jetName,"n"+jetName)]

    # filter jets
    oldjets = [j for j in oldjets if j.pt > minJpt]

    # vectorial summ of jets for MET
    deltaJetP4 = ROOT.TLorentzVector(0,0,0,0)
    for jet in oldjets: deltaJetP4 += jet.p4()

    if corrJEC == "central":
        #pass # don't do anything
        for jet in newjets: jet.pt = jet.rawPt * jet.corr
    elif corrJEC == "up":
        for jet in newjets: jet.pt = jet.rawPt * jet.corr_JECUp
    elif corrJEC == "down":
        for jet in newjets: jet.pt = jet.rawPt * jet.corr_JECDown
    if smearJER!= "None":
        for jet in newjets: jet.pt = returnJERSmearedPt(jet.pt,abs(jet.eta),jet.mcPt,smearJER)

    # filter jets
    newjets = [j for j in newjets if j.pt > minJpt]

    for jet in newjets: deltaJetP4 -= jet.p4()

    #print "MET diff = ", deltaJetP4.Pt()
    return (metp4 - deltaJetP4)

def returnJERSmearFactor(aeta, shiftJER):
    # from https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution
    #13 TeV tables

    factor = 1.061 + shiftJER*0.023
    if   aeta > 3.2: factor = 1.320 + shiftJER * 0.286
    elif aeta > 3.0: factor = 1.303 + shiftJER * 0.111
    elif aeta > 2.5: factor = 1.343 + shiftJER * 0.123
    elif aeta > 1.9: factor = 1.126 + shiftJER * 0.094
    elif aeta > 1.3: factor = 1.106 + shiftJER * 0.030
    elif aeta > 0.8: factor = 1.088 + shiftJER * 0.029

    return factor

def returnJERSmearedPt(jetpt,aeta,genpt,smearJER):
    if genpt==0: return jetpt
#    assert (any(val==smearJER for val in JERAllowedValues) and smearJER!="None")
    shiftJER=0
    if   smearJER=="up"  : shiftJER = +1
    elif smearJER=="down": shiftJER = -1
    ptscale = max(0.0, (jetpt + (returnJERSmearFactor(aeta, shiftJER)-1)*(jetpt-genpt))/jetpt)
    return jetpt*ptscale

## B tag Working points
## CSV (v1 -- Run1) WPs
#btag_LooseWP = 0.244
#btag_TightWP = 0.679

## CMVA (PHYS14)
#btag_LooseWP = 0.244
#btag_TightWP = 0.762

## CSV v2 (CSV-IVF) ( PHYS14)
#btag_LooseWP = 0.423
#btag_MediumWP = 0.814
#btag_TightWP = 0.941

## CSV v2 (CSV-IVF) (Spring16)
#btag_LooseWP = 0.460
#btag_MediumWP = 0.800
#btag_TightWP = 0.935

# CSV v2 (CSV-IVF) (after remeasurement by BTV POG)
btag_LooseWP = 0.5426
btag_MediumWP = 0.8484
btag_TightWP = 0.9535

# DeepCSV (new Deep Flavour tagger)
btag_DeepLooseWP = 0.2219
btag_DeepMediumWP = 0.6324
btag_DeepTightWP = 0.8958

###########
# MUONS
###########

muID = 'medium' # 'medium'(2015) or 'ICHEPmediumMuonId' (2016)



###########
# Electrons
###########

eleID = 'CB' # 'MVA' or 'CB'

print
print 30*'#'
print 'Going to use', eleID, 'electron ID!'
print 30*'#'
print

## PHYS14 IDs
## Non-triggering electron MVA id (Phys14 WP)
# Tight MVA WP
Ele_mvaPhys14_eta0p8_T = 0.73;
Ele_mvaPhys14_eta1p4_T = 0.57;
Ele_mvaPhys14_eta2p4_T = 0.05;
# Medium MVA WP  <--- UPDATE
Ele_mvaPhys14_eta0p8_M = 0.35;
Ele_mvaPhys14_eta1p4_M = 0.20;
Ele_mvaPhys14_eta2p4_M = -0.52;
# Loose MVA WP
Ele_mvaPhys14_eta0p8_L = 0.35;
Ele_mvaPhys14_eta1p4_L = 0.20;
Ele_mvaPhys14_eta2p4_L = -0.52;

## SPRING15 IDs
## Non-triggering electron MVA id (Spring15 WP):
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSLeptonSF#Electrons
# Tight MVA WP
Ele_mvaSpring15_eta0p8_T = 0.87;
Ele_mvaSpring15_eta1p4_T = 0.6;
Ele_mvaSpring15_eta2p4_T = 0.17;
# Medium MVA WP  <--- UPDATE
Ele_mvaSpring15_eta0p8_M = 0.35;
Ele_mvaSpring15_eta1p4_M = 0.20;
Ele_mvaSpring15_eta2p4_M = -0.52;
# Loose MVA WP
Ele_mvaSpring15_eta0p8_L = -0.16;
Ele_mvaSpring15_eta1p4_L = -0.65;
Ele_mvaSpring15_eta2p4_L = -0.74;
# VLoose MVA WP
Ele_mvaSpring15_eta0p8_VL = -0.11;
Ele_mvaSpring15_eta1p4_VL = -0.55;
Ele_mvaSpring15_eta2p4_VL = -0.74;

## Ele MVA check
def checkEleMVA(lep,WP = 'Tight', era = "Spring15" ):
    # Eta dependent MVA ID check:
    passID = False

    lepEta = abs(lep.eta)

    # eta cut
    if lepEta > eleEta:
        print "here"
        return False

    if era == "Spring15":
        lepMVA = lep.mvaIdSpring15

        if WP == 'Tight':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaSpring15_eta0p8_T
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaSpring15_eta1p4_T
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaSpring15_eta2p4_T
        elif WP == 'Medium':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaSpring15_eta0p8_M
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaSpring15_eta1p4_M
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaSpring15_eta2p4_M
        elif WP == 'Loose':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaSpring15_eta0p8_L
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaSpring15_eta1p4_L
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaSpring15_eta2p4_L
        elif WP == 'VLoose':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaSpring15_eta0p8_VL
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaSpring15_eta1p4_VL
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaSpring15_eta2p4_VL

    elif era == "Phys14":
        lepMVA = lep.mvaIdPhys14

        if WP == 'Tight':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaPhys14_eta0p8_T
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaPhys14_eta1p4_T
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaPhys14_eta2p4_T
        elif WP == 'Medium':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaPhys14_eta0p8_M
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaPhys14_eta1p4_M
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaPhys14_eta2p4_M
        elif WP == 'Loose':
            if lepEta < 0.8: passID = lepMVA > Ele_mvaPhys14_eta0p8_L
            elif lepEta < 1.44: passID = lepMVA > Ele_mvaPhys14_eta1p4_L
            elif lepEta >= 1.57: passID = lepMVA > Ele_mvaPhys14_eta2p4_L

    return passID

## Isolation
ele_miniIsoCut = 0.1
muo_miniIsoCut = 0.2
Lep_miniIsoCut = 0.4
trig_miniIsoCut = 0.8

## Lepton cuts (for MVAID)
goodEl_lostHits = 0
goodEl_sip3d = 4
goodMu_sip3d = 4

class EventVars1L_base:
    def __init__(self):

        self.branches = [
            ## general event info
            'Run','Lumi','Xsec',("Event","l"),'genWeight','isData',
            ## leptons
            'nLep', 'nVeto',
            'nEl','nMu',
            ## selected == tight leps
            #'nTightLeps',
            'nTightEl','nTightMu',
            # for indx
            ("nTightLeps","I"),("tightLepsIdx","I",10,"nTightLeps"),
            #("tightLeps_DescFlag","I",10,"nTightLeps"),
            'Lep_pdgId','Lep_pt','Lep_eta','Lep_phi','Lep_Idx','Lep_relIso','Lep_miniIso','Lep_hOverE',
            'Selected', # selected (tight) or anti-selected lepton
            # second leading lepton
            'Lep2_pt', 'Selected2',
            ## MET
            'MET','LT','ST',
            'MT',
            "MT_misET",
            "DeltaPhiLepW", 'dPhi','Lp',
            "GendPhi","GenLT","GenMET",
            # no HF stuff
#            'METNoHF', 'LTNoHF', 'dPhiNoHF',
            ## jets
            'HT','nJets','nBJet', 'nBJetDeep',
            ("nJets30","I"),("Jets30Idx","I",50,"nJets30"),'nBJets30','nJets30Clean',
            'nJets40','nBJets40',
            "htJet30j", "htJet30ja","htJet40j",
            'Jet1_pt','Jet2_pt',
            ## top tags
            "nHighPtTopTag", "nHighPtTopTagPlusTau23",
            ## special Vars
            "LSLjetptGT80", # leading + subl. jet pt > 80
            'isSR', # is it Signal or Control region
            'Mll', #di-lepton mass
            'METfilters',
            #Datasets
            'PD_JetHT', 'PD_SingleEle', 'PD_SingleMu', 'PD_MET',
            'isDPhiSignal',
            'RA2_muJetFilter',
            'Flag_fastSimCorridorJetCleaning'
            ]

    def listBranches(self):
        return self.branches[:]

    def __call__(self,event,keyvals):

        # prepare output
        #ret = dict([(name,-999.0) for name in self.branches])
        ret = {}
        for name in self.branches:
            if type(name) == 'tuple':
                ret[name] = []
            elif type(name) == 'str':
                ret[name] = -999

        ##############################
        ##############################
        # DATASET FLAG
        # -- needs to be adjusted manually
        ##############################
        ret['PD_JetHT'] = 0
        ret['PD_SingleEle'] = 0
        ret['PD_SingleMu'] = 0
        ret['PD_MET'] = 0
        ret['isDPhiSignal'] = 0

        if event.isData and hasattr(self,"sample"):
            if "JetHT" in self.sample: ret['PD_JetHT'] = 1
            elif "SingleEle" in self.sample: ret['PD_SingleEle'] = 1
            elif "SingleMu" in self.sample: ret['PD_SingleMu'] = 1
            elif "MET_" in self.sample: ret['PD_MET'] = 1
        if not event.isData and hasattr(self,"sample"):
            if "T1tttt" in self.sample or "T5qqqqWW" in self.sample:
                ret['isDPhiSignal'] = 1
        ##############################

        # copy basic event info:
        ret['Run'] = event.run
        ret['Event'] = event.evt
        ret['Lumi'] = event.lumi
        if hasattr(event, 'genWeight'):
            ret['genWeight'] = event.genWeight

        if hasattr(event,'xsec'):
            ret['Xsec'] = event.xsec

        if hasattr(event, 'isData'):
            ret['isData'] = event.isData

        '''
        # make python lists as Collection does not support indexing in slices
        genleps = [l for l in Collection(event,"genLep","ngenLep")]
        genparts = [l for l in Collection(event,"GenPart","nGenPart")]
        '''

        leps = [l for l in Collection(event,"LepGood","nLepGood")]
        nlep = len(leps)

        ### LEPTONS
        Selected = False

        # selected good leptons
        selectedTightLeps = []
        selectedTightLepsIdx = []
        selectedVetoLeps = []

        # anti-selected leptons
        antiTightLeps = []
        antiTightLepsIdx = []
        antiVetoLeps = []

        for idx,lep in enumerate(leps):

            # for acceptance check
            lepEta = abs(lep.eta)

            # Pt cut
            if lep.pt < 10: continue

            # Iso cut -- to be compatible with the trigger
            if lep.miniRelIso > trig_miniIsoCut: continue

            ###################
            # MUONS
            ###################
            if(abs(lep.pdgId) == 13):
                if lepEta > 2.4: continue

                ## Lower ID is POG_LOOSE (see cfg)

                # ID, IP and Iso check:
                passID = 0
                if muID=='ICHEPmediumMuonId': passID = lep.ICHEPmediumMuonId
                else: passID = lep.mediumMuonId
                passIso = lep.miniRelIso < muo_miniIsoCut
                passIP = lep.sip3d < goodMu_sip3d

                # selected muons
                if passID and passIso and passIP:
                    selectedTightLeps.append(lep); selectedTightLepsIdx.append(idx)

                    antiVetoLeps.append(lep);
                else:
                    selectedVetoLeps.append(lep)

                # anti-selected muons
                if not passIso:
                    antiTightLeps.append(lep); antiTightLepsIdx.append(idx)
                else:
                    antiVetoLeps.append(lep);

            ###################
            # ELECTRONS
            ###################

            elif(abs(lep.pdgId) == 11):

                if lepEta > eleEta: continue

                # pass variables
                passIso = False
                passConv = False

                if eleID == 'CB':
                    # ELE CutBased ID
                    eidCB = lep.eleCBID_SPRING15_25ns_ConvVetoDxyDz

                    passTightID = (eidCB == 4)
                    passMediumID = (eidCB >= 3)
                    #passLooseID = (eidCB >= 2)
                    passVetoID = (eidCB >= 1)

                elif eleID == 'MVA':
                    # ELE MVA ID
                    # check MVA WPs
                    passTightID = checkEleMVA(lep,'Tight')
                    passLooseID = checkEleMVA(lep,'VLoose')

                # selected
                if passTightID:

                    # all tight leptons are veto for anti
                    antiVetoLeps.append(lep)

                    # Iso check:
                    if lep.miniRelIso < ele_miniIsoCut: passIso = True
                    # conversion check
                    if eleID == 'MVA':
                        if lep.lostHits <= goodEl_lostHits and lep.convVeto and lep.sip3d < goodEl_sip3d: passConv = True
                    elif eleID == 'CB':
                        passConv = True # cuts already included in POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_X


                    passPostICHEPHLTHOverE = True # comment out again if (lep.hOverE < 0.04 and abs(lep.eta)>1.479) or abs(lep.eta)<=1.479 else False

                    # fill
                    if passIso and passConv and passPostICHEPHLTHOverE:
                        selectedTightLeps.append(lep); selectedTightLepsIdx.append(idx)
                    else:
                        selectedVetoLeps.append(lep)

                # anti-selected
                elif not passMediumID:#passVetoID:

                    # all anti leptons are veto for selected
                    selectedVetoLeps.append(lep)

                    # Iso check
                    passIso = lep.miniRelIso < Lep_miniIsoCut # should be true anyway
                    # other checks
                    passOther = False
                    if hasattr(lep,"hOverE"):
                        passOther = lep.hOverE > 0.01

                    # fill
                    if passIso and passOther:
                        antiTightLeps.append(lep); antiTightLepsIdx.append(idx)
                    else:
                        antiVetoLeps.append(lep)
                # Veto leptons
                elif passVetoID:
                    # the rest is veto for selected and anti
                    selectedVetoLeps.append(lep)
                    antiVetoLeps.append(lep)
        # end lepton loop

        ###################
        # EXTRA Loop for lepOther -- for anti-selected leptons
        ###################

        otherleps = [l for l in Collection(event,"LepOther","nLepOther")]
        #otherleps = []

        for idx,lep in enumerate(otherleps):

            # check acceptance
            lepEta = abs(lep.eta)
            if lepEta > 2.4: continue

            # Pt cut
            if lep.pt < 10: continue

            # Iso cut -- to be compatible with the trigger
            if lep.miniRelIso > trig_miniIsoCut: continue

            ############
            # Muons
            if(abs(lep.pdgId) == 13):
                ## Lower ID is POG_LOOSE (see cfg)

                # ID, IP and Iso check:
                #passID = lep.mediumMuonId == 1
                passIso = lep.miniRelIso > muo_miniIsoCut
                # cuts like for the LepGood muons
                #passIP = abs(lep.dxy) < 0.05 and abs(lep.dz) < 0.1

                #if passIso and passID and passIP:
                if passIso:
                    antiTightLeps.append(lep)
                    antiTightLepsIdx.append(idx)
                else:
                    antiVetoLeps.append(lep)

            ############
            # Electrons
            elif(abs(lep.pdgId) == 11):

                if(lepEta > eleEta): continue

                ## Iso selection: ele should have MiniIso < 0.4 (for trigger)
                if lep.miniRelIso > Lep_miniIsoCut: continue

                ## Set Ele IDs
                if eleID == 'CB':
                    # ELE CutBased ID
                    eidCB = lep.eleCBID_SPRING15_25ns_ConvVetoDxyDz

                    passMediumID = (eidCB >= 3)
                    passVetoID = (eidCB >= 1)
                else:
                    passMediumID = False
                    passVetoID = False

                # Cuts for Anti-selected electrons
                if not passMediumID:
                    # should always be true for LepOther

                    # other checks
                    passOther = False
                    if hasattr(lep,"hOverE"):
                        passOther = lep.hOverE > 0.01

                    #if not lep.conVeto:
                    if passOther:
                        antiTightLeps.append(lep)
                        antiTightLepsIdx.append(idx);
                    else:
                        antiVetoLeps.append(lep)

                elif passVetoID: #all Medium+ eles in LepOther
                    antiVetoLeps.append(lep)

        # choose common lepton collection: select selected or anti lepton
        if len(selectedTightLeps) > 0:
            tightLeps = selectedTightLeps
            tightLepsIdx = selectedTightLepsIdx

            vetoLeps = selectedVetoLeps

            ret['nTightLeps'] = len(tightLeps)
            ret['nTightMu'] = sum([ abs(lep.pdgId) == 13 for lep in tightLeps])
            ret['nTightEl'] = sum([ abs(lep.pdgId) == 11 for lep in tightLeps])

            ret['tightLepsIdx'] = tightLepsIdx

            ret['Selected'] = 1

            # Is second leading lepton selected, too?
            if len(selectedTightLeps) > 1:
                ret['Selected2'] = 1
            else:
                ret['Selected2'] = 0

        elif len(antiTightLeps) > 0:
            tightLeps = antiTightLeps
            tightLepsIdx = antiTightLepsIdx

            vetoLeps = antiVetoLeps

            ret['nTightLeps'] = 0
            ret['nTightMu'] = 0
            ret['nTightEl'] = 0

            ret['tightLepsIdx'] = []

            ret['Selected'] = -1

        else:
            tightLeps = []
            tightLepsIdx = []

            vetoLeps = []

            ret['nTightLeps'] = 0
            ret['nTightMu'] = 0
            ret['nTightEl'] = 0

            ret['tightLepsIdx'] = []

            ret['Selected'] = 0

        # store Tight and Veto lepton numbers
        ret['nLep'] = len(tightLeps)
        ret['nVeto'] = len(vetoLeps)

        # get number of tight el and mu
        tightEl = [lep for lep in tightLeps if abs(lep.pdgId) == 11]
        tightMu = [lep for lep in tightLeps if abs(lep.pdgId) == 13]

        ret['nEl'] = len(tightEl)
        ret['nMu'] = len(tightMu)

        # save leading lepton vars
        if len(tightLeps) > 0:
            ret['Lep_Idx'] = tightLepsIdx[0]

            ret['Lep_pt'] = tightLeps[0].pt
            ret['Lep_eta'] = tightLeps[0].eta
            ret['Lep_phi'] = tightLeps[0].phi
            ret['Lep_pdgId'] = tightLeps[0].pdgId

            ret['Lep_relIso'] = tightLeps[0].relIso03
            ret['Lep_miniIso'] = tightLeps[0].miniRelIso
            if hasattr(tightLeps[0],"hOverE"):
                ret['Lep_hOverE'] = tightLeps[0].hOverE

        elif len(leps) > 0: # fill it with leading lepton
            ret['Lep_Idx'] = 0

            ret['Lep_pt'] = leps[0].pt
            ret['Lep_eta'] = leps[0].eta
            ret['Lep_phi'] = leps[0].phi
            ret['Lep_pdgId'] = leps[0].pdgId

            ret['Lep_relIso'] = leps[0].relIso03
            ret['Lep_miniIso'] = leps[0].miniRelIso
            if hasattr(leps[0],"hOverE"):
                ret['Lep_hOverE'] = leps[0].hOverE

        # save second leading lepton vars
        if len(tightLeps) > 1:
            ret['Lep2_pt'] = tightLeps[1].pt

        ########
        ### Jets
        ########
        jets = [j for j in Collection(event,"Jet","nJet")]
        njet = len(jets)

        # Apply JEC up/down variations if needed (only MC!)
        if event.isData == False:
            if corrJEC == "central":
                pass # don't do anything
                #for jet in jets: jet.pt = jet.rawPt * jet.corr
            elif corrJEC == "up":
                for jet in jets: jet.pt = jet.rawPt * jet.corr_JECUp
            elif corrJEC == "down":
                for jet in jets: jet.pt = jet.rawPt * jet.corr_JECDown
            else:
                pass
            if smearJER!= "None":
                for jet in jets: jet.pt = returnJERSmearedPt(jet.pt,abs(jet.eta),jet.mcPt,smearJER)

        centralJet30 = []; centralJet30idx = []
        centralJet40 = []

        ret['Flag_fastSimCorridorJetCleaning'] = 1
        for i,j in enumerate(jets):
            # Cleaning up of fastsim jets (from "corridor" studies) https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSRecommendationsMoriond17#Cleaning_up_of_fastsim_jets_from
            if ret['isDPhiSignal']: #only check for signals (see condition check above)
                if j.pt>20 and abs(j.eta)<2.5 and j.mcPt == 0 and j.chHEF<0.1: ret['Flag_fastSimCorridorJetCleaning'] = 0  
            if j.pt>30 and abs(j.eta)<centralEta:
                centralJet30.append(j)
                centralJet30idx.append(i)
            if j.pt>40 and abs(j.eta)<centralEta:
                centralJet40.append(j)

        # jets 30 (cmg cleaning only)
        nJetC = len(centralJet30)
        ret['nJets']   = nJetC
        ret['nJets30']   = nJetC
        # store indeces
        ret['Jets30Idx'] = centralJet30idx
        #print "nJets30:", len(centralJet30), " nIdx:", len(centralJet30idx)

        # jets 40
        nJet40C = len(centralJet40)
        ret['nJets40']   = nJet40C

        ##############################
        ## Local cleaning from leptons
        ##############################
        cJet30Clean = []
        dRminCut = 0.4

        # Do cleaning a la CMG: clean max 1 jet for each lepton (the nearest)
        cJet30Clean = centralJet30

        for lep in tightLeps:
            # don't clean LepGood, only LepOther
            if lep not in otherleps: continue

            jNear, dRmin = None, 99
            # find nearest jet
            for jet in centralJet30:

                dR = jet.p4().DeltaR(lep.p4())
                if dR < dRmin:
                    jNear, dRmin = jet, dR

            # remove nearest jet
            if dRmin < dRminCut:
                cJet30Clean.remove(jNear)

        if nJetC !=  len(cJet30Clean) and False:
            print "Non-clean jets: ", nJetC, "\tclean jets:", len(cJet30Clean)
            print jets
            print leps
            print otherleps

        # cleaned jets
        nJet30C = len(cJet30Clean)
        ret['nJets30Clean'] = len(cJet30Clean)

        if nJet30C > 0:
            ret['Jet1_pt'] = cJet30Clean[0].pt
        if nJet30C > 1:
            ret['Jet2_pt'] = cJet30Clean[1].pt

        # imho, use Jet2_pt > 80 instead
        ret['LSLjetptGT80'] = 1 if sum([j.pt>80 for j in cJet30Clean])>=2 else 0

        ret['htJet30j']  = sum([j.pt for j in cJet30Clean])
        ret['htJet30ja'] = sum([j.pt for j in jets if j.pt>30])

        ret['htJet40j']  = sum([j.pt for j in centralJet40])

        ret['HT'] = ret['htJet30j']

        ## B tagging WPs for CSVv2 (CSV-IVF)
        ## from: https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideBTagging#Preliminary_working_or_operating

        # WP defined on top
        btagWP = btag_MediumWP

        BJetMedium30 = []
        BJetMedium40 = []

        nBJetDeep = 0

        for i,j in enumerate(cJet30Clean):
            if j.btagCSV > btagWP:
                BJetMedium30.append(j)
            if (j.DFb + j.DFbb) > btag_DeepMediumWP:
                nBJetDeep += 1

        for i,j in enumerate(centralJet40):
            if j.btagCSV > btagWP:
                BJetMedium40.append(j)

        # using cleaned collection!
        ret['nBJet']   = len(BJetMedium30)
        ret['nBJets30']   = len(BJetMedium30)

        ret['nBJetDeep'] = nBJetDeep

        # using normal collection
        ret['nBJets40']   = len(BJetMedium40)

        ######
        # MET
        #####
        metp4 = ROOT.TLorentzVector(0,0,0,0)
        if hasattr(event, 'metMuEGClean_pt'):
            metp4.SetPtEtaPhiM(event.metMuEGClean_pt,event.metMuEGClean_eta,event.metMuEGClean_phi,event.metMuEGClean_mass)
        else:
            metp4.SetPtEtaPhiM(event.met_pt,event.met_eta,event.met_phi,event.met_mass)

        # recalc MET
        if corrJEC != "central" or smearJER!= "None":
            ## get original jet collection
            metp4 = getRecalcMET(metp4,event,corrJEC,smearJER)
        
        Genmetp4 = ROOT.TLorentzVector(0,0,0,0)
        
        if not event.isData:
            Genmetp4.SetPtEtaPhiM(event.met_genPt,event.met_genEta,event.met_genPhi,0)

        ret["MET"] = metp4.Pt()

        ## MET NO HF
#        metNoHFp4 = ROOT.TLorentzVector(0,0,0,0)
#        metNoHFp4.SetPtEtaPhiM(event.metNoHF_pt,event.metNoHF_eta,event.metNoHF_phi,event.metNoHF_mass)
#        ret["METNoHF"] = metNoHFp4.Pt()

        ## MET FILTERS for data
        if event.isData:
            #ret['METfilters'] = event.Flag_goodVertices and event.Flag_HBHENoiseFilter_fix and event.Flag_CSCTightHaloFilter and event.Flag_eeBadScFilter)
            #ret['METfilters'] = event.nVert > 0 and event.Flag_HBHENoiseFilter_fix and event.Flag_CSCTightHaloFilter and event.Flag_eeBadScFilter
            # add HCAL Iso Noise
            if hasattr(event,"Flag_eeBadScFilter"):
                #old ret['METfilters'] = event.Flag_goodVertices and event.Flag_CSCTightHaloFilter and event.Flag_eeBadScFilter and event.Flag_HBHENoiseFilter_fix and event.Flag_HBHENoiseIsoFilter
                #for ICHEP; same as in eventVars_1l_filters.py
                #ret['METfilters'] = event.Flag_HBHENoiseFilter and event.Flag_HBHENoiseIsoFilter and event.Flag_EcalDeadCellTriggerPrimitiveFilter and  event.Flag_goodVertices and event.Flag_eeBadScFilter and event.Flag_globalTightHalo2016Filter and event.Flag_badChargedHadronFilter and event.Flag_badMuonFilter
                #for Moriond 2017: use updated badChargedHadron and badPFMuon filters (Ece's Summer2016 implementation). Do NOT use Flag_badMuons and Flag_duplicateMuons (they are only to be used if new tails would appear in the metMuEGClean collection comparing to the METUncorrected collection)
                ret['METfilters'] = event.Flag_HBHENoiseFilter and event.Flag_HBHENoiseIsoFilter and event.Flag_EcalDeadCellTriggerPrimitiveFilter and  event.Flag_goodVertices and event.Flag_eeBadScFilter and event.Flag_globalTightHalo2016Filter and event.Flag_badChargedHadronSummer2016 and event.Flag_badMuonSummer2016
            else:
                ret['METfilters'] = 1
        else:
            ret['METfilters'] = 1


        # deltaPhi between the (single) lepton and the reconstructed W (lep + MET)
        dPhiLepW = -999 # set default value to -999 to spot "empty" entries
        GendPhiLepW = -999 # set default value to -999 to spot "empty" entries
#        dPhiLepWNoHF = -999 # set default value to -999 to spot "empty" entries
        # LT of lepton and MET
        LT = -999
        GenLT = -999
#        LTNoHF = -999
        Lp = -99
        MT = -99
        MT_misET=-99
        if len(tightLeps) >=1:
            recoWp4 =  tightLeps[0].p4() + metp4
            GenrecoWp4 =  tightLeps[0].p4() + Genmetp4
            GendPhiLepW = tightLeps[0].p4().DeltaPhi(GenrecoWp4)
            GenLT = tightLeps[0].pt + Genmetp4.Pt()
            dPhiLepW = tightLeps[0].p4().DeltaPhi(recoWp4)
            LT = tightLeps[0].pt + metp4.Pt()
            Lp = tightLeps[0].pt / recoWp4.Pt() * cos(dPhiLepW)

            #MT = recoWp4.Mt() # doesn't work
            MT = sqrt(2*metp4.Pt()*tightLeps[0].pt * (1-cos(dPhiLepW)))
            MT_misET = sqrt(2*metp4.Pt()*tightLeps[0].pt * (1-cos(tightLeps[0].p4().DeltaPhi(metp4))))

            ## no HF
#            recoWNoHFp4 =  tightLeps[0].p4() + metNoHFp4
#            dPhiLepWNoHF = tightLeps[0].p4().DeltaPhi(recoWNoHFp4)
#            LTNoHF = tightLeps[0].pt + event.metNoHF_pt

        ret["DeltaPhiLepW"] = dPhiLepW
        dPhi = abs(dPhiLepW) # nickname for absolute dPhiLepW
        ret['dPhi'] = dPhi
        ret['ST'] = LT
        ret['LT'] = LT
        ret['Lp'] = Lp
        ret['MT'] = MT
        ret['MT_misET'] = MT_misET
        ret['GendPhi'] = abs(GendPhiLepW)
        ret['GenLT'] = GenLT
        ret['GenMET'] = Genmetp4.Pt()
        # no HF
#        dPhiNoHF = abs(dPhiLepWNoHF) # nickname for absolute dPhiLepW
#        ret['dPhiNoHF'] = dPhiNoHF
#        ret['LTNoHF'] = LTNoHF

        #####################
        ## SIGNAL REGION FLAG
        #####################

        ## Signal region flag
        # isSR SR vs CR flag
        isSR = 0

        # 0-B SRs -- simplified dPhi
        if ret['nBJet'] == 0:
            if LT < 250:   isSR = 0
            elif LT > 250: isSR = dPhi > 0.75
            # BLIND data
            if event.isData and nJet30C >= 5:
                isSR = - isSR
        # Multi-B SRs
        elif nJet30C < 99:
            if LT < 250:   isSR = 0
            elif LT < 350: isSR = dPhi > 1.0
            elif LT < 600: isSR = dPhi > 0.75
            elif LT > 600: isSR = dPhi > 0.5

            # BLIND data
            if event.isData and nJet30C >= 6:
                isSR = - isSR

        ret['isSR'] = isSR

        #############
        ## Playground
        #############

        # di-lepton mass: opposite-sign, same flavour
        Mll = 0

        if len(tightLeps) > 1:

            lep1 = tightLeps[0]
            id1 = lep1.pdgId

            for lep2 in leps[1:]:
                if lep2.pdgId + lep1.pdgId == 0:
                    dilepP4 = lep1.p4() + lep2.p4()
                    Mll = dilepP4.M()

        ret['Mll'] = Mll

        # RA2 proposed filter
        ret['RA2_muJetFilter'] = True
        for j in cJet30Clean:
            if j.pt > 200 and j.muEF > 0.5 and abs(acos(cos(j.phi-metp4.Phi()))) > (pi - 0.4):
                ret['RA2_muJetFilter'] = False

        return ret

# Main function for test
if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf = EventVars1L_base()
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf(ev,{})
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)
