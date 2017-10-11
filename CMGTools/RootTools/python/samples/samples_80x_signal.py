import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### SUSY2016B

Scalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-1500_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_1700_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_1700_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-1700_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_1900_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_1900_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-1900_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_2100_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_2100_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-2100_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_2500_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_2500_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-2500_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_2700_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_2700_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-2700_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_3100_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_3100_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-3100_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_3300_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_3300_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-3300_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_3500_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_3500_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-3500_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_3700_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_3700_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-3700_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_3900_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_3900_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-3900_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Scalar_MonoTop_LO_Mphi_4100_Mchi_100_13TeV_madgraph = kreator.makeMCComponent("Scalar_MonoTop_LO_Mphi_4100_Mchi_100_13TeV_madgraph","/Scalar_MonoTop_LO_Mphi-4100_Mchi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")
scalor_monotop = [Scalar_MonoTop_LO_Mphi_1500_Mchi_100_13TeV_madgraph, Scalar_MonoTop_LO_Mphi_1700_Mchi_100_13TeV_madgraph, Scalar_MonoTop_LO_Mphi_1900_Mchi_100_13TeV_madgraph, Scalar_MonoTop_LO_Mphi_2100_Mchi_100_13TeV_madgraph, Scalar_MonoTop_LO_Mphi_2500_Mchi_100_13TeV_madgraph, Scalar_MonoTop_LO_Mphi_2700_Mchi_100_13TeV_madgraph, Scalar_MonoTop_LO_Mphi_3100_Mchi_100_13TeV_madgraph,
                  Scalar_MonoTop_LO_Mphi_3300_Mchi_100_13TeV_madgraph,
                  Scalar_MonoTop_LO_Mphi_3500_Mchi_100_13TeV_madgraph, 
                  Scalar_MonoTop_LO_Mphi_3700_Mchi_100_13TeV_madgraph,
                  Scalar_MonoTop_LO_Mphi_3900_Mchi_100_13TeV_madgraph,
                  Scalar_MonoTop_LO_Mphi_4100_Mchi_100_13TeV_madgraph
                  ]

SMS_T5qqqqVV_TuneCUETP8M1 = kreator.makeMCComponent("SMS_T5qqqqVV_TuneCUETP8M1","/SMS-T5qqqqVV_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16Fast_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM","CMS",".*root")
mcSamplesT5qqqqVV = [SMS_T5qqqqVV_TuneCUETP8M1]

### OFFICIAL SMS SIGNALS

Vector_MonoTop_NLO_Mphi_2500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph = kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph","/Vector_MonoTop_NLO_Mphi-2500_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1000_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph = kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1000_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph","/Vector_MonoTop_NLO_Mphi-1000_Mchi-600_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS",".*root")

Vector_MonoTop_NLO_Mphi_300_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph = kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_300_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph","/Vector_MonoTop_NLO_Mphi-300_Mchi-100_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1000_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph = kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1000_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1000_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1000_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph = kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1000_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1000_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1000_Mchi_350_gSM_0p25_gDM_1p0_13TeV_madgraph = kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1000_Mchi_350_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1000_Mchi-350_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")


Vector_MonoTop_NLO_Mphi_100_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_100_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-100_Mchi-100_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_100_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_100_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-100_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_125_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_125_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-125_Mchi-100_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1500_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1500_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1500_Mchi-1000_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1500_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1500_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1500_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1500_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1500_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1500_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1500_Mchi-600_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1750_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1750_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1750_Mchi-1000_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1750_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1750_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1750_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1750_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1750_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1750_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_1750_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_1750_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-1750_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2000_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2000_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2000_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2000_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2000_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2000_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2000_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2000_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2000_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_200_Mchi_10_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_200_Mchi_10_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-200_Mchi-10_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_200_Mchi_150_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_200_Mchi_150_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-200_Mchi-150_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_200_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_200_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-200_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_200_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_200_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-200_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_200_Mchi_50_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_200_Mchi_50_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-200_Mchi-50_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_20_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_20_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-20_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_20_Mchi_75_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_20_Mchi_75_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-20_Mchi-75_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2250_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2250_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2250_Mchi-1000_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2250_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2250_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2250_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2250_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2250_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2250_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2250_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2250_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2250_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2500_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2500_Mchi_1000_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2500_Mchi-1000_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2500_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2500_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2500_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")


Vector_MonoTop_NLO_Mphi_2500_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2500_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2500_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2500_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2500_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2500_Mchi-600_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_2500_Mchi_700_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_2500_Mchi_700_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-2500_Mchi-700_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_3000_Mchi_1600_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_3000_Mchi_1600_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-3000_Mchi-1600_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_3000_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_3000_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-3000_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_3000_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_3000_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-3000_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")


Vector_MonoTop_NLO_Mphi_300_Mchi_10_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_300_Mchi_10_gSM_0p25_gDM_1p0_13TeV_madgraph/",  "/Vector_MonoTop_NLO_Mphi-300_Mchi-10_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_300_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_300_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-300_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_300_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_300_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-300_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_400_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_400_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-400_Mchi-100_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_400_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_400_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-400_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_400_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_400_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-400_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_500_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_500_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-500_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_500_Mchi_200_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_500_Mchi_200_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-500_Mchi-200_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-500_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_500_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_500_Mchi_500_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-500_Mchi-500_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_500_Mchi_50_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_500_Mchi_50_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-500_Mchi-50_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_50_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_50_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-50_Mchi-100_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_750_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_750_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-750_Mchi-100_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_750_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_750_Mchi_1_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-750_Mchi-1_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_750_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_750_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-750_Mchi-300_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_750_Mchi_350_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_750_Mchi_350_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-750_Mchi-350_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_750_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_750_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-750_Mchi-600_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")

Vector_MonoTop_NLO_Mphi_750_Mchi_700_gSM_0p25_gDM_1p0_13TeV_madgraph= kreator.makeMCComponent("Vector_MonoTop_NLO_Mphi_750_Mchi_700_gSM_0p25_gDM_1p0_13TeV_madgraph", "/Vector_MonoTop_NLO_Mphi-750_Mchi-700_gSM-0p25_gDM-1p0_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS",".*root")




vector_monotop = [Vector_MonoTop_NLO_Mphi_300_Mchi_100_gSM_0p25_gDM_1p0_13TeV_madgraph,
                  Vector_MonoTop_NLO_Mphi_1000_Mchi_600_gSM_0p25_gDM_1p0_13TeV_madgraph,
                  Vector_MonoTop_NLO_Mphi_2500_Mchi_300_gSM_0p25_gDM_1p0_13TeV_madgraph
                  ]
mcSamples= vector_monotop



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
