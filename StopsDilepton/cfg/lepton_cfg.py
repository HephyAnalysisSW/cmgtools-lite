##########################################################
##      SUSY CONFIGURATION FOR LEPTON ID STUDIES        ##
## makes trees with one entry per lepton, not per event ##
##########################################################

import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
#from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 
from CMGTools.StopsDilepton.AutoFillVectorTreeProducer  import * 
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *
# General
import os

# Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

### Tree Producer
#from CMGTools.TTHAnalysis.analyzers.ttHLepStudyTreeProducer import ttHLepStudyTreeProducer
#treeProducer = cfg.Analyzer(
#    ttHLepStudyTreeProducer,
#    vectorTree = True,
#    PDFWeights = [],
#    triggerBits = {},
#    )

treeProducer = cfg.Analyzer(
     AutoFillVectorTreeProducer, name='treeProducer',
     vectorTree = False,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     globalVariables = [ ], # rho, nvertices, njets
     globalObjects = [], 
     collection = ( "selectedLeptons" , NTupleCollection("lep", leptonTypeSusy, 10, help="leptons after the preselection") ),
     vector_collection = ( "pfCands" , NTupleCollection("pfCand", particleType, 100, help="pf candidates associated") ),
     defaultFloatType = 'F',
)


# add lepton classes
leptonTypeSusy.variables.append( NTupleVariable("isPromptId", lambda x: abs(getattr(x, 'mcMatchId', -99)) in [6,23,24,25,37], int, help="isPrompt for leptons after the preselection for MVA training"))
leptonTypeSusy.variables.append( NTupleVariable("isNonPromptId", lambda x: not (abs(getattr(x, 'mcMatchId', -99)) in [6,23,24,25,37]) and (abs(getattr(x,'mcMatchAny',-99)) in [4,5]), int,  help="isNonPrompt for leptons after the preselection for MVA training"))
leptonTypeSusy.variables.append( NTupleVariable("isFakeId", lambda x: not (abs(getattr(x, 'mcMatchId', -99)) in [6,23,24,25,37]) and not (abs(getattr(x,'mcMatchAny',-99)) in [4,5]), int,  help="isFake for leptons after the preselection for MVA training"))

#add INT-Type lepton variables as FLOAT (is default)
leptonTypeSusy.variables.append( NTupleVariable("convVeto_float", lambda x : x.passConversionVeto() if abs(x.pdgId())==11 else 1, help="Conversion veto (always true for muons)"))
leptonTypeSusy.variables.append( NTupleVariable("lostHits_float", lambda x : (x.gsfTrack() if abs(x.pdgId())==11 else x.innerTrack()).hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS), help="Number of lost hits on inner track"))


# Lepton settings
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.rhoMuon          = 'fixedGridRhoFastjetAll'
lepAna.rhoElectron      = 'fixedGridRhoFastjetAll'

# Electrons
lepAna.loose_electron_pt  = 5
lepAna.doMiniIsolation = True

lepAna.loose_electron_id  = ""
lepAna.loose_electron_lostHits = 999. # no cut
lepAna.loose_electron_dxy    = 999.
lepAna.loose_electron_dz     = 999.

lepAna.inclusive_electron_id  = ""
lepAna.inclusive_electron_lostHits = 999.  # no cut
lepAna.inclusive_electron_dxy    = 999. # no cut since embedded in ID
lepAna.inclusive_electron_dz     = 999. # no cut since embedded in ID

# Muons
# store everything
lepAna.loose_muon_pt  = 5
lepAna.inclusive_muon_dxy = 999.
lepAna.inclusive_muon_dz  = 999.
lepAna.inclusive_muon_eta = 999.
lepAna.inclusive_muon_id = None#   POG_ID_Loose
lepAna.inclusive_muon_pt = 0.

# rho area for both lepton flavors
lepAna.ele_isoCorr = "rhoArea"
lepAna.mu_isoCorr  = "rhoArea"
lepAna.mu_effectiveAreas = 'Spring15_25ns_v1'
lepAna.ele_effectiveAreas = 'Spring15_25ns_v1'

# Loose selection 
lepAna.loose_electron_relIso = 0.5
lepAna.loose_muon_relIso     = 0.5
lepAna.match_inclusiveLeptons=True
lepAna.pfCandAssocDR         = 0.5
#-------- SEQUENCE

sequence = cfg.Sequence([
    skimAnalyzer,
    #eventSelector,
    jsonAna,
    pileUpAna,
    genAna,
    vertexAna,
    lepAna,
    jetAna,
    treeProducer,
    ])

selectedComponents = [
        ]

leptonTypeSusy.variables.append(  NTupleVariable("isElectron",lambda lepton : abs(lepton.pdgId())==11, help="isElectron") )
leptonTypeSusy.variables.append(  NTupleVariable("isMuon",lambda lepton : abs(lepton.pdgId())==13, help="isMuon") )

if getHeppyOption("loadSamples"):

    from CMGTools.RootTools.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
    from CMGTools.RootTools.samples.samples_13TeV_DATA2016 import *
    from CMGTools.RootTools.samples.samples_13TeV_signals import *
    from CMGTools.StopsDilepton.TTbarDMJets_signals_RunIISummer16MiniAODv2 import *
    from CMGTools.StopsDilepton.ttX0j_5f_MLM_signals_RunIISummer16MiniAODv2 import *
    #from CMGTools.StopsDilepton.samples import *

    for sample in dataSamples:
        sample.json="$CMSSW_BASE/src/CMGTools/TTHAnalysis/data/json/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"

    # sync mc
    TTJets_SingleLeptonFromTbar.files=["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00A25ADE-DFD4-E611-8EAC-0025905A48B2.root"]
    #TTJets_SingleLeptonFromTbar.files=["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/00D6E4E7-EFD4-E611-9C59-549F3525A184.root"]
    #TTJets_SingleLeptonFromTbar.files=["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/TTJets_SingleLeptFromTbar_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/020F0317-AED4-E611-ACCA-002590DE3A92.root"]
    selectedComponents = [TTJets_SingleLeptonFromTbar]
    
    #QCD_Pt120to170.files=["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/QCD_Pt-120to170_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/020CF991-90B1-E611-ADFB-0017A4770C28.root"]
    #selectedComponents = [QCD_Pt120to170]
    ## sync data
    #MuonEG_Run2016F_03Feb2017.files=["root://cms-xrd-global.cern.ch//store/data/Run2016F/MuonEG/MINIAOD/03Feb2017-v1/50000/0496325A-05EB-E611-953B-0025905A60DE.root"]
    #selectedComponents += [MuonEG_Run2016F_03Feb2017]

    #selectedComponents = [ttZ0j_ll]
    #selectedComponents = [WZTo3LNu]
    for comp in selectedComponents:
        comp.files = comp.files[:1]
        comp.splitFactor = 1

from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
event_class = Events
if getHeppyOption("fetch"):
  event_class = EOSEventsWithDownload

config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     preprocessor=None, 
                     events_class = event_class)

