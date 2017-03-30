import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### ----------------------------- 25 ns ----------------------------------------
# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)


# http://t3serv001.mit.edu/~paus/qcut/ttbar/CrossSectionsAndMatching.txt
TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_100 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_100", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-10_Mphi-100_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.976e-01*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_10 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_10", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-10_Mphi-10_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.522e-02*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_15 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_15", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-10_Mphi-15_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.950e-02*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_50 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_50", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-10_Mphi-50_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.091e-01*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_10000 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_10000", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-10000_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.814e-09*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_100 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_100", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.932e-01*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_10 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_10", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-10_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 4.517e-01*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_200 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_200", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-200_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 8.786e-02*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_20 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_20", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-20_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 4.117e-01*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_300 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_300", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-300_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.950e-02*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_500 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_500", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-500_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 5.163e-03*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_50 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_50", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-1_Mphi-50_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.080e-01*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_10 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_10", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-50_Mphi-10_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.405e-03*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_200 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_200", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-50_Mphi-200_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 8.476e-02*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_300 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_300", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-50_Mphi-300_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.845e-02*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_50 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_50", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-50_Mphi-50_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.928e-03*0.104976 )
TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_95 = kreator.makeMCComponent("TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_95", "/TTbarDMJets_DiLept_pseudoscalar_Mchi-50_Mphi-95_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.072e-02*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_100 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_100", "/TTbarDMJets_DiLept_scalar_Mchi-10_Mphi-100_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 7.417e-01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_10 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_10", "/TTbarDMJets_DiLept_scalar_Mchi-10_Mphi-10_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.011e-01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_15 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_15", "/TTbarDMJets_DiLept_scalar_Mchi-10_Mphi-15_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.279e-01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_50 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_50", "/TTbarDMJets_DiLept_scalar_Mchi-10_Mphi-50_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.097e+00*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_10000 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_10000", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-10000_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.342e-09*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_100 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_100", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-100_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 7.205e-01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_10 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_10", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-10_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.136e+01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_200 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_200", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-200_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.016e-01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_20 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_20", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-20_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.095e+01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_300 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_300", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-300_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.045e-02*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_500 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_500", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-500_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 4.947e-03*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_50 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_50", "/TTbarDMJets_DiLept_scalar_Mchi-1_Mphi-50_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.088e+00*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_10 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_10", "/TTbarDMJets_DiLept_scalar_Mchi-50_Mphi-10_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.078e-03*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_200 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_200", "/TTbarDMJets_DiLept_scalar_Mchi-50_Mphi-200_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 1.003e-01*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_300 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_300", "/TTbarDMJets_DiLept_scalar_Mchi-50_Mphi-300_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 3.046e-02*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_50 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_50", "/TTbarDMJets_DiLept_scalar_Mchi-50_Mphi-50_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 2.567e-03*0.104976 )
TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_95 = kreator.makeMCComponent("TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_95", "/TTbarDMJets_DiLept_scalar_Mchi-50_Mphi-95_TuneCUETP8M1_v2_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 7.202e-03*0.104976 )

TTbarDMJets_pseudoscalar_Mchi_10_Mphi_100_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_10_Mphi_100_ext1", "/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.976e-01 )
TTbarDMJets_pseudoscalar_Mchi_10_Mphi_10_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_10_Mphi_10_ext1", "/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.522e-02 )
TTbarDMJets_pseudoscalar_Mchi_10_Mphi_15_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_10_Mphi_15_ext1", "/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-15_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.950e-02 )
TTbarDMJets_pseudoscalar_Mchi_10_Mphi_50_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_10_Mphi_50_ext1", "/TTbarDMJets_pseudoscalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.091e-01 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_10000_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_10000_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.814e-09 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_100_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_100_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.932e-01 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_10_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_10_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 4.517e-01, useAAA=True )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_200_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_200_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 8.786e-02 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_20_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_20_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 4.117e-01 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_300_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_300_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.950e-02 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_500_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_500_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 5.163e-03 )
TTbarDMJets_pseudoscalar_Mchi_1_Mphi_50_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_1_Mphi_50_ext1", "/TTbarDMJets_pseudoscalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.080e-01 )
TTbarDMJets_pseudoscalar_Mchi_50_Mphi_10_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_50_Mphi_10_ext1", "/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.405e-03 )
TTbarDMJets_pseudoscalar_Mchi_50_Mphi_200_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_50_Mphi_200_ext1", "/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 8.476e-02 )
TTbarDMJets_pseudoscalar_Mchi_50_Mphi_300_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_50_Mphi_300_ext1", "/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.845e-02 )
TTbarDMJets_pseudoscalar_Mchi_50_Mphi_50_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_50_Mphi_50_ext1", "/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.928e-03 )
TTbarDMJets_pseudoscalar_Mchi_50_Mphi_95_ext1 = kreator.makeMCComponent("TTbarDMJets_pseudoscalar_Mchi_50_Mphi_95_ext1", "/TTbarDMJets_pseudoscalar_Mchi-50_Mphi-95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.072e-02 )

TTbarDMJets_scalar_Mchi_10_Mphi_100_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_10_Mphi_100_ext1", "/TTbarDMJets_scalar_Mchi-10_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 7.417e-01 )
TTbarDMJets_scalar_Mchi_10_Mphi_10_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_10_Mphi_10_ext1", "/TTbarDMJets_scalar_Mchi-10_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.011e-01 )
TTbarDMJets_scalar_Mchi_10_Mphi_15_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_10_Mphi_15_ext1", "/TTbarDMJets_scalar_Mchi-10_Mphi-15_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.279e-01 )
TTbarDMJets_scalar_Mchi_10_Mphi_50_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_10_Mphi_50_ext1", "/TTbarDMJets_scalar_Mchi-10_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.097e+00 )
TTbarDMJets_scalar_Mchi_1_Mphi_10000_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_10000_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-10000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.342e-09 )
TTbarDMJets_scalar_Mchi_1_Mphi_100_ext2 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_100_ext2", "/TTbarDMJets_scalar_Mchi-1_Mphi-100_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 7.205e-01 )
TTbarDMJets_scalar_Mchi_1_Mphi_100_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_100_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 7.205e-01 )
TTbarDMJets_scalar_Mchi_1_Mphi_10_ext2 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_10_ext2", "/TTbarDMJets_scalar_Mchi-1_Mphi-10_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 2.136e+01 )
TTbarDMJets_scalar_Mchi_1_Mphi_10_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_10_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.136e+01 )
TTbarDMJets_scalar_Mchi_1_Mphi_200_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_200_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.016e-01 )
TTbarDMJets_scalar_Mchi_1_Mphi_20_ext2 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_20_ext2", "/TTbarDMJets_scalar_Mchi-1_Mphi-20_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 1.095e+01 )
TTbarDMJets_scalar_Mchi_1_Mphi_20_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_20_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-20_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.095e+01 )
TTbarDMJets_scalar_Mchi_1_Mphi_300_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_300_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v4/MINIAODSIM", "CMS", ".*root", 3.045e-02 )
TTbarDMJets_scalar_Mchi_1_Mphi_500_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_500_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 4.947e-03 )
TTbarDMJets_scalar_Mchi_1_Mphi_50_ext2 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_50_ext2", "/TTbarDMJets_scalar_Mchi-1_Mphi-50_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1/MINIAODSIM", "CMS", ".*root", 3.088e+00 )
TTbarDMJets_scalar_Mchi_1_Mphi_50_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_1_Mphi_50_ext1", "/TTbarDMJets_scalar_Mchi-1_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.088e+00 )
TTbarDMJets_scalar_Mchi_50_Mphi_10_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_50_Mphi_10_ext1", "/TTbarDMJets_scalar_Mchi-50_Mphi-10_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.078e-03 )
TTbarDMJets_scalar_Mchi_50_Mphi_200_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_50_Mphi_200_ext1", "/TTbarDMJets_scalar_Mchi-50_Mphi-200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.003e-01 )
TTbarDMJets_scalar_Mchi_50_Mphi_300_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_50_Mphi_300_ext1", "/TTbarDMJets_scalar_Mchi-50_Mphi-300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.046e-02 )
TTbarDMJets_scalar_Mchi_50_Mphi_50_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_50_Mphi_50_ext1", "/TTbarDMJets_scalar_Mchi-50_Mphi-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 2.567e-03 )
TTbarDMJets_scalar_Mchi_50_Mphi_95_ext1 = kreator.makeMCComponent("TTbarDMJets_scalar_Mchi_50_Mphi_95_ext1", "/TTbarDMJets_scalar_Mchi-50_Mphi-95_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 7.202e-03 )


samples = [TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_100, TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_10, TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_15, TTbarDMJets_DiLept_pseudoscalar_Mchi_10_Mphi_50, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_10000, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_100, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_10, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_200, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_20, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_300, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_500, TTbarDMJets_DiLept_pseudoscalar_Mchi_1_Mphi_50, TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_10, TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_200, TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_300, TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_50, TTbarDMJets_DiLept_pseudoscalar_Mchi_50_Mphi_95, TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_100, TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_10, TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_15, TTbarDMJets_DiLept_scalar_Mchi_10_Mphi_50, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_10000, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_100, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_10, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_200, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_20, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_300, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_500, TTbarDMJets_DiLept_scalar_Mchi_1_Mphi_50, TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_10, TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_200, TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_300, TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_50, TTbarDMJets_DiLept_scalar_Mchi_50_Mphi_95, TTbarDMJets_pseudoscalar_Mchi_10_Mphi_100_ext1, TTbarDMJets_pseudoscalar_Mchi_10_Mphi_10_ext1, TTbarDMJets_pseudoscalar_Mchi_10_Mphi_15_ext1, TTbarDMJets_pseudoscalar_Mchi_10_Mphi_50_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_10000_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_100_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_10_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_200_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_20_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_300_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_500_ext1, TTbarDMJets_pseudoscalar_Mchi_1_Mphi_50_ext1, TTbarDMJets_pseudoscalar_Mchi_50_Mphi_10_ext1, TTbarDMJets_pseudoscalar_Mchi_50_Mphi_200_ext1, TTbarDMJets_pseudoscalar_Mchi_50_Mphi_300_ext1, TTbarDMJets_pseudoscalar_Mchi_50_Mphi_50_ext1, TTbarDMJets_pseudoscalar_Mchi_50_Mphi_95_ext1, TTbarDMJets_scalar_Mchi_10_Mphi_100_ext1, TTbarDMJets_scalar_Mchi_10_Mphi_10_ext1, TTbarDMJets_scalar_Mchi_10_Mphi_15_ext1, TTbarDMJets_scalar_Mchi_10_Mphi_50_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_10000_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_100_ext2, TTbarDMJets_scalar_Mchi_1_Mphi_100_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_10_ext2, TTbarDMJets_scalar_Mchi_1_Mphi_10_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_200_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_20_ext2, TTbarDMJets_scalar_Mchi_1_Mphi_20_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_300_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_500_ext1, TTbarDMJets_scalar_Mchi_1_Mphi_50_ext2, TTbarDMJets_scalar_Mchi_1_Mphi_50_ext1, TTbarDMJets_scalar_Mchi_50_Mphi_10_ext1, TTbarDMJets_scalar_Mchi_50_Mphi_200_ext1, TTbarDMJets_scalar_Mchi_50_Mphi_300_ext1, TTbarDMJets_scalar_Mchi_50_Mphi_50_ext1, TTbarDMJets_scalar_Mchi_50_Mphi_95_ext1]





### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in samples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
