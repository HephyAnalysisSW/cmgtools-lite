#!/bin/env python
from math import *
from PhysicsTools.Heppy.analyzers.core.autovars import NTupleObjectType  
from PhysicsTools.Heppy.analyzers.objects.autophobj import  *
from PhysicsTools.HeppyCore.utils.deltar import deltaR

#from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *
#from CMGTools.TTHAnalysis.signedSip import *

##------------------------------------------  
## LEPTON
##------------------------------------------  

leptonTypeDegStop = NTupleObjectType("leptonDegStop", baseObjectTypes = [ leptonType ], variables = [
    NTupleVariable("mvaIdSpring15",   lambda lepton : lepton.mvaRun2("NonTrigSpring15MiniAOD") if abs(lepton.pdgId()) == 11 else 1, help="EGamma POG MVA ID for non-triggering electrons, Spring15 re-training; 1 for muons"),

    # CLEANUP # # Lepton MVA-id related variables
    # CLEANUP # NTupleVariable("mvaTTH",    lambda lepton : getattr(lepton, 'mvaValueTTH', -1), help="Lepton MVA (TTH version)"),
    # CLEANUP # NTupleVariable("jetPtRatiov1", lambda lepton : lepton.pt()/lepton.jet.pt() if hasattr(lepton,'jet') else -1, help="pt(lepton)/pt(nearest jet)"),
    # CLEANUP # NTupleVariable("jetPtRelv1", lambda lepton : ptRelv1(lepton.p4(),lepton.jet.p4()) if hasattr(lepton,'jet') else -1, help="pt of the lepton transverse to the jet axis (subtracting the lepton)"),
    # CLEANUP # NTupleVariable("jetPtRatiov2", lambda lepton: lepton.pt()/jetLepAwareJEC(lepton).Pt() if hasattr(lepton,'jet') else -1, help="pt(lepton)/[rawpt(jet-PU-lep)*L2L3Res+pt(lepton)]"),
    # CLEANUP # NTupleVariable("jetPtRelv2", lambda lepton : ptRelv2(lepton) if hasattr(lepton,'jet') else -1, help="pt of the lepton transverse to the jet axis (subtracting the lepton) - v2"),
    # CLEANUP # NTupleVariable("jetBTagCSV", lambda lepton : lepton.jet.btag('pfCombinedInclusiveSecondaryVertexV2BJetTags') if hasattr(lepton,'jet') and hasattr(lepton.jet, 'btag') else -99, help="CSV btag of nearest jet"),
    # CLEANUP # NTupleVariable("jetBTagCMVA", lambda lepton : lepton.jet.btag('pfCombinedMVABJetTags') if hasattr(lepton,'jet') and hasattr(lepton.jet, 'btag') else -99, help="CMA btag of nearest jet"),
    # CLEANUP # NTupleVariable("jetDR",      lambda lepton : deltaR(lepton.eta(),lepton.phi(),lepton.jet.eta(),lepton.jet.phi()) if hasattr(lepton,'jet') else -1, help="deltaR(lepton, nearest jet)"),
    # CLEANUP # NTupleVariable("r9",      lambda lepton : lepton.full5x5_r9() if abs(lepton.pdgId()) == 11 else -99, help="SuperCluster 5x5 r9 variable, only for electrons; -99 for muons"),

 # ID variables
    NTupleVariable("SPRING15_25ns_v1", lambda x : (1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Loose") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Medium") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Tight")) if abs(x.pdgId()) == 11 else -1, int, help="Electron cut-based id (POG_SPRING15_25ns_v1_ConvVetoDxyDy): 0=none, 1=veto, 2=loose, 3=medium, 4=tight"),
    NTupleVariable("eleCBID_SPRING15_25ns_ConvVetoDxyDz", lambda x : (1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Veto") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Loose") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Medium") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_ConvVetoDxyDz_Tight")) if abs(x.pdgId()) == 11 else -1, int, help="Electron cut-based id (POG_SPRING15_25ns_v1_ConvVetoDxyDy): 0=none, 1=veto, 2=loose, 3=medium, 4=tight"),
    NTupleVariable("eleCBID_SPRING15_25ns", lambda x : (1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_Veto") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_Loose") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_Medium") + 1*x.electronID("POG_Cuts_ID_SPRING15_25ns_v1_Tight")) if abs(x.pdgId()) == 11 else -1, int, help="Electron cut-based id (POG_SPRING15_25ns_v1_ConvVetoDxyDy): 0=none, 1=veto, 2=loose, 3=medium, 4=tight"),

    # Low level vars -- duplicates of leptonSusyExtra
    NTupleVariable("hOverE", lambda x : x.hadronicOverEm() if abs(x.pdgId())==11 else 0, help="Electron hadronicOverEm"),
    NTupleVariable("ooEmooP",  lambda x : ((1.0/x.ecalEnergy() - x.eSuperClusterOverP()/x.ecalEnergy()) if x.ecalEnergy()>0. else 9e9) if abs(x.pdgId())==11 else 0, help="Electron 1/E - 1/p  (without absolute value!)"),
    # Extra isolation variables
    #NTupleVariable("chargedHadRelIso03",  lambda x : x.chargedHadronIsoR(0.3)/x.pt(), help="PF Rel Iso, R=0.3, charged hadrons only"),
    #NTupleVariable("chargedHadRelIso04",  lambda x : x.chargedHadronIsoR(0.4)/x.pt(), help="PF Rel Iso, R=0.4, charged hadrons only"),
    # Extra muon ID working points

    NTupleVariable("softMuonId", lambda x : x.muonID("POG_ID_Soft") if abs(x.pdgId())==13 else 1, int, help="Muon POG Soft id"),
    NTupleVariable("looseMuonId",   lambda x : x.muonID("POG_ID_Loose") if abs(x.pdgId())==13 else 1, int, help="Muon POG Loose id"),
    #
    NTupleVariable("absIso03",  lambda x : x.absIso03  , help="PF Abs Iso, R=0.3, pile-up corrected"),
    NTupleVariable("absIso",  lambda x : x.absIso04 , help="PF Rel Iso, R=0.4, pile-up corrected"),
    #NTupleVariable("hybIso",  lambda x : x.relIso04 * x.pt() if True, help="PF Rel Iso, R=0.4, pile-up corrected"),
    NTupleVariable("cosPhiLepMet",  lambda x : x.cosLMet , help="Cos phi of the lepton and met  "),
    NTupleVariable("mt",          lambda x : x.mt, help="Transverse Mass calculated for lepton"),
    NTupleVariable("Q80",         lambda x : x.Q80  , help="Q80 variable for the deconstrcuted transverse mass"),
    #

    #NTupleVariable("eleCutId2012_full5x5",     lambda x : (1*x.electronID("POG_Cuts_ID_2012_full5x5_Veto") + 1*x.electronID("POG_Cuts_ID_2012_full5x5_Loose") + 1*x.electronID("POG_Cuts_ID_2012_full5x5_Medium") + 1*x.electronID("POG_Cuts_ID_2012_full5x5_Tight")) if abs(x.pdgId()) == 11 else -1, int, help="Electron cut-based id (POG 2012, full5x5 shapes): 0=none, 1=veto, 2=loose, 3=medium, 4=tight"),
    NTupleVariable("sigmaIEtaIEta",  lambda x : x.full5x5_sigmaIetaIeta() if abs(x.pdgId())==11 else 0, help="Electron sigma(ieta ieta), with full5x5 cluster shapes"),
    NTupleVariable("dEtaScTrkIn",    lambda x : x.deltaEtaSuperClusterTrackAtVtx() if abs(x.pdgId())==11 else 0, help="Electron deltaEtaSuperClusterTrackAtVtx (without absolute value!)"),
    NTupleVariable("dPhiScTrkIn",    lambda x : x.deltaPhiSuperClusterTrackAtVtx() if abs(x.pdgId())==11 else 0, help="Electron deltaPhiSuperClusterTrackAtVtx (without absolute value!)"),
    NTupleVariable("hadronicOverEm", lambda x : x.hadronicOverEm() if abs(x.pdgId())==11 else 0, help="Electron hadronicOverEm"),
    NTupleVariable("eInvMinusPInv",  lambda x : ((1.0/x.ecalEnergy() - x.eSuperClusterOverP()/x.ecalEnergy()) if x.ecalEnergy()>0. else 9e9) if abs(x.pdgId())==11 else 0, help="Electron 1/E - 1/p  (without absolute value!)"),

#    new version used by EGM in Spring15, 7_4_14:
    NTupleVariable("eInvMinusPInv_tkMom", lambda x: ((1.0/x.ecalEnergy()) - (1.0 / x.trackMomentumAtVtx().R() ) if (x.ecalEnergy()>0. and x.trackMomentumAtVtx().R()>0.) else 9e9) if abs(x.pdgId())==11 else 0, help="Electron 1/E - 1/p_tk_vtx  (without absolute value!)"),
    NTupleVariable("etaSc", lambda x : x.superCluster().eta() if abs(x.pdgId())==11 else -100, help="Electron supercluster pseudorapidity"),
])


##------------------------------------------  
## TAU
##------------------------------------------  

tauTypeSusy = NTupleObjectType("tauSusy",  baseObjectTypes = [ tauType ], variables = [
])

##------------------------------------------  
## PHOTON
##------------------------------------------  

photonTypeSusy = NTupleObjectType("gammaSusy", baseObjectTypes = [ photonType ], variables = [
    NTupleVariable("genIso04",  lambda x : getattr(x, 'genIso04', -1.0), float, mcOnly=True, help="sum pt of all status 1 particles within DeltaR = 0.4 of the photon"),
    NTupleVariable("genIso03",  lambda x : getattr(x, 'genIso03', -1.0), float, mcOnly=True, help="sum pt of all status 1 particles within DeltaR = 0.3 of the photon"),
    NTupleVariable("chHadIsoRC04",  lambda x : getattr(x, 'chHadIsoRC04', -1.0), float, mcOnly=False, help="charged iso 0.4 in a random cone 90 degrees in phi from photon"),
    NTupleVariable("chHadIsoRC",  lambda x : getattr(x, 'chHadIsoRC03', -1.0), float, mcOnly=False, help="charged iso 0.3 in a random cone 90 degrees in phi from photon"),
    NTupleVariable("drMinParton",  lambda x : getattr(x, 'drMinParton', -1.0), float, mcOnly=True, help="deltaR min between photon and parton"),
])

##------------------------------------------  
## JET
##------------------------------------------  

jetTypeSusy = NTupleObjectType("jetSusy",  baseObjectTypes = [ jetType ], variables = [

    #NTupleVariable("DFudsg", lambda x : x.btag('deepFlavourJetTags:probudsg'), float, help="Deep flavor discriminator: udsg"),
    #NTupleVariable("DFb",    lambda x : x.btag('deepFlavourJetTags:probb'),    float, help="Deep flavor discriminator: b"),
    #NTupleVariable("DFc",    lambda x : x.btag('deepFlavourJetTags:probc'),    float, help="Deep flavor discriminator: c"),
    #NTupleVariable("DFbb",   lambda x : x.btag('deepFlavourJetTags:probbb'),   float, help="Deep flavor discriminator: bb"),
    #NTupleVariable("DFcc",   lambda x : x.btag('deepFlavourJetTags:probcc'),   float, help="Deep flavor discriminator: cc"),

    #NTupleVariable("DFCMVAudsg", lambda x : x.btag('deepFlavourCMVAJetTags:probudsg'), float, help="Deep flavor discriminator: udsg"),
    #NTupleVariable("DFCMVAb",    lambda x : x.btag('deepFlavourCMVAJetTags:probb'),    float, help="Deep flavor discriminator: b"),
    #NTupleVariable("DFCMVAc",    lambda x : x.btag('deepFlavourCMVAJetTags:probc'),    float, help="Deep flavor discriminator: c"),
    #NTupleVariable("DFCMVAbb",   lambda x : x.btag('deepFlavourCMVAJetTags:probbb'),   float, help="Deep flavor discriminator: bb"),
    #NTupleVariable("DFCMVAcc",   lambda x : x.btag('deepFlavourCMVAJetTags:probcc'),   float, help="Deep flavor discriminator: cc"),



    NTupleVariable("mcMatchFlav",  lambda x : getattr(x,'mcMatchFlav',-99), int, mcOnly=True, help="Flavour of associated parton from hard scatter (if any)"),
    NTupleVariable("chHEF", lambda x : x.chargedHadronEnergyFraction(), float, mcOnly = False, help="chargedHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("neHEF", lambda x : x.neutralHadronEnergyFraction(), float, mcOnly = False,help="neutralHadronEnergyFraction (relative to uncorrected jet energy)"),
    NTupleVariable("phEF", lambda x : x.photonEnergyFraction(), float, mcOnly = False,help="photonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("eEF", lambda x : x.electronEnergyFraction(), float, mcOnly = False,help="electronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("muEF", lambda x : x.muonEnergyFraction(), float, mcOnly = False,help="muonEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("HFHEF", lambda x : x.HFHadronEnergyFraction(), float, mcOnly = False,help="HFHadronEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("HFEMEF", lambda x : x.HFEMEnergyFraction(), float, mcOnly = False,help="HFEMEnergyFraction (relative to corrected jet energy)"),
    NTupleVariable("chHMult", lambda x : x.chargedHadronMultiplicity(), int, mcOnly = False,help="chargedHadronMultiplicity from PFJet.h"),
    NTupleVariable("neHMult", lambda x : x.neutralHadronMultiplicity(), int, mcOnly = False,help="neutralHadronMultiplicity from PFJet.h"),
    NTupleVariable("phMult", lambda x : x.photonMultiplicity(), int, mcOnly = False,help="photonMultiplicity from PFJet.h"),
    NTupleVariable("eMult", lambda x : x.electronMultiplicity(), int, mcOnly = False,help="electronMultiplicity from PFJet.h"),
    NTupleVariable("muMult", lambda x : x.muonMultiplicity(), int, mcOnly = False,help="muonMultiplicity from PFJet.h"),
    NTupleVariable("HFHMult", lambda x : x.HFHadronMultiplicity(), int, mcOnly = False,help="HFHadronMultiplicity from PFJet.h"),
    NTupleVariable("HFEMMult", lambda x : x.HFEMMultiplicity(), int, mcOnly = False,help="HFEMMultiplicity from PFJet.h"),
])

      
##------------------------------------------  
## MET
##------------------------------------------  
  
metTypeSusy = NTupleObjectType("metSusy", baseObjectTypes = [ metType ], variables = [
])


##------------------------------------------  
## GENPARTICLE
##------------------------------------------  

genParticleWithMotherIndex = NTupleObjectType("genParticleWithMotherIndex", baseObjectTypes = [ genParticleWithMotherId ], mcOnly=True, variables = [
    NTupleVariable("nDaughters", lambda x : x.numberOfDaughters(), int, help="index of the daughters in the genParticles"),
    NTupleVariable("nMothers", lambda x : x.numberOfMothers(), int, help="index of the mother in the genParticles"),
    NTupleVariable("motherIndex1", lambda x : x.motherRef(0).index() if x.numberOfMothers() > 0 else -1, int, help="index of the first mother in the genParticles"),
    NTupleVariable("daughterIndex1", lambda x : x.daughterRef(0).index() if x.numberOfDaughters() >0 else -1, int, help="index of the first mother in the genParticles"),
    NTupleVariable("motherIndex2", lambda x : x.motherRef(x.numberOfMothers()-1).index() if x.numberOfMothers() > 1 else -1, int, help="index of the last mother in the genParticles"),
    NTupleVariable("daughterIndex2", lambda x : x.daughterRef(x.numberOfDaughters()-1).index() if x.numberOfDaughters() > 1 else -1, int, help="index of the last mother in the genParticles"),
])





##------------------------------------------  
## TRACKS
##------------------------------------------  


genTrackTypeSusy = NTupleObjectType("genTrackSusy",  baseObjectTypes = [ isoTrackType ], variables = [
    
    NTupleVariable("matchedJetIndex",     lambda x : x.matchedJetIndex , help="index of the matched Jet to the track"),
    NTupleVariable("matchedJetDr",        lambda x : x.matchedJetDr    , help="deltaR of the matched Jet to the track"),
    NTupleVariable("matchedLepIndex",     lambda x : x.matchedLepIndex , help="index of the matched Lepton to the track"),
    NTupleVariable("matchedLepDr",        lambda x : x.matchedLepDr    , help="deltaR of the matched Lepton to the track"),
    NTupleVariable("matchedGenPartIndex", lambda x : x.matchedGenPartIndex , mcOnly=True, help="index of the matched GenParticle to the track"),
    NTupleVariable("matchedGenPartDr",    lambda x : x.matchedGenPartDr    , mcOnly=True, help="deltaR of the matched GenPartricle to the track"),
    NTupleVariable("CosPhiMet",          lambda x : x.CosPhiMet   , help="Cos Track Phi with Met"     ),
    NTupleVariable("CosPhiJet1",          lambda x : x.CosPhiJet1   , help="Cos Track Phi with the Leading Jet"     ),
    NTupleVariable("CosPhiJet12",          lambda x : x.CosPhiJet12   , help="Cos Track Phi with the Leading + SubJet"),
    NTupleVariable("CosPhiJetAll",        lambda x : x.CosPhiJetAll , help="Cos Track Phi with the All Jets"     ),
])  
    
trackTypeSusy = NTupleObjectType("trackSusy",  baseObjectTypes = [ genTrackTypeSusy ], variables = [
    
    NTupleVariable("dxy",                 lambda x : x.dxy() , help="d_{xy} of lead track with respect to PV, in cm (with sign)"), 
    NTupleVariable("dxyError",            lambda x : x.dxyError() , help="d_{xy}Err of lead track with respect to PV, in cm (with sign)"),
    NTupleVariable("dzError",             lambda x : x.dzError() , help="d_{z}Err of lead track with respect to PV, in cm (with sign)"),
    NTupleVariable("fromPV",              lambda x : x.fromPV()  , help="is fromPV"),
    NTupleVariable("isJet",               lambda x : x.isJet()),
    NTupleVariable("numberOfPixleHits",   lambda x : x.numberOfPixelHits(), int),
    NTupleVariable("numberOfHits",        lambda x : x.numberOfHits(), int ),
    NTupleVariable("trackHighPurity",     lambda x : x.trackHighPurity(), int),
    NTupleVariable("puppiWeight",         lambda x : x.puppiWeight()  ),
    NTupleVariable("mcMatchIndex",        lambda x : x.mcMatchIndex ),
    NTupleVariable("mcMatchDr",           lambda x : x.mcMatchDr ),
    NTupleVariable("mcMatchPtRatio",           lambda x : x.mcMatchPtRatio ),

])




genJetType = NTupleObjectType("genJets",  baseObjectTypes = [ fourVectorType ], mcOnly=True, variables = [
    NTupleVariable("nConstituents", lambda x : x.nConstituents() ,help="Number of Constituents"),
])




