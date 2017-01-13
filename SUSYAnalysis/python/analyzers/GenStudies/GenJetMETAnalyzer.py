import math, os
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Jet
from PhysicsTools.HeppyCore.utils.deltar import deltaR2, deltaPhi, matchObjectCollection, matchObjectCollection2, bestMatch,matchObjectCollection3
import PhysicsTools.HeppyCore.framework.config as cfg

from PhysicsTools.Heppy.physicsutils.QGLikelihoodCalculator import QGLikelihoodCalculator

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
from PhysicsTools.Heppy.physicsutils.genutils import *


import copy

class GenJetMETAnalyzer( Analyzer ):
    """Taken from RootTools.JetAnalyzer, simplified, modified, added corrections    """
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(GenJetMETAnalyzer,self).__init__(cfg_ana, cfg_comp, looperName)

    def declareHandles(self):
        super(GenJetMETAnalyzer, self).declareHandles()
        self.handles['genJet'] = AutoHandle( self.cfg_ana.genJetCol, 'vector<reco::GenJet>' )
        self.handles['genMET'] = AutoHandle( 'genMetTrue' , 'vector<reco::GenMET>')
        
 
    def beginLoop(self, setup):
        super(GenJetMETAnalyzer,self).beginLoop(setup)

    def matchGenJetsToBs(self,genJets, genParts, varName = "bTag" , maxDR = 0.4):
        bs = []
        for igp , gp in enumerate( genParts ):
            setattr( gp , varName , False)
            if gp.status() != 2: continue
            id = abs(gp.pdgId())
            if id == 5 or ((id % 1000) / 100) == 5 or ((id % 10000)/1000) == 5:
                bs.append( (igp, gp) )
        for j in genJets:
            setattr( j , varName , False)
            drs = []
            for igp, gp in bs:
                dr  = deltaR(gp.eta(),gp.phi(),j.eta(),j.phi())
                if dr < maxDR:
                    setattr( gp , varName , True)
                    setattr( j , varName , True)
                    drs.append( (dr, igp) )
            if drs:
                minDr , igp = min(drs)
                setattr( j, varName+"_minDr", minDr    )
                setattr( j, varName+"_minDrIndex" , igp)
                print drs
                print minDr, igp
                print '--------------------------'    
                    
        return

    def process(self, event):
        self.readCollections( event.input )

       

        if self.cfg_comp.isMC:
            #event.genMET  = [ x for x in self.handles['genMET'].product() ]
            event.genMET  = self.handles['genMET'].product()[0]
            #print len(self.handles['genMET'].product() )
            #print event.genMET.pt()
            #print event.genMET.phi()
            self.genJets = [ x for x in self.handles['genJet'].product() ]
            setattr(event,"genJets"                +self.cfg_ana.collectionPostFix, self.genJets                )
            
            self.matchGenJetsToBs( self.genJets, event.genParticles     , "bHadronMatched")
            #self.matchGenJetsToBs( self.genJets, event.generatorSummary , "bQuarkMatched")

 
        return True

        





setattr(GenJetMETAnalyzer,"defaultConfig", cfg.Analyzer(
    class_object = GenJetMETAnalyzer,
    copyJetsByValue = False,      #Whether or not to copy the input jets or to work with references (should be 'True' if JetAnalyzer is run more than once)
    genJetCol = 'slimmedGenJets',
    collectionPostFix = ""
    )
)
