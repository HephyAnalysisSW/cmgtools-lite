from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.HeppyCore.utils.deltar import *

import ROOT
ROOT.gInterpreter.ProcessLine("#include <DataFormats/MuonReco/interface/MuonSelectors.h>")


class badGlobalMuonAnalyzer( Analyzer ):

    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(badGlobalMuonAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.ptCut_                     = getattr(cfg_ana , "muonPtCut" )
        self.selectClones_              = getattr(cfg_ana , "selectClones" )

    def declareHandles(self):
        super(badGlobalMuonAnalyzer, self).declareHandles()

    #
    # From Giovanni's code: https://hypernews.cern.ch/HyperNews/CMS/get/physics-validation/2786.html
    #

    def outInOnly(self,mu):
        tk = mu.innerTrack().get();
        return tk.algoMask().count() == 1 and tk.isAlgoInMask(tk.muonSeededStepOutIn);

    def preselection(self, mu):
        return mu.isGlobalMuon() and (not(self.selectClones_) or self.outInOnly(mu));

    def tighterId(self, mu):
        return mu.isMediumMuon() and mu.numberOfMatchedStations() >= 2;

    def tightGlobal(self, mu):
        return (mu.globalTrack().hitPattern().muonStationsWithValidHits() >= 3 and mu.globalTrack().normalizedChi2() <= 20);

    def safeId(self, mu):
        if (mu.muonBestTrack().ptError() > 0.2 * mu.muonBestTrack().pt()): return False;
        return mu.numberOfMatchedStations() >= 1 or self.tightGlobal(mu);

    def partnerId(self, mu):
        return mu.pt() >= 10 and mu.numberOfMatchedStations() >= 1;

    def tagBadGlobalMuons(self, allmuons, allvertices):
        """Returns the list of bad muons in an event"""

        muons = list(m for m in allmuons) # make it a python list
        goodMuon = []

        if len(allvertices) < 1: raise RuntimeError
        PV = allvertices[0].position()

        out = []
        for mu in muons:
            if (not(mu.isPFMuon()) or mu.innerTrack().isNull()):
                goodMuon.append(-1); # bad but we don't care
                continue;
            if (self.preselection(mu)):
                dxypv = abs(mu.innerTrack().dxy(PV));
                dzpv  = abs(mu.innerTrack().dz(PV));
                if (self.tighterId(mu)):
                    ipLoose = ((dxypv < 0.5 and dzpv < 2.0) or mu.innerTrack().hitPattern().pixelLayersWithMeasurement() >= 2);
                    goodMuon.append(ipLoose or (not(self.selectClones_) and self.tightGlobal(mu)));
                elif (self.safeId(mu)):
                    ipTight = (dxypv < 0.2 and dzpv < 0.5);
                    goodMuon.append(ipTight);
                else:
                    goodMuon.append(0);
            else:
                goodMuon.append(3); # maybe good, maybe bad, but we don't care

        n = len(muons)
        for i in xrange(n):
            if (muons[i].pt() < self.ptCut_ or goodMuon[i] != 0): continue;
            bad = True;
            if (self.selectClones_):
                bad = False; # unless proven otherwise
                n1 = muons[i].numberOfMatches(ROOT.reco.Muon.SegmentArbitration);
                for j in xrange(n):
                    if (j == i or goodMuon[j] <= 0 or not(self.partnerId(muons[j]))): continue
                    n2 = muons[j].numberOfMatches(ROOT.reco.Muon.SegmentArbitration);
                    if (deltaR(muons[i],muons[j]) < 0.4 or (n1 > 0 and n2 > 0 and ROOT.muon.sharedSegments(muons[i],muons[j]) >= 0.5*min(n1,n2))):
                        bad = True;
                        break;
            if (bad):
                muons[i].isBadGlobalMuon = 1
                out.append(muons[i]);
        return out


    def beginLoop(self, setup):
        super(badGlobalMuonAnalyzer,self).beginLoop( setup )

    def process(self, event):
        self.readCollections( event.input )
        
        allLeptons  = event.selectedLeptons + event.otherLeptons
        allMuons    = [ lep for lep in allLeptons if abs(lep.pdgId())==13 ]
        allVertices = event.vertices

        badMuons = self.tagBadGlobalMuons( allMuons, allVertices )

        if badMuons:
            print "Found Bad Muons (%s) in the Event!"%len(badMuons)
            print badMuons

        return True

    def printInfo(self, event):
        pass 

#            print 'found muon: run=', event.run,' lumi=', event.lumi,' event',event.eventId

setattr(badGlobalMuonAnalyzer,"defaultConfig", cfg.Analyzer(
        class_object = badGlobalMuonAnalyzer,
        selectClones = True,
        muonPtCut    = 3.0 , 
        )
)
