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

#
# Lepton collection:
#



########################
###### ANALYZERS #######
########################

from CMGTools.SUSYAnalysis.analyzers.GenStudies.GenJetMETAnalyzer import GenJetMETAnalyzer

genJetMETAna = cfg.Analyzer(
    GenJetMETAnalyzer,
    name = "GenJetMETAna",
    copyJetsByValue = False,      #Whether or not to copy the input jets or to work with references (should be 'True' if JetAnalyzer is run more than once)
    genJetCol = "ak4GenJetsNoNu",
    collectionPostFix = "",
    )


from CMGTools.SUSYAnalysis.analyzers.GenStudies.GeneratorAnalyzer import GeneratorAnalyzer
genAna = cfg.Analyzer(
    GeneratorAnalyzer, name="GeneratorAnalyzer",
    stableBSMParticleIds = [ 1000022 ],
    savePreFSRParticleIds = [ 1,2,3,4,5, 11,12,13,14,15,16, 21,22 ],
    makeAllGenParticles  = True,
    makeSplittedGenLists = True,
    allGenTaus = False,
    verbose = False,
    )


#from CMGTools.SUSYAnalysis.analyzers.GenStudies.ttHGenLevelOnlyStudy import ttHGenLevelOnlyStudy
#
#genLevelOnlyStudyAna = cfg.Analyzer(
#    ttHGenLevelOnlyStudy, name="GenLevelOnlyStudy",
#    )



genSequence = [
    lheWeightAna,
    #genLevelOnlyStudyAna,
    genAna,
    genJetMETAna,
]


###
###   Create Sample Components
### 
  
from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

DegStop300_270 = kreator.makeMCComponentFromLocal( "DegStop300_270", dataset="", path="/afs/hephy.at/user/m/mwinder/public/GEN_ROOT/" , xSec = 1)

selectedComponents = [ DegStop300_270 ]



###
###   NTupleTypes and Collections and Global Variables
### 
from PhysicsTools.Heppy.analyzers.core.autovars import NTupleObjectType  
from CMGTools.SUSYAnalysis.analyzers.treeProducerSusyDegStop import *
from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import *





globalVariables = [
        NTupleVariable("GenMET_pt",  lambda ev : ev.genMET.pt() , mcOnly=True, help="Gen MET"),
        NTupleVariable("GenMET_phi", lambda ev : ev.genMET.phi(), mcOnly=True, help="Gen MET phi"),
]

globalObjects = [ 

                ]



genParticleForGenStudies = NTupleObjectType("genParticleForGenStudies", baseObjectTypes = [ genParticleWithMotherIndex ], mcOnly=True, variables = [
    NTupleVariable("bGenMatched",            lambda x : getattr( x , "bHadronMatched" ,-999) , help="matched to a GenJet"),
    #NTupleVariable("bQuarkMatched" , lambda x : getattr( x , "bQuarkMatched"  ,-999) , help="matched to a b-quark"),
])

genJetTypeForGenStudies = NTupleObjectType("genJetTypeForGenStudies",  baseObjectTypes = [ genJetType ], mcOnly=True, variables = [
    NTupleVariable("bMatched",            lambda x : getattr( x , "bHadronMatched" ,-999) , help="matched to a b-hadron"),
    NTupleVariable("bMatchedMinDr",       lambda x : getattr( x , "bHadronMatched_minDr" ,-999) , help="matched to a b-hadron, smalled Dr"),
    NTupleVariable("bMatchedMinDrIndex",  lambda x : getattr( x , "bHadronMatched_minDrIndex" ,-999) , help="matched to a b-hadron, index of the best matched genparticle"),
])


collections = {
            "genParticles"     : NTupleCollection("GenPartAll", genParticleForGenStudies , 10000 , help="All scattering particles, with ancestry and links"),
            "generatorSummary" : NTupleCollection("GenPart", genParticleForGenStudies , 100 , help="Hard scattering particles, with ancestry and links"),
            "genJets"          : NTupleCollection("GenJet",  genJetTypeForGenStudies,  100, help="Gen Jets before cleaning, sorted by pt")
}





## 
##   Tree Producer
## 

## 

treeProducer = cfg.Analyzer(
  AutoFillTreeProducer, name='treeProducerSusySingleLepton',
  vectorTree = True,
  saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
  defaultFloatType = 'F', # use Float_t for floating point
  PDFWeights = {},
  globalVariables = globalVariables,
  globalObjects   = globalObjects,
  collections     = collections,
  )




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
    option='recreate'
    )
outputService.append(output_service)


### GEN


sequence = cfg.Sequence( genSequence +[treeProducer] )

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
         sequence = sequence,
         services = outputService,
         events_class = Events)

