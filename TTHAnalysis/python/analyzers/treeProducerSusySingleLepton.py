from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

def p(x):
  print(x)
  return True
susySingleLepton_globalVariables = susyCore_globalVariables + [

            NTupleVariable("LHEweight_original", lambda ev: ev.LHE_originalWeight if  hasattr(ev,'LHE_originalWeight') else 0, mcOnly=True, help="original LHE weight"),
            #NTupleVariable("LHEWeights"        , lambda ev: getattr(ev,'LHEWeights', 0)  if p(ev.LHEWeights) else 0              , 1000, mcOnly=True, help="LHE weights read from GenEventInfoProduct"),

            ##-------- custom jets ------------------------------------------
            #NTupleVariable("htJet25", lambda ev : ev.htJet25, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            #NTupleVariable("mhtJet25", lambda ev : ev.mhtJet25, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 25 GeV)"),
            #NTupleVariable("htJet30j", lambda ev : ev.htJet30j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 30 GeV)"),
            #NTupleVariable("htJet40j", lambda ev : ev.htJet40j, help="H_{T} computed from only jets (with |eta|<2.4, pt > 40 GeV)"),
            #NTupleVariable("htJet40", lambda ev : ev.htJet40, help="H_{T} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            #NTupleVariable("mhtJet40", lambda ev : ev.mhtJet40, help="H_{T}^{miss} computed from leptons and jets (with |eta|<2.4, pt > 40 GeV)"),
            #NTupleVariable("nSoftBJetLoose25",  lambda ev: sum([(sv.mva>0.3 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with loose sv mva"),
            #NTupleVariable("nSoftBJetMedium25", lambda ev: sum([(sv.mva>0.7 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with medium sv mva"),
            #NTupleVariable("nSoftBJetTight25",  lambda ev: sum([(sv.mva>0.9 and (sv.jet == None or sv.jet.pt() < 25)) for sv in ev.ivf]) + len(ev.bjetsMedium), int, help="Exclusive sum of jets with pt > 25 passing CSV medium and SV from ivf with tight sv mva"),
            ##------------------------------------------------

            # ----------------------- type1met systematics -------------------------------------------------------------------- #

            NTupleVariable("metNoHF_rawPt", lambda ev : ev.metNoHF.uncorPt() if  hasattr(ev,'metNoHF') else  0, help="raw noHF met p_{T}"),
            NTupleVariable("metNoHF_rawPhi", lambda ev : ev.metNoHF.uncorPhi() if  hasattr(ev,'metNoHF') else  0, help="raw noHF met phi"),
            NTupleVariable("metNoHF_rawSumEt", lambda ev : ev.metNoHF.uncorSumEt() if  hasattr(ev,'metNoHF') else  0, help="raw noHF met sumEt"),

            NTupleVariable("met_caloPt", lambda ev : ev.met.caloMETPt(), help="calo met p_{T}"),
            NTupleVariable("met_caloPhi", lambda ev : ev.met.caloMETPhi(), help="calo met phi"),
            NTupleVariable("met_caloSumEt", lambda ev : ev.met.caloMETSumEt(), help="calo met sumEt"),


            NTupleVariable("met_JetEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetEnUp), help="type1, JetEnUp, pt"),
            NTupleVariable("met_JetEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetEnUp), help="type1, JetEnUp, phi"),
            NTupleVariable("met_JetResUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResUp), help="type1, JetResUp, pt"),
            NTupleVariable("met_JetResUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResUp), help="type1, JetResUp, phi"),
            #NTupleVariable("met_JetResUpSmear_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResUpSmear), help="type1, JetResUpSmear, pt"),
            #NTupleVariable("met_JetResUpSmear_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResUpSmear), help="type1, JetResUpSmear, phi"),
            NTupleVariable("met_MuonEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.MuonEnUp), help="type1, MuonEnUp, pt"),
            NTupleVariable("met_MuonEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.MuonEnUp), help="type1, MuonEnUp, phi"),
            NTupleVariable("met_ElectronEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnUp), help="type1, ElectronEnUp, pt"),
            NTupleVariable("met_ElectronEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnUp), help="type1, ElectronEnUp, phi"),
            NTupleVariable("met_TauEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.TauEnUp), help="type1, TauEnUp, pt"),
            NTupleVariable("met_TauEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.TauEnUp), help="type1, TauEnUp, phi"),
            NTupleVariable("met_UnclusteredEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.UnclusteredEnUp), help="type1, UnclusteredEnUp, pt"),
            NTupleVariable("met_UnclusteredEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.UnclusteredEnUp), help="type1, UnclusteredEnUp, phi"),
            NTupleVariable("met_ElectronEnUp_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnUp), help="type1, ElectronEnUp, pt"),
            NTupleVariable("met_ElectronEnUp_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnUp), help="type1, ElectronEnUp, phi"),


            NTupleVariable("met_JetEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetEnDown), help="type1, JetEnDown, pt"),
            NTupleVariable("met_JetEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetEnDown), help="type1, JetEnDown, phi"),
            NTupleVariable("met_JetResDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResDown), help="type1, JetResDown, pt"),
            NTupleVariable("met_JetResDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResDown), help="type1, JetResDown, phi"),
            #NTupleVariable("met_JetResDownSmear_Pt", lambda ev : ev.met.shiftedPt(ev.met.JetResDownSmear), help="type1, JetResDownSmear, pt"),
            #NTupleVariable("met_JetResDownSmear_Phi", lambda ev : ev.met.shiftedPhi(ev.met.JetResDownSmear), help="type1, JetResDownSmear, phi"),
            NTupleVariable("met_MuonEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.MuonEnDown), help="type1, MuonEnDown, pt"),
            NTupleVariable("met_MuonEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.MuonEnDown), help="type1, MuonEnDown, phi"),
            NTupleVariable("met_ElectronEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnDown), help="type1, ElectronEnDown, pt"),
            NTupleVariable("met_ElectronEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnDown), help="type1, ElectronEnDown, phi"),
            NTupleVariable("met_TauEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.TauEnDown), help="type1, TauEnDown, pt"),
            NTupleVariable("met_TauEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.TauEnDown), help="type1, TauEnDown, phi"),
            NTupleVariable("met_UnclusteredEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.UnclusteredEnDown), help="type1, UnclusteredEnDown, pt"),
            NTupleVariable("met_UnclusteredEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.UnclusteredEnDown), help="type1, UnclusteredEnDown, phi"),
            NTupleVariable("met_ElectronEnDown_Pt", lambda ev : ev.met.shiftedPt(ev.met.ElectronEnDown), help="type1, ElectronEnDown, pt"),
            NTupleVariable("met_ElectronEnDown_Phi", lambda ev : ev.met.shiftedPhi(ev.met.ElectronEnDown), help="type1, ElectronEnDown, phi"),

            #NTupleVariable("metNoHF_JetEnUp_Pt", lambda ev : ev.metNoHF.shiftedPt(ev.met.JetEnUp) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnUp, pt"),
            #NTupleVariable("metNoHF_JetEnUp_Phi", lambda ev : ev.metNoHF.shiftedPhi(ev.met.JetEnUp) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnUp, phi"),
            #NTupleVariable("metNoHF_JetEnDown_Pt", lambda ev : ev.metNoHF.shiftedPt(ev.met.JetEnDown) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnDown, pt"),
            #NTupleVariable("metNoHF_JetEnDown_Phi", lambda ev : ev.metNoHF.shiftedPhi(ev.met.JetEnDown) if hasattr(ev,'metNoHF') else -999, help="type1 noHF , JetEnDown, phi"),





            ##--------------------------------------------------
            ## MET filter information (temporary)
            ##--------------------------------------------------
            NTupleVariable("Flag_HBHENoiseFilter_fix", lambda ev: ev.hbheFilterNew if hasattr(ev,'hbheFilterNew') else  0, help="HBEHE baseline temporary filter decision"),
            NTupleVariable("Flag_HBHEIsoNoiseFilter_fix", lambda ev: ev.hbheFilterIso if hasattr(ev,'hbheFilterIso') else  0, help="HBEHE isolation temporary filter decision"),
            NTupleVariable("Flag_badChargedHadronFilter", lambda ev: ev.badChargedHadron, help="bad charged hadron filter decision"),
            NTupleVariable("Flag_badMuonFilter", lambda ev: ev.badMuon, help="bad muon filter decision"),

            # ----------------------- HT from LHE event (requires LHE analyzer to have run)  --------------------------------------------------------- #
            NTupleVariable("lheHT", lambda ev : ev.lheHT, mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer"),
            NTupleVariable("lheHTIncoming", lambda ev : ev.lheHTIncoming, mcOnly=True, help="H_{T} computed from quarks and gluons in Heppy LHEAnalyzer (only LHE status<0 as mothers)"),
            # ---------------------------------------------------------------------------------------------------------------------------------------- #
            #ISR jet counting for SUSY reweighting
            NTupleVariable("nIsr", lambda ev : getattr(ev,"nIsr",-999) , help="Number of ISR jets not matched to gen particles"),


]
susySingleLepton_globalObjects = susyCore_globalObjects.copy()
susySingleLepton_globalObjects.update({
            # put more here
})

susySingleLepton_collections = susyCore_collections.copy()
susySingleLepton_collections.update({

            # put more here
            #"genParticles"     : NTupleCollection("genPartAll",  genParticleWithMotherId, 200, help="all pruned genparticles"), # need to decide which gen collection ?
            "genParticles"     : NTupleCollection("genPartAll",  genParticleWithMotherIndex, 200, help="all pruned genparticles"), # need to decide which gen collection ?
            ## ---------------------------------------------
            "selectedLeptons" : NTupleCollection("LepGood", leptonTypeDegStop, 8, help="Leptons after the preselection"),
            "otherLeptons"    : NTupleCollection("LepOther", leptonTypeDegStop, 8, help="Leptons after the preselection"),
            "selectedTaus"    : NTupleCollection("TauGood", tauTypeSusy, 3, help="Taus after the preselection"),
            #"selectedIsoTrack"    : NTupleCollection("isoTrack", isoTrackType, 50, help="isoTrack, sorted by pt"),
            ##------------------------------------------------
            "cleanJetsAll"       : NTupleCollection("Jet",     jetTypeSusy, 25, help="Cental jets after full selection and cleaning, sorted by pt"),
            "allJetsUsedForMET"       : NTupleCollection("JetForMET",     jetType, 40, help="All Jets used for MET"),

            ## DegStop:
            #"packedGenParticles"  : NTupleCollection("genPartPkd",  packedGenParticleWithMotherIndex, 2000, help="all packed genparticles"),
            "cleanGenJets"    : NTupleCollection("GenJet",  genJetType,  30, help="Clean Gen Jets, sorted by pt"),
            "genJets"         : NTupleCollection("GenJetDirty",  genJetType,  30, help="Gen Jets before cleaning, sorted by pt"),


            #"Tracks"              : NTupleCollection("Tracks",      trackTypeSusy, 150, help="all Tracks from PackedPFCandidates (pt>1) , sorted by pt"),
            #"GenTracks"           : NTupleCollection("GenTracks",   genTrackTypeSusy, 150, mcOnly=True, help="all Tracks from PackedPFCandidates (pt>1) , sorted by pt"),



            ####


            #"discardedJets"    : NTupleCollection("DiscJet", jetTypeSusy, 15, help="Jets discarted in the jet-lepton cleaning"),
            ##------------------------------------------------
            #"ivf"       : NTupleCollection("SV",     svType, 20, help="SVs from IVF"),
            "LHE_weights"    : NTupleCollection("LHEweight" ,  weightsInfoType, 1000, mcOnly=True, help="LHE weight info"),
})

