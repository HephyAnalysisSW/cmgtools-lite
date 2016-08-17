##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption


#JSON
jsonAna.useLumiBlocks = True

####### Leptons  #####
# lep collection
lepAna.packedCandidates = 'packedPFCandidates'



#
# Electrons:
#

lepAna.loose_electron_eta = 2.5
lepAna.inclusive_electron_pt  = 5
lepAna.loose_electron_pt  = 5
lepAna.inclusive_electron_id  = "" # same as in susyCore
lepAna.loose_electron_id = "POG_MVA_ID_Spring15_NonTrig_VLoose" # Spring15 25ns era

#
# Muons
#

lepAna.inclusive_muon_id  = ""
lepAna.inclusive_muon_pt  = 3 
lepAna.loose_muon_pt      = 3 

# Isolation

absIsoCut   = 5
ptSwitch    = 25
relIsoCut   = 1.*absIsoCut/ptSwitch

lepAna.doMiniIsolation = False
lepAna.ele_isoCorr = "rhoArea"
lepAna.mu_isoCorr = "rhoArea"
lepAna.loose_muon_isoCut     =  lambda mu: (   mu.absIso03 < absIsoCut  ) or ( mu.relIso03 <  relIsoCut ) 
lepAna.loose_electron_isoCut =  lambda el: (   el.absIso03 < absIsoCut ) or ( el.relIso03  <  relIsoCut )  

###

#lepAna.inclusive_electron_dxy = 2.5
#lepAna.inclusive_electron_dz  = 2.5
#lepAna.inclusive_muon_dxy    = 2.5
#lepAna.inclusive_muon_dz     = 2.5


lepAna.loose_electron_dxy     = 0.02
lepAna.loose_electron_dz      = 0.5
lepAna.loose_muon_dxy         = 0.02
lepAna.loose_muon_dz          = 0.5



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

#jetAna.jetPt = 20
#jetAna.jetEta = 2.4


#jetAna.calculateType1METCorrection = True
## MET (can be used for MiniAODv2)
metAna.recalibrate = True

## Iso Track
isoTrackAna.setOff=False

# store all taus by default
genAna.allGenTaus = True




selectedComponents = []
if getHeppyOption("loadSamples") :
#if getHeppyOption("loadSamples") or True:

  test = 1 

  #sample = 'data'
  sample = 'MC'
  #sample = 'Signal'

  if sample == "MC":
    from CMGTools.RootTools.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
    selectedComponents = [ ZJetsToNuNu_HT800to1200 ] #TTs + SingleTop #TTJets_SingleLepton
    print 'Going to process MC'
    isData = False
    isSignal = False
  
  elif sample == "Signal":
    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    #selectedComponents = [T1tttt_mGo_1475to1500_mLSP_1to1250, T1tttt_mGo_1200_mLSP_1to825 ]
    selectedComponents = [ SMS_T2tt_dM_10to80_2Lfilter , ]
    selectedComponents = [ SMS_T2tt_dM_10to80_genHT_160_genMET_80 ]
    #susyCounter.SMS_varying_masses = ['genSusyMGluino','genSusyMNeutralino']
    print 'Going to process Signal'
    isData = False
    isSignal = True
    #jetAna.mcGT = "FastSim_Summer15_25nsV6_MC"


  elif sample == "data":
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *

    #selectedComponents = [ MET_Run2016B_PromptReco_v2 , SingleElectron_Run2016B_PromptReco_v2, SingleMuon_Run2016B_PromptReco_v2]
    selectedComponents = [ SingleMuon_Run2016D_PromptReco_v2,  SingleElectron_Run2016D_PromptReco_v2]
    #selectedComponents = [  MET_Run2016D_PromptReco_v2 ]
    print 'Going to process DATA'
    isData = True
    isSignal = False
    if test!=0 and jsonAna in susyCoreSequence: susyCoreSequence.remove(jsonAna)
  
  
    # Benchmarks
  
    if test==1:
      comp = selectedComponents[0]
      selectedComponents = selectedComponents[:1]
      comp.files = comp.files[:1]
      comp.fineSplitFactor = 1
      comp.splitFactor = 1
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
  
  


  #if isData:# or isSignal :
  #  pass
  #if isSignal:
  #  sequence.remove(eventFlagsAna)
  #  sequence.remove(hbheFilterAna)




## PDF weights
PDFWeights = []
#PDFWeights = [ ("CT10",53), ("MSTW2008lo68cl",41), ("NNPDF21_100",101) ]
#PDFWeights = [ ("CT10nlo",53),("MSTW2008nlo68cl",41),("NNPDF30LO",101),("NNPDF30_nlo_nf_5_pdfas",103), ("NNPDF30_lo_as_0130",101)]
#PDFWeights = [ ("NNPDF30_lo_as_0130",101) ]
# see for TTJets  https://github.com/cms-sw/genproductions/blob/c41ab29f3d86c9e53df8b0d76c12cd519adbf013/bin/MadGraph5_aMCatNLO/cards/production/13TeV/tt0123j_5f_ckm_LO_MLM/tt0123j_5f_ckm_LO_MLM_run_card.dat#L52
# and then https://lhapdf.hepforge.org/pdfsets.html

#--------- Tree Producer
from CMGTools.TTHAnalysis.analyzers.treeProducerSusySingleLepton import *
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


isSignal=False
if isSignal:
  ## SUSY Counter
  ## histo counter
  #susyCoreSequence.insert(susyCoreSequence.index(skimAnalyzer),
  susyCoreSequence.insert(susyCoreSequence.index(susyScanAna)+1,
        susyCounter)
  #susyCoreSequence.append(susyCounter)


  jetAna.applyL2L3Residual = False
  jetAna.calculateType1METCorrection = True
  jetAna.doQG = False
  jetAna.mcGT = "Spring16_FastSimV1_MC"
  jetAna.relaxJetId = True  # relax jetId for FastSIM


  # change scn mass parameters
  susyCounter.SUSYmodel = 'T2tt_dM_10to80_genHT_160_genMET_80'
  susyCounter.SMS_mass_1 = "genSusyMStop"
  susyCounter.SMS_mass_2 = "genSusyMNeutralino"
  susyCounter.SMS_varying_masses = ['genSusyMStop','genSusyMNeutralino']



print "Selected Components: "
for comp in selectedComponents:
  print comp.name


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

