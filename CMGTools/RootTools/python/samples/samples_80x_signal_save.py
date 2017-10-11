import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### SUSY2016B

#Scalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-1500_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")
#mcScalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph = [Scalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph]

SMS_T1tttt_TuneCUETP8M1 = kreator.makeMCComponent("SMS_T1tttt_TuneCUETP8M1","/Scalar_MonoTop_LO_Mphi-1500_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")
mcSamplesT1tttt = [SMS_T1tttt_TuneCUETP8M1]

#SMS_T1tttt_TuneCUETP8M1 = kreator.makeMCComponent("SMS_T1tttt_TuneCUETP8M1","/SMS-T1tttt_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root")
#mcSamplesT1tttt = [SMS_T1tttt_TuneCUETP8M1]

SMS_T5qqqqVV_TuneCUETP8M1 = kreator.makeMCComponent("SMS_T5qqqqVV_TuneCUETP8M1","/SMS-T5qqqqVV_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root")
mcSamplesT5qqqqVV = [SMS_T5qqqqVV_TuneCUETP8M1]
### OFFICIAL SMS SIGNALS



#mcSamples = mcScalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph
mcSamples=mcSamplesT1tttt
#mcSamples=mcScalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph
samples = mcSamples

dataSamples = []

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

for comp in dataSamples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
