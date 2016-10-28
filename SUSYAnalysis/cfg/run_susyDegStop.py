##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption




#absIsoCut   = 5
#ptSwitch    = 25
#relIsoCut   = 1.*absIsoCut/ptSwitch
absIsoCut   = 20
ptSwitch    = 25
relIsoCut   = 1.*absIsoCut/ptSwitch




#JSON
jsonAna.useLumiBlocks = True





####### Leptons  #####
# lep collection
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.match_inclusiveLeptons = True # match to all inclusive leptons
lepAna.match_inclusiveLeptons = True

#
# Electrons:
#


lepAna.loose_electron_eta      = 2.5
lepAna.inclusive_electron_pt   = 3
lepAna.loose_electron_pt       = 3
lepAna.inclusive_electron_id   = "" # same as in susyCore
lepAna.loose_electron_id       = "POG_MVA_ID_Spring15_NonTrig_VLoose" # Spring15 25ns era

lepAna.loose_electron_lostHits = 0.0
lepAna.loose_electron_lostHits = 0.0


#
# Muons
#

lepAna.inclusive_muon_id  = ""
lepAna.inclusive_muon_pt  = 3 
lepAna.loose_muon_pt      = 3 

###

#
# IP:
#

#LepOther
lepAna.loose_electron_dxy     = 0.5
lepAna.loose_electron_dz      = 1.0
lepAna.loose_muon_dxy         = 0.5
lepAna.loose_muon_dz          = 1.0

#LepGood
lepAna.loose_electron_dxy     = 0.2
lepAna.loose_electron_dz      = 0.5
lepAna.loose_muon_dxy         = 0.2
lepAna.loose_muon_dz          = 0.5

# Isolation


lepAna.doMiniIsolation       =  False
lepAna.ele_isoCorr           =  "rhoArea"
lepAna.mu_isoCorr            =  "rhoArea"
lepAna.loose_muon_isoCut     =  lambda mu: (   mu.absIso03 < absIsoCut )  or ( mu.relIso03  <  relIsoCut ) 
lepAna.loose_electron_isoCut =  lambda el: (   el.absIso03 < absIsoCut )  or ( el.relIso03  <  relIsoCut )  



########################
###### ANALYZERS #######
########################

#add LHE ana for HT info
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer
LHEAna = LHEAnalyzer.defaultConfig

from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
  ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
  minJets25 = 0,
  )

## Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
      ttHFatJetAna)

#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
#     ttHSVAna)


#from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import * # central trigger list
from CMGTools.RootTools.samples.triggers_13TeV_Spring15_degStop import *

#-------- TRIGGERS -----------
triggerFlagsAna.triggerBits = {}



for trigger in  triggers:
  trigger_name = "trigger_{trig}".format(trig=trigger.replace("_v*","") )
  HLT_name = "{trig}".format(trig=trigger.replace("_v*","").replace("HLT_","") )
  triggerFlagsAna.triggerBits[HLT_name] = eval( trigger_name )





#      {                                                
#      ## MET PD
#      "CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72"           : triggers_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight_BTagCSV0p72           , 
#      "CaloMHTNoPU90_PFMET90_PFMHT90_IDTight"                       : triggers_HLT_CaloMHTNoPU90_PFMET90_PFMHT90_IDTight                       , 
#      "MET200"                                                      : triggers_HLT_MET200                                                      , 
#      "MET250"                                                      : triggers_HLT_MET250                                                      , 
#      "MET300"                                                      : triggers_HLT_MET300                                                      , 
#      "MET60_IsoTrk35_Loose"                                        : triggers_HLT_MET60_IsoTrk35_Loose                                        ,               
#      "MET75_IsoTrk50"                                              : triggers_HLT_MET75_IsoTrk50                                              ,         
#      "MET90_IsoTrk50"                                              : triggers_HLT_MET90_IsoTrk50                                              ,         
#      "MonoCentralPFJet80_PFMETNoMu120_PFMH_PFMHTNoMu120_IDTight"   : triggers_HLT_MonoCentralPFJet80_PFMETNoMu120_PFMH_PFMHTNoMu120_IDTight   ,                                                    
#      "MonoCentralPFJet80_PFMETNoMu90_PFMHT_PFMHTNoMu90_IDTight"    : triggers_HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHT_PFMHTNoMu90_IDTight    ,                                                   
#      "MonoCentralPFJet80_PFMETNoMu120_PFMH_PFMHTNoMu120_IDLoose"   : triggers_HLT_MonoCentralPFJet80_PFMETNoMu120_PFMH_PFMHTNoMu120_IDLoose   ,                                                    
#      "MonoCentralPFJet80_PFMETNoMu90_PFMHT_PFMHTNoMu90_IDLoose"    : triggers_HLT_MonoCentralPFJet80_PFMETNoMu90_PFMHT_PFMHTNoMu90_IDLoose    ,                                                   
#      "Mu14er_PFMET100"                                             : triggers_HLT_Mu14er_PFMET100                                             ,          
#      "Mu3er_PFHT140_PFMET125"                                      : triggers_HLT_Mu3er_PFHT140_PFMET125                                      ,                 
#      "Mu6_PFHT200_PFMET100"                                        : triggers_HLT_Mu6_PFHT200_PFMET100                                        ,               
#      "Mu6_PFHT200_PFMET80_BTagCSV0p72"                             : triggers_HLT_Mu6_PFHT200_PFMET80_BTagCSV0p72                             ,                          
#      "PFMET100_PFMHT100_IDTight"                                   : triggers_HLT_PFMET100_PFMHT100_IDTight                                   ,                    
#      "PFMET100_PFMHT100_IDLoose"                                   : triggers_HLT_PFMET100_PFMHT100_IDLoose                                   ,                    
#      "PFMET110_PFMHT110_IDTight"                                   : triggers_HLT_PFMET110_PFMHT110_IDTight                                   ,                    
#      "PFMET110_PFMHT110_IDLoose"                                   : triggers_HLT_PFMET110_PFMHT110_IDLoose                                   ,                    
#      "PFMET120_BTagCSV0p72"                                        : triggers_HLT_PFMET120_BTagCSV0p72                                        ,               
#      "PFMET120_Mu5"                                                : triggers_HLT_PFMET120_Mu5                                                ,       
#      "PFMET120_PFMHT120_IDTight"                                   : triggers_HLT_PFMET120_PFMHT120_IDTight                                   ,                    
#      "PFMET120_PFMHT120_IDLoose"                                   : triggers_HLT_PFMET120_PFMHT120_IDLoose                                   ,                    
#      "PFMET170_HBHECleaned"                                        : triggers_HLT_PFMET170_HBHECleaned                                        ,               
#      "PFMET170_JetIdCleaned"                                       : triggers_HLT_PFMET170_JetIdCleaned                                       ,                
#      "PFMET170_NoiseCleaned"                                       : triggers_HLT_PFMET170_NoiseCleaned                                       ,                
#      "PFMET170"                                                    : triggers_HLT_PFMET170                                                    ,   
#      "PFMET300"                                                    : triggers_HLT_PFMET300                                                    ,   
#      "PFMET400"                                                    : triggers_HLT_PFMET400                                                    ,   
#      "PFMET90_PFMHT90_IDTight"                                     : triggers_HLT_PFMET90_PFMHT90_IDTight                                     ,                  
#      "PFMET90_PFMHT90_IDLoose"                                     : triggers_HLT_PFMET90_PFMHT90_IDLoose                                     ,                  
#      "PFMETNoMu120_PFMHTNoMu120_IDTight"                           : triggers_HLT_PFMETNoMu120_PFMHTNoMu120_IDTight                           ,                            
#      "PFMETNoMu90_PFMHTNoMu90_IDTight"                             : triggers_HLT_PFMETNoMu90_PFMHTNoMu90_IDTight                             ,                          
#      "PFMETNoMu120_PFMHTNoMu120_IDLoose"                           : triggers_HLT_PFMETNoMu120_PFMHTNoMu120_IDLoose                           ,                            
#      "PFMETNoMu90_PFMHTNoMu90_IDLoose"                             : triggers_HLT_PFMETNoMu90_PFMHTNoMu90_IDLoose                             ,                          
#     
#      ## SingleMuon PD 
#      "IsoMu17_eta2p1"                                              : triggers_HLT_IsoMu17_eta2p1                                              ,               
#      "IsoMu18"                                                     : triggers_HLT_IsoMu18                                                     ,        
#      "IsoMu20"                                                     : triggers_HLT_IsoMu20                                                     ,        
#      "IsoMu22"                                                     : triggers_HLT_IsoMu22                                                     ,        
#      "IsoMu27"                                                     : triggers_HLT_IsoMu27                                                     ,        
#      "IsoTkMu18"                                                   : triggers_HLT_IsoTkMu18                                                   ,          
#      "IsoTkMu20"                                                   : triggers_HLT_IsoTkMu20                                                   ,          
#      "IsoTkMu22"                                                   : triggers_HLT_IsoTkMu22                                                   ,          
#      "IsoTkMu27"                                                   : triggers_HLT_IsoTkMu27                                                   ,          
#      "L1SingleMu16"                                                : triggers_HLT_L1SingleMu16                                                ,             
#      "L1SingleMuOpen"                                              : triggers_HLT_L1SingleMuOpen                                              ,               
#      "L2Mu10"                                                      : triggers_HLT_L2Mu10                                                      ,       
#      "Mu20"                                                        : triggers_HLT_Mu20                                                        ,        
#      "Mu24_eta2p1"                                                 : triggers_HLT_Mu24_eta2p1                                                 ,            
#      "Mu27"                                                        : triggers_HLT_Mu27                                                        ,        
#      "Mu45_eta2p1"                                                 : triggers_HLT_Mu45_eta2p1                                                 ,            
#      "Mu50"                                                        : triggers_HLT_Mu50                                                        ,          
#      "Mu55"                                                        : triggers_HLT_Mu55                                                        ,        
#      "TkMu20"                                                      : triggers_HLT_TkMu20                                                      ,              
#      "TkMu24_eta2p1"                                               : triggers_HLT_TkMu24_eta2p1                                               ,              
#      "TkMu27"                                                      : triggers_HLT_TkMu27                                                      ,       
#
#      }




# --- JET-LEPTON CLEANING ---
#jetAna.cleanSelectedLeptons = True
jetAna.minLepPt = 5 #10

## JEC
#jetAna.mcGT   = "Spring16_25nsV3_MC"
#jetAna.dataGT = "Spring16_25nsV3_DATA"
jetAna.mcGT   = "Spring16_25nsV6_MC"
jetAna.dataGT = "Spring16_25nsV6_DATA"
jetAna.calculateType1METCorrection = False


# add also JEC up/down shifts corrections
jetAna.addJECShifts       = True
jetAna.addJERShifts       = True
jetAna.doQG               = True
jetAna.smearJets          = True #should be false in susycore, already
jetAna.recalibrateJets    = True # false for miniAOD v2!
jetAna.applyL2L3Residual  = True

jetAna.jetPt = 20
#jetAna.jetEta = 2.4


#jetAna.calculateType1METCorrection = True
## MET (can be used for MiniAODv2)
metAna.recalibrate = True

## Iso Track
isoTrackAna.setOff=False

# store all taus by default
genAna.allGenTaus = True



##
## Read LHE weights
pdfwAna.doLHEWeights = True


selectedComponents = []
if getHeppyOption("loadSamples") :

  test = 1 
  sample = 'MC'
  if sample == "MC":
    from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
    #selectedComponents = [ ZJetsToNuNu_HT800to1200 ] #TTs + SingleTop #TTJets_SingleLepton
    #selectedComponents = [  TTJets_FastSIM ] 
    selectedComponents = [  TTJets_LO      ]

    print 'Going to process MC'
    isData = False
    isSignal = False
  
  elif sample == "Signal":
    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    #selectedComponents = [SMS_T5qqqqVV_TuneCUETP8M1]
    selectedComponents = [SMS_T1tttt_mGluino1500_mLSP100]


    from CMGTools.RootTools.samples.samples_13TeV_80X_susySignalsPriv import *
    #selectedComponents = [ T2tt_dM_30to80_genHT_160_genMET_80 ]
    #selectedComponents = [ T2tt_dM_30to80_genHT_160_genMET_80 , T2tt_dM_30to80 ] 
    #selectedComponents = [ SMS_T2tt_dM_10to80_genHT_160_genMET_80 ]
    #susyCounter.SMS_varying_masses = ['genSusyMGluino','genSusyMNeutralino']
    print  'Going to process Signal'
    isData   = False
    isSignal = True

  elif sample == "data":
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *

    selectedComponents = [ SingleMuon_Run2016D_PromptReco_v2,  SingleElectron_Run2016D_PromptReco_v2]
    print 'Going to process DATA'
    isData = True
    isSignal = False
  if test!=0 and jsonAna in susyCoreSequence: susyCoreSequence.remove(jsonAna)
  
  # Benchmarks
  if test==1:
    selectedComponents = selectedComponents[:1]

    for comp in selectedComponents:
      comp.files = comp.files[:1]
  elif test==2:
    for comp in selectedComponents:
      comp.splitFactor = 1
      comp.fineSplitFactor = 1
      comp.files = comp.files[:1]
  elif test==3:
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  elif test==0:
    for comp in selectedComponents:
      comp.fineSplitFactor = 1
      comp.splitFactor = len(comp.files)
  
  


PDFWeights = []

#--------- Tree Producer
#from CMGTools.TTHAnalysis.analyzers.treeProducerSusySingleLepton import *
from CMGTools.SUSYAnalysis.analyzers.treeProducerSusyDegStop import *
treeProducer = cfg.Analyzer(
  AutoFillTreeProducer, name='treeProducerSusySingleLepton',
  vectorTree = True,
  saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
  defaultFloatType = 'F', # use Float_t for floating point
  PDFWeights = PDFWeights,
  globalVariables = susySingleLepton_globalVariables,
  globalObjects = susySingleLepton_globalObjects,
  collections = susySingleLepton_collections,
  )

## Recompute HBHE filters
# HBHE filter analyzer
from CMGTools.TTHAnalysis.analyzers.hbheAnalyzer import hbheAnalyzer
hbheFilterAna = cfg.Analyzer(
    hbheAnalyzer, name = 'hbheAnalyzer',IgnoreTS4TS5ifJetInLowBVRegion=False
)

#from CMGTools.SUSYAnalysis.analyzers.badChargedHadronAnalyzer import badChargedHadronAnalyzer
#badChargedHadronAna = cfg.Analyzer(
#    badChargedHadronAnalyzer, name = 'badChargedHadronAna',
#    muons='slimmedMuons',
#    packedCandidates = 'packedPFCandidates',
#)
#
#from CMGTools.SUSYAnalysis.analyzers.badMuonAnalyzer import badMuonAnalyzer
#badMuonAna = cfg.Analyzer(
#    badMuonAnalyzer, name = 'badMuonAna',
#    muons='slimmedMuons',
#    packedCandidates = 'packedPFCandidates',
#)
#





sequence = cfg.Sequence(susyCoreSequence+[
    LHEAna,
    ttHEventAna,
    hbheFilterAna,
    treeProducer,
#   susyCounter
    ])

isFastSIM=False
isSignal=False
if isSignal:
  isFastSIM = True
  ## SUSY Counter
  ## histo counter
  #susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
  susyCoreSequence.insert(susyCoreSequence.index(susyScanAna)+1,
        susyCounter)
  #susyCoreSequence.append(susyCounter)




  # change scn mass parameters
  susyCounter.SUSYmodel = 'T2tt_dM_10to80_genHT_160_genMET_80'
  susyCounter.SMS_mass_1 = "genSusyMStop"
  susyCounter.SMS_mass_2 = "genSusyMNeutralino"
  susyCounter.SMS_varying_masses = ['genSusyMStop','genSusyMNeutralino']

if isFastSIM:
  jetAna.applyL2L3Residual = False
  jetAna.calculateType1METCorrection = True
  jetAna.doQG = False
  jetAna.mcGT = "Spring16_FastSimV1_MC"
  jetAna.relaxJetId = True  # relax jetId for FastSIM
   

print "Selected Components: "
for comp in selectedComponents:
  print "   ", comp.name , "nFiles:", len(comp.files)


## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='treeProducerSusySingleLepton/tree.root',
    #fname='susyCounter/counts.root',
    option='recreate'
    )
outputService.append(output_service)


from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
         sequence = sequence,
         services = outputService,
         events_class = Events)

