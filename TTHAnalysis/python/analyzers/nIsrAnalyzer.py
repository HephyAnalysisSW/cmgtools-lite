from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.utils.deltar import deltaR2
import math

##__________________________________________________________________||
class NIsrAnalyzer(Analyzer):

    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(NIsrAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.genPartCollection = getattr(cfg_ana, 'genPartCollection', 'genParticles')
        self.jetCollection =     getattr(cfg_ana, 'jetCollection',     'cleanJetsAll')
        self.isrPrefix =         getattr(cfg_ana, 'isrPrefix',  '')

    def process(self, event):

        if not self.cfg_comp.isMC: return True # Can only be performed on MC
   
        genPartCol = getattr(event, self.genPartCollection)
        jetCol =     getattr(event, self.jetCollection)
 
        self.findIsr(event, genPartCol, jetCol, self.isrPrefix)
    
        return True
   
    @staticmethod 
    def findIsr(event, genPartCol, jetCol, isrPrefix):
        nIsr = 0 
        for jet in jetCol:

            if jet.pt()<30.0: continue
            if abs(jet.eta())>2.4: continue
            matched = False
            for mc in genPartCol: 
                if matched: break
                if (mc.status()!=23 or abs(mc.pdgId())>5): continue
                momid = abs(mc.mother().pdgId())
                if not (momid==6 or momid==23 or momid==24 or momid==25 or momid>1e6): continue
                    #check against daughter in case of hard initial splitting
                for idau in range(mc.numberOfDaughters()):
                    dR = math.sqrt(deltaR2(jet.eta(),jet.phi(), mc.daughter(idau).p4().eta(),mc.daughter(idau).p4().phi()))
                    if dR<0.3:
                        matched = True
                        break
            if not matched:
                nIsr += 1 
                setattr(jet, 'is%sIsr'%isrPrefix, 1)

        setattr(event, 'n%sIsr'%isrPrefix, nIsr)

##__________________________________________________________________||
