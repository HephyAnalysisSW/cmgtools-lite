import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

###############################
####### Parameters ############
###############################
#options = VarParsing ('python')
#
#options.register('reportEvery', 1000,
#    VarParsing.multiplicity.singleton,
#    VarParsing.varType.int,
#    "Report every N events (default is N=10)"
#)
#options.register('wantSummary', False,
#    VarParsing.multiplicity.singleton,
#    VarParsing.varType.bool,
#    "Print out trigger and timing summary"
#)
#
### 'maxEvents' is already registered by the Framework, changing default value
#options.setDefault('maxEvents', 100)
#
#options.parseArguments()

process = cms.Process("RERUN")

process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000#options.reportEvery

### Events to process
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

## Input files
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v1/50000/3E1DE3B8-87C0-E611-8733-00145EDD74ED.root'
    )
)

### Output file
#process.TFileService = cms.Service("TFileService",
#   fileName = cms.string(options.outputFilename)
#)

## Options and Output Report
process.options   = cms.untracked.PSet(
#    wantSummary = cms.untracked.bool(options.wantSummary),
    wantSummary = cms.untracked.bool(True),
    allowUnscheduled = cms.untracked.bool(True)
)

#################################################
## Update PAT jets
#################################################

from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
updateJetCollection(
  process,
  jetSource = cms.InputTag('slimmedJets'),
  #labelName = 'selectedUpdated',
  jetCorrections = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None'),
  # DeepCSV twiki: https://twiki.cern.ch/twiki/bin/view/CMS/DeepFlavour
  btagDiscriminators = [
    'pfCombinedSecondaryVertexV2BJetTags',
    'pfDeepCSVJetTags:probudsg',
    'pfDeepCSVJetTags:probb',
    'pfDeepCSVJetTags:probc',
    'pfDeepCSVJetTags:probbb',
   #'pfDeepCSVJetTags:probcc', # not available in CMSSW_9_X_Y, also not really needed for us
  ]
 )

from PhysicsTools.PatAlgos.tools.helpers import getPatAlgosToolsTask
#process.jetSequence=getPatAlgosToolsTask(process)    
process.p = cms.Path(getPatAlgosToolsTask(process))        

process.MINIAODSIMoutput = cms.OutputModule("PoolOutputModule",                     
    compressionAlgorithm = cms.untracked.string('LZMA'),    
    compressionLevel = cms.untracked.int32(4),              
    dataset = cms.untracked.PSet(   
        dataTier = cms.untracked.string(''),                
        filterName = cms.untracked.string('')               
    ),      
    dropMetaData = cms.untracked.string('ALL'),             
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),                   
    fastCloning = cms.untracked.bool(False),                
    fileName = cms.untracked.string('BTagging.root'),  
    outputCommands = cms.untracked.vstring('keep *',
                                           #'drop *_deepNNTagInfos*_*_*',
                                           'drop *',
                                           'keep *_selectedUpdatedPatJets*_*_*',
                                           ),
    overrideInputFileSplitLevels = cms.untracked.bool(True) 
)           

process.endpath = cms.EndPath(process.MINIAODSIMoutput)                                                                                                                                                     
