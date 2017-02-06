import PhysicsTools.HeppyCore.framework.config as cfg
import os

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = "$CMSSW_BASE/src/CMGTools/SUSYAnalysis/data"  # use environmental variable, useful for instance to run on CRAB
prompt_json=dataDir+'/Cert_271036-284044_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
json = "$CMSSW_BASE/src/CMGTools/SUSYAnalysis/data/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"



JetHT_Run2016B_PromptReco_v1     =   kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v1" , "/JetHT/Run2016B-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016B_PromptReco_v2     =   kreator.makeDataComponent("JetHT_Run2016B_PromptReco_v2" , "/JetHT/Run2016B-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016C_PromptReco_v2     =   kreator.makeDataComponent("JetHT_Run2016C_PromptReco_v2" , "/JetHT/Run2016C-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016D_PromptReco_v2     =   kreator.makeDataComponent("JetHT_Run2016D_PromptReco_v2" , "/JetHT/Run2016D-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016E_PromptReco_v2     =   kreator.makeDataComponent("JetHT_Run2016E_PromptReco_v2" , "/JetHT/Run2016E-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016F_PromptReco_v1     =   kreator.makeDataComponent("JetHT_Run2016F_PromptReco_v1" , "/JetHT/Run2016F-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016G_PromptReco_v1     =   kreator.makeDataComponent("JetHT_Run2016G_PromptReco_v1" , "/JetHT/Run2016G-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
JetHT_Run2016H_PromptReco_v1     =   kreator.makeDataComponent("JetHT_Run2016H_PromptReco_v1" , "/JetHT/Run2016H-PromptReco-v1/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016H_PromptReco_v2     =   kreator.makeDataComponent("JetHT_Run2016H_PromptReco_v2" , "/JetHT/Run2016H-PromptReco-v2/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016H_PromptReco_v3     =   kreator.makeDataComponent("JetHT_Run2016H_PromptReco_v3" , "/JetHT/Run2016H-PromptReco-v3/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016B_PromptReco_v1     =   kreator.makeDataComponent("MET_Run2016B_PromptReco_v1" , "/MET/Run2016B-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016B_PromptReco_v2     =   kreator.makeDataComponent("MET_Run2016B_PromptReco_v2" , "/MET/Run2016B-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016C_PromptReco_v2     =   kreator.makeDataComponent("MET_Run2016C_PromptReco_v2" , "/MET/Run2016C-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016D_PromptReco_v2     =   kreator.makeDataComponent("MET_Run2016D_PromptReco_v2" , "/MET/Run2016D-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016E_PromptReco_v2     =   kreator.makeDataComponent("MET_Run2016E_PromptReco_v2" , "/MET/Run2016E-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016F_PromptReco_v1     =   kreator.makeDataComponent("MET_Run2016F_PromptReco_v1" , "/MET/Run2016F-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016G_PromptReco_v1     =   kreator.makeDataComponent("MET_Run2016G_PromptReco_v1" , "/MET/Run2016G-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
MET_Run2016H_PromptReco_v1     =   kreator.makeDataComponent("MET_Run2016H_PromptReco_v1" , "/MET/Run2016H-PromptReco-v1/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016H_PromptReco_v2     =   kreator.makeDataComponent("MET_Run2016H_PromptReco_v2" , "/MET/Run2016H-PromptReco-v2/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016H_PromptReco_v3     =   kreator.makeDataComponent("MET_Run2016H_PromptReco_v3" , "/MET/Run2016H-PromptReco-v3/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016B_PromptReco_v1     =   kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v1" , "/SingleElectron/Run2016B-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016B_PromptReco_v2     =   kreator.makeDataComponent("SingleElectron_Run2016B_PromptReco_v2" , "/SingleElectron/Run2016B-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016C_PromptReco_v2     =   kreator.makeDataComponent("SingleElectron_Run2016C_PromptReco_v2" , "/SingleElectron/Run2016C-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016D_PromptReco_v2     =   kreator.makeDataComponent("SingleElectron_Run2016D_PromptReco_v2" , "/SingleElectron/Run2016D-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016E_PromptReco_v2     =   kreator.makeDataComponent("SingleElectron_Run2016E_PromptReco_v2" , "/SingleElectron/Run2016E-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016F_PromptReco_v1     =   kreator.makeDataComponent("SingleElectron_Run2016F_PromptReco_v1" , "/SingleElectron/Run2016F-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016G_PromptReco_v1     =   kreator.makeDataComponent("SingleElectron_Run2016G_PromptReco_v1" , "/SingleElectron/Run2016G-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleElectron_Run2016H_PromptReco_v1     =   kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v1" , "/SingleElectron/Run2016H-PromptReco-v1/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016H_PromptReco_v2     =   kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v2" , "/SingleElectron/Run2016H-PromptReco-v2/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016H_PromptReco_v3     =   kreator.makeDataComponent("SingleElectron_Run2016H_PromptReco_v3" , "/SingleElectron/Run2016H-PromptReco-v3/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016B_PromptReco_v1     =   kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v1" , "/SingleMuon/Run2016B-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016B_PromptReco_v2     =   kreator.makeDataComponent("SingleMuon_Run2016B_PromptReco_v2" , "/SingleMuon/Run2016B-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016C_PromptReco_v2     =   kreator.makeDataComponent("SingleMuon_Run2016C_PromptReco_v2" , "/SingleMuon/Run2016C-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016D_PromptReco_v2     =   kreator.makeDataComponent("SingleMuon_Run2016D_PromptReco_v2" , "/SingleMuon/Run2016D-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016E_PromptReco_v2     =   kreator.makeDataComponent("SingleMuon_Run2016E_PromptReco_v2" , "/SingleMuon/Run2016E-PromptReco-v2/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016F_PromptReco_v1     =   kreator.makeDataComponent("SingleMuon_Run2016F_PromptReco_v1" , "/SingleMuon/Run2016F-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016G_PromptReco_v1     =   kreator.makeDataComponent("SingleMuon_Run2016G_PromptReco_v1" , "/SingleMuon/Run2016G-PromptReco-v1/MINIAOD" , "CMS", ".*root", prompt_json) 
SingleMuon_Run2016H_PromptReco_v1     =   kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v1" , "/SingleMuon/Run2016H-PromptReco-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016H_PromptReco_v2     =   kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v2" , "/SingleMuon/Run2016H-PromptReco-v2/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016H_PromptReco_v3     =   kreator.makeDataComponent("SingleMuon_Run2016H_PromptReco_v3" , "/SingleMuon/Run2016H-PromptReco-v3/MINIAOD" , "CMS", ".*root", json) 


dataSamples_PromptReco =[
                        JetHT_Run2016B_PromptReco_v1 , JetHT_Run2016B_PromptReco_v2 , JetHT_Run2016C_PromptReco_v2 , JetHT_Run2016D_PromptReco_v2 , JetHT_Run2016E_PromptReco_v2 , JetHT_Run2016F_PromptReco_v1 , JetHT_Run2016G_PromptReco_v1 , JetHT_Run2016H_PromptReco_v1 , JetHT_Run2016H_PromptReco_v2 , JetHT_Run2016H_PromptReco_v3 , 
                        MET_Run2016B_PromptReco_v1 , MET_Run2016B_PromptReco_v2 , MET_Run2016C_PromptReco_v2 , MET_Run2016D_PromptReco_v2 , MET_Run2016E_PromptReco_v2 , MET_Run2016F_PromptReco_v1 , MET_Run2016G_PromptReco_v1 , MET_Run2016H_PromptReco_v1 , MET_Run2016H_PromptReco_v2 , MET_Run2016H_PromptReco_v3 , 
                        SingleElectron_Run2016B_PromptReco_v1 , SingleElectron_Run2016B_PromptReco_v2 , SingleElectron_Run2016C_PromptReco_v2 , SingleElectron_Run2016D_PromptReco_v2 , SingleElectron_Run2016E_PromptReco_v2 , SingleElectron_Run2016F_PromptReco_v1 , SingleElectron_Run2016G_PromptReco_v1 , SingleElectron_Run2016H_PromptReco_v1 , SingleElectron_Run2016H_PromptReco_v2 , SingleElectron_Run2016H_PromptReco_v3 , 
                        SingleMuon_Run2016B_PromptReco_v1 , SingleMuon_Run2016B_PromptReco_v2 , SingleMuon_Run2016C_PromptReco_v2 , SingleMuon_Run2016D_PromptReco_v2 , SingleMuon_Run2016E_PromptReco_v2 , SingleMuon_Run2016F_PromptReco_v1 , SingleMuon_Run2016G_PromptReco_v1 , SingleMuon_Run2016H_PromptReco_v1 , SingleMuon_Run2016H_PromptReco_v2 , SingleMuon_Run2016H_PromptReco_v3 
                ]


JetHT_Run2016B_23Sep2016_v1     =   kreator.makeDataComponent("JetHT_Run2016B_23Sep2016_v1" , "/JetHT/Run2016B-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016B_23Sep2016_v3     =   kreator.makeDataComponent("JetHT_Run2016B_23Sep2016_v3" , "/JetHT/Run2016B-23Sep2016-v3/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016C_23Sep2016_v1     =   kreator.makeDataComponent("JetHT_Run2016C_23Sep2016_v1" , "/JetHT/Run2016C-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016D_23Sep2016_v1     =   kreator.makeDataComponent("JetHT_Run2016D_23Sep2016_v1" , "/JetHT/Run2016D-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016E_23Sep2016_v1     =   kreator.makeDataComponent("JetHT_Run2016E_23Sep2016_v1" , "/JetHT/Run2016E-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016F_23Sep2016_v1     =   kreator.makeDataComponent("JetHT_Run2016F_23Sep2016_v1" , "/JetHT/Run2016F-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
JetHT_Run2016G_23Sep2016_v1     =   kreator.makeDataComponent("JetHT_Run2016G_23Sep2016_v1" , "/JetHT/Run2016G-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016B_23Sep2016_v2     =   kreator.makeDataComponent("MET_Run2016B_23Sep2016_v2" , "/MET/Run2016B-23Sep2016-v2/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016B_23Sep2016_v3     =   kreator.makeDataComponent("MET_Run2016B_23Sep2016_v3" , "/MET/Run2016B-23Sep2016-v3/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016C_23Sep2016_v1     =   kreator.makeDataComponent("MET_Run2016C_23Sep2016_v1" , "/MET/Run2016C-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016D_23Sep2016_v1     =   kreator.makeDataComponent("MET_Run2016D_23Sep2016_v1" , "/MET/Run2016D-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016E_23Sep2016_v1     =   kreator.makeDataComponent("MET_Run2016E_23Sep2016_v1" , "/MET/Run2016E-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016F_23Sep2016_v1     =   kreator.makeDataComponent("MET_Run2016F_23Sep2016_v1" , "/MET/Run2016F-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
MET_Run2016G_23Sep2016_v1     =   kreator.makeDataComponent("MET_Run2016G_23Sep2016_v1" , "/MET/Run2016G-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016B_23Sep2016_v2     =   kreator.makeDataComponent("SingleElectron_Run2016B_23Sep2016_v2" , "/SingleElectron/Run2016B-23Sep2016-v2/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016B_23Sep2016_v3     =   kreator.makeDataComponent("SingleElectron_Run2016B_23Sep2016_v3" , "/SingleElectron/Run2016B-23Sep2016-v3/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016C_23Sep2016_v1     =   kreator.makeDataComponent("SingleElectron_Run2016C_23Sep2016_v1" , "/SingleElectron/Run2016C-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016D_23Sep2016_v1     =   kreator.makeDataComponent("SingleElectron_Run2016D_23Sep2016_v1" , "/SingleElectron/Run2016D-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016E_23Sep2016_v1     =   kreator.makeDataComponent("SingleElectron_Run2016E_23Sep2016_v1" , "/SingleElectron/Run2016E-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016F_23Sep2016_v1     =   kreator.makeDataComponent("SingleElectron_Run2016F_23Sep2016_v1" , "/SingleElectron/Run2016F-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleElectron_Run2016G_23Sep2016_v1     =   kreator.makeDataComponent("SingleElectron_Run2016G_23Sep2016_v1" , "/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016B_23Sep2016_v1     =   kreator.makeDataComponent("SingleMuon_Run2016B_23Sep2016_v1" , "/SingleMuon/Run2016B-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016B_23Sep2016_v3     =   kreator.makeDataComponent("SingleMuon_Run2016B_23Sep2016_v3" , "/SingleMuon/Run2016B-23Sep2016-v3/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016C_23Sep2016_v1     =   kreator.makeDataComponent("SingleMuon_Run2016C_23Sep2016_v1" , "/SingleMuon/Run2016C-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016D_23Sep2016_v1     =   kreator.makeDataComponent("SingleMuon_Run2016D_23Sep2016_v1" , "/SingleMuon/Run2016D-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016E_23Sep2016_v1     =   kreator.makeDataComponent("SingleMuon_Run2016E_23Sep2016_v1" , "/SingleMuon/Run2016E-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016F_23Sep2016_v1     =   kreator.makeDataComponent("SingleMuon_Run2016F_23Sep2016_v1" , "/SingleMuon/Run2016F-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 
SingleMuon_Run2016G_23Sep2016_v1     =   kreator.makeDataComponent("SingleMuon_Run2016G_23Sep2016_v1" , "/SingleMuon/Run2016G-23Sep2016-v1/MINIAOD" , "CMS", ".*root", json) 



dataSamples_ReReco= [
              JetHT_Run2016B_23Sep2016_v1 , JetHT_Run2016B_23Sep2016_v3 , JetHT_Run2016C_23Sep2016_v1 , JetHT_Run2016D_23Sep2016_v1 , JetHT_Run2016E_23Sep2016_v1 , JetHT_Run2016F_23Sep2016_v1 , JetHT_Run2016G_23Sep2016_v1 , 
              MET_Run2016B_23Sep2016_v2 , MET_Run2016B_23Sep2016_v3 , MET_Run2016C_23Sep2016_v1 , MET_Run2016D_23Sep2016_v1 , MET_Run2016E_23Sep2016_v1 , MET_Run2016F_23Sep2016_v1 , MET_Run2016G_23Sep2016_v1 , 
              SingleElectron_Run2016B_23Sep2016_v2 , SingleElectron_Run2016B_23Sep2016_v3 , SingleElectron_Run2016C_23Sep2016_v1 , SingleElectron_Run2016D_23Sep2016_v1 , SingleElectron_Run2016E_23Sep2016_v1 , SingleElectron_Run2016F_23Sep2016_v1 , SingleElectron_Run2016G_23Sep2016_v1 , 
              SingleMuon_Run2016B_23Sep2016_v1 , SingleMuon_Run2016B_23Sep2016_v3 , SingleMuon_Run2016C_23Sep2016_v1 , SingleMuon_Run2016D_23Sep2016_v1 , SingleMuon_Run2016E_23Sep2016_v1 , SingleMuon_Run2016F_23Sep2016_v1 , SingleMuon_Run2016G_23Sep2016_v1 
            ] 
samples = dataSamples_ReReco + dataSamples_PromptReco

### ---------------------------------------------------------------------

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"

for comp in samples:
    comp.splitFactor = 1000
    comp.isMC = False
    comp.isData = True

if __name__ == "__main__":
   import sys
   if "test" in sys.argv:
       from CMGTools.RootTools.samples.ComponentCreator import testSamples
       testSamples(samples)
   if "locality" in sys.argv:
       import re
       from CMGTools.Production.localityChecker import LocalityChecker
       tier2Checker = LocalityChecker("T2_CH_CERN", datasets="/*/*/MINIAOD*")
       for comp in samples:
           if len(comp.files) == 0: 
               print '\033[34mE: Empty component: '+comp.name+'\033[0m'
               continue
           if not hasattr(comp,'dataset'): continue
           if not re.match("/[^/]+/[^/]+/MINIAOD(SIM)?", comp.dataset): continue
           if "/store/" not in comp.files[0]: continue
           if re.search("/store/(group|user|cmst3)/", comp.files[0]): continue
           if not tier2Checker.available(comp.dataset):
               print "\033[1;31mN: Dataset %s (%s) is not available on T2_CH_CERN\033[0m" % (comp.name,comp.dataset)
           else: print "Y: Dataset %s (%s) is available on T2_CH_CERN" % (comp.name,comp.dataset)
   if "refresh" in sys.argv:
        from CMGTools.Production.cacheChecker import CacheChecker
        checker = CacheChecker()
        dataSamples = samples
        if len(sys.argv) > 2: 
            dataSamples = []
            for x in sys.argv[2:]:
                for s in samples:
                    if x in s.name and s not in dataSamples:
                        dataSamples.append(s)
            dataSamples.sort(key = lambda d : d.name)
        for d in dataSamples:
            print "Checking ",d.name," aka ",d.dataset
            checker.checkComp(d, verbose=True)
   if "list" in sys.argv:
        from CMGTools.HToZZ4L.tools.configTools import printSummary
        dataSamples = samples
        if len(sys.argv) > 2:
            dataSamples = []
            for x in sys.argv[2:]:
                for s in samples:
                    if x in s.name and s not in dataSamples:
                        dataSamples.append(s)
            dataSamples.sort(key = lambda d : d.name)
        printSummary(dataSamples)
