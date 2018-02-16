import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

### NB: Commented lines refer to samples available in RunIIFall15MiniAODv2 but not yet in RunIISpring16MiniAODv1

### ----------------------------- 25 ns ----------------------------------------

# TTbar cross section: NNLO, https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO (172.5)


TTLep_pow       = kreator.makeMCComponent("TTLep_pow", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2))
TTSemiLep_pow   = kreator.makeMCComponent("TTSemiLep_pow", "/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 2*831.76*(3*0.108)*(1-3*0.108) )
TTHad_pow       = kreator.makeMCComponent("TTHad_pow", "/TTToHadronic_mtop178p5_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 831.76*(0.676**2))

TTs = [
TTLep_pow,
TTSemiLep_pow,
TTHad_pow
]

### TTV
TTWToLNu            = kreator.makeMCComponent("TTWToLNu", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.2043)
TTWToQQ             = kreator.makeMCComponent("TTWToQQ", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.40620)
TTW_LO              = kreator.makeMCComponent("TTW_LO", "/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.6105 )
TTZToQQ             = kreator.makeMCComponent("TTZToQQ","/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.5297)
TTZToLLNuNu         = kreator.makeMCComponent("TTZToLLNuNu", "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.2728) # x-sec should be 0.2529, use other value to sync
TTZToLLNuNu_m1to10  = kreator.makeMCComponent("TTZToLLNuNu_m1to10","/TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.0493)
TTZ_LO              = kreator.makeMCComponent("TTZ_LO", "/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root",  0.5297/0.692)
TTGJets             = kreator.makeMCComponent("TTGJets",    "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 3.697)
#TTGJets_ext         = kreator.makeMCComponent("TTGJets_ext","/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/MINIAODSIM", "CMS", ".*root", 3.697)

TTH_pow             = kreator.makeMCComponent("TTH_pow", "/ttH_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.5071)
TTHnobb_fxfx        = kreator.makeMCComponent("TTHnobb_fxfx", "/ttHJetToNonbb_M125_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.5071*(1-0.582))
TTHnobb_pow         = kreator.makeMCComponent("TTHnobb_pow", "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.5071*(1-0.582))
TTHtautau_pow       = kreator.makeMCComponent("TTHtautau_pow", "/ttHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 0.5071*0.06272)

TZQToLL             = kreator.makeMCComponent("TZQToLL","/tZq_ll_4f_ckm_NLO_TuneCP5_PSweights_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.07358)

TTV = [
TTWToLNu,
TTWToQQ,
TTW_LO,
TTZToQQ,
TTZToLLNuNu,
TTZToLLNuNu_m1to10,
TTZ_LO,
TTGJets,
#TTGJets_ext,
TTH_pow,
TTHnobb_fxfx,
TTHnobb_pow,
TTHtautau_pow,
TZQToLL
]


#DYJetsToLL_M10to50_LO = kreator.makeMCComponent("DYJetsToLL_M10to50_LO", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer17MiniAOD-92X_upgrade2017_realistic_v10-v1/MINIAODSIM",  "CMS", ".*root", 18610, useAAA=Tru
DYJetsToLL_M50_LO   = kreator.makeMCComponent("DYJetsToLL_M50_LO", "/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-RECOSIMstep_94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)
DYJetsToLL_M50      = kreator.makeMCComponent("DYJetsToLL_M50", "/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 2008.*3)

VJets = [
    #DYJetsToLL_M10to50_LO,
    DYJetsToLL_M50_LO,
    DYJetsToLL_M50
]


# ====== TT + DIBOSON, 4-top =====

#TTTT = kreator.makeMCComponent("TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.009103)
#TTWH = kreator.makeMCComponent("TTWH", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.00114)
#TTZH = kreator.makeMCComponent("TTZH", "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.001138)
#TTWW = kreator.makeMCComponent("TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM", "CMS", ".*root", 0.006977)
#TTHH = kreator.makeMCComponent("TTHH", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.0006666)
#
#TTTJ = kreator.makeMCComponent("TTTJ", "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.0003987)
#TTTW = kreator.makeMCComponent("TTTW", "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v3/MINIAODSIM", "CMS", ".*root", 0.0007273)
#
#TTXXs = [ TTTT, TTWH, TTZH, TTWW, TTHH, TTTJ, TTTW ]

## Triboson

WW = kreator.makeMCComponent("WW", "/WW_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 63.21 * 1.82)
WZ = kreator.makeMCComponent("WZ", "/WZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 47.13, useAAA=True )
ZZ = kreator.makeMCComponent("ZZ", "/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 16.523 )

WWTo2L2Nu = kreator.makeMCComponent("WWTo2L2Nu", "/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 10.481 )
WW_DPS = kreator.makeMCComponent("WW_DPS", "/WW_DoubleScattering_13TeV-pythia8_TuneCP5/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 1.921)

WZTo3LNu_fxfx = kreator.makeMCComponent("WZTo3LNu_fxfx", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 5.063)

ZZTo4L = kreator.makeMCComponent("ZZTo4L", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v2/MINIAODSIM", "CMS", ".*root", 1.256)
ZZTo4L_ext = kreator.makeMCComponent("ZZTo4L_ext", "/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10_ext1-v1/MINIAODSIM", "CMS", ".*root", 1.256)
ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM", "CMS", ".*root", 0.564)

DiBosons = [
    WW,
    WZ,
    ZZ,
    WZTo3LNu_fxfx,
    WWTo2L2Nu,
    WW_DPS,
    ZZTo4L,
    ZZTo4L_ext,
    ZZTo2L2Nu
]

#WWW = kreator.makeMCComponent("WWW", "/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 0.2086)
#WWZ = kreator.makeMCComponent("WWZ", "/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",  0.1651 )
#WZZ = kreator.makeMCComponent("WZZ", "/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",  0.05565 )
#ZZZ = kreator.makeMCComponent("ZZZ", "/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root",  0.01398 )

TriBosons = [
#WWW,
#WZZ,
#WWZ,
#ZZZ,
]

### ----------------------------- summary ----------------------------------------

mcSamples = TTs + VJets + DiBosons + TriBosons + TTV

samples = mcSamples

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

if __name__ == "__main__":
    from CMGTools.RootTools.samples.tools import runMain
    runMain(samples,localobjs=locals())
