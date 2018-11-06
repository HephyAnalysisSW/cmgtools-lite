import operator 
import itertools
import copy

from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg

class deepLeptonIsoProducer( Analyzer ):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(deepLeptonIsoProducer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.pfCandAssocDR = getattr(cfg_ana, "pfCandAssocDR", 0.)
        self.ivfAssocDR    = getattr(cfg_ana, "ivfAssocDR", 0.)
        self.otherLeptons  = getattr(cfg_ana, "otherLeptons", False)

    def declareHandles(self):
        super(deepLeptonIsoProducer, self).declareHandles()
        self.handles['packedCandidates'] = AutoHandle( self.cfg_ana.packedCandidates, 'std::vector<pat::PackedCandidate>')

    def beginLoop(self, setup):
        super(deepLeptonIsoProducer,self).beginLoop( setup )

    def process(self, event):
        self.readCollections( event.input )
        
        # defaults
        isolation_candidates = []
        event.ivf_candidates = []

        # do nothing if there are no leptons
        leptons = event.selectedLeptons
        if self.otherLeptons: leptons += event.otherLeptons
        if len( leptons ) == 0 :
            return

        for pfCand in self.handles['packedCandidates'].product():
            for i_lepton, lepton in enumerate( event.selectedLeptons[:16] ):
               if deltaR(lepton.eta(),lepton.phi(),pfCand.eta(),pfCand.phi())<self.pfCandAssocDR:
                    # if this is a new pf candidate, it 
                    if not hasattr( pfCand, "selectedLeptons_mask" ): 
                        pfCand.selectedLeptons_mask = 0
                    if self.otherLeptons: 
                        if not hasattr( pfCand, "otherLeptons_mask" ): 
                            pfCand.otherLeptons_mask = 0 
                    pfCand.selectedLeptons_mask |= (1 << i_lepton)
                    if pfCand not in isolation_candidates: isolation_candidates.append( pfCand )
            if self.otherLeptons: 
                for i_lepton, lepton in enumerate( event.otherLeptons[:16] ):
                   if deltaR(lepton.eta(),lepton.phi(),pfCand.eta(),pfCand.phi())<self.pfCandAssocDR:
                        # if this is a new pf candidate, it 
                        if not hasattr( pfCand, "selectedLeptons_mask" ): 
                            pfCand.selectedLeptons_mask = 0 
                        if not hasattr( pfCand, "otherLeptons_mask" ): 
                            pfCand.otherLeptons_mask = 0 
                        pfCand.otherLeptons_mask |= (1 << i_lepton)
                        if pfCand not in isolation_candidates: isolation_candidates.append( pfCand )

#        for pfCand in isolation_candidates:
#            print "Cand pt %3.2f %3.2f pdgId %i mask(sel) %i mask(other) %i" %(pfCand.pt(), pfCand.eta(), pfCand.pdgId(), pfCand.selectedLeptons_mask, pfCand.otherLeptons_mask)

        event.pfCands_neutral = filter( lambda p: abs(p.pdgId()) == 130, isolation_candidates)
        event.pfCands_charged = filter( lambda p: abs(p.pdgId()) == 211, isolation_candidates)
        event.pfCands_photon  = filter( lambda p: abs(p.pdgId()) == 22, isolation_candidates)
        event.pfCands_electron= filter( lambda p: abs(p.pdgId()) == 11, isolation_candidates)
        event.pfCands_muon    = filter( lambda p: abs(p.pdgId()) == 13, isolation_candidates)
        event.pfCands_neutral .sort(key = lambda p:-p.pt())  
        event.pfCands_charged .sort(key = lambda p:-p.pt())
        event.pfCands_photon  .sort(key = lambda p:-p.pt())
        event.pfCands_electron.sort(key = lambda p:-p.pt())
        event.pfCands_muon    .sort(key = lambda p:-p.pt())

        print "total", len(isolation_candidates), "ne/ch/ph/el/mu/",len(event.pfCands_neutral),len(event.pfCands_charged),len(event.pfCands_photon), len(event.pfCands_electron), len(event.pfCands_muon)
    
        if hasattr(event, "ivf"):
            for ivf in event.ivf:
                for i_lepton, lepton in enumerate( event.selectedLeptons[:16] ):
                   if deltaR(lepton.eta(),lepton.phi(),ivf.eta(),ivf.phi())<self.ivfAssocDR:
                        # if this is a new pf candidate, it 
                        if not hasattr( ivf, "selectedLeptons_mask" ): 
                            ivf.selectedLeptons_mask = 0 
                        if self.otherLeptons: 
                            if not hasattr( ivf, "otherLeptons_mask" ): 
                                ivf.otherLeptons_mask = 0 
                        ivf.selectedLeptons_mask |= (1 << i_lepton)
                        event.ivf_candidates.append( ivf )
                if self.otherLeptons: 
                    for i_lepton, lepton in enumerate( event.otherLeptons[:16] ):
                       if deltaR(lepton.eta(),lepton.phi(),ivf.eta(),ivf.phi())<self.ivfAssocDR:
                            # if this is a new pf candidate, it 
                            if not hasattr( ivf, "selectedLeptons_mask" ): 
                                ivf.selectedLeptons_mask = 0 
                            if not hasattr( ivf, "otherLeptons_mask" ): 
                                ivf.otherLeptons_mask = 0 
                            ivf.otherLeptons_mask |= (1 << i_lepton)
                            event.ivf_candidates.append( ivf )
#        for ivf in event.ivf_candidates:
#            print "IVF pt %3.2f %3.2f mask(sel) %i mask(other) %i" %(ivf.pt(), ivf.eta(),  ivf.selectedLeptons_mask, ivf.otherLeptons_mask)

                    
setattr(deepLeptonIsoProducer,"defaultConfig", cfg.Analyzer(
        class_object = deepLeptonIsoProducer,
        packedCandidates = 'packedPFCandidates',
        pfCandAssocDR = 0.5, #DR below which pf cands are associated to the lepton 
        ivfAssocDR = 0.6, #DR below which IVF are associated to the lepton
        otherLeptons = False, # whether to run on other leptons 
        )
)
