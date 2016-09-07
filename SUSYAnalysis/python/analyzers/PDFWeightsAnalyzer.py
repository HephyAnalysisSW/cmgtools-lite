from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
import PhysicsTools.HeppyCore.framework.config as cfg
from ROOT.gen import WeightsInfo
        
class PDFWeightsAnalyzer( Analyzer ):
    """    """
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(PDFWeightsAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.doPDFWeights = hasattr(self.cfg_ana, "PDFWeights") and len(self.cfg_ana.PDFWeights) > 0
        self.doPDFVars   = hasattr(self.cfg_ana, "doPDFVars") and self.cfg_ana.doPDFVars == True
        self.doLHEWeights = getattr(self.cfg_ana, "doLHEWeights")
        if self.doPDFWeights:
            self.pdfWeightInit = False
    #---------------------------------------------
    # DECLARATION OF HANDLES OF GEN LEVEL OBJECTS 
    #---------------------------------------------
        

    def declareHandles(self):
        super(PDFWeightsAnalyzer, self).declareHandles()

        if self.doPDFVars or self.doPDFWeights or self.doLHEWeights:
            self.mchandles['pdfstuff'] = AutoHandle( 'generator', 'GenEventInfoProduct' )

    def beginLoop(self, setup):
        super(PDFWeightsAnalyzer,self).beginLoop(setup)

    def initPDFWeights(self):
        from ROOT import PdfWeightProducerTool
        self.pdfWeightInit = True
        self.pdfWeightTool = PdfWeightProducerTool()
        for pdf in self.cfg_ana.PDFWeights:
            self.pdfWeightTool.addPdfSet(pdf+".LHgrid")
        self.pdfWeightTool.beginJob()

    def makePDFWeights(self, event):
        if not self.pdfWeightInit: self.initPDFWeights()
        self.pdfWeightTool.processEvent(self.genInfo)
        event.pdfWeights = {}
        for pdf in self.cfg_ana.PDFWeights:
            ws = self.pdfWeightTool.getWeights(pdf+".LHgrid")
            event.pdfWeights[pdf] = [w for w in ws]

    def process(self, event):
        self.readCollections( event.input )

        # if not MC, nothing to do
        if not self.cfg_comp.isMC: 
            return True

        if self.doPDFVars or self.doPDFWeights or self.doLHEWeights:
            self.genInfo = self.mchandles['pdfstuff'].product()
        if self.doPDFWeights:
            self.makePDFWeights(event)
        if self.doPDFVars:
            event.pdf_x1 = self.genInfo.pdf().x.first
            event.pdf_x2 = self.genInfo.pdf().x.second
            event.pdf_id1 = self.genInfo.pdf().id.first
            event.pdf_id2 = self.genInfo.pdf().id.second
            event.pdf_scale = self.genInfo.pdf().scalePDF
        
        if self.doLHEWeights:
            # https://twiki.cern.ch/twiki/bin/view/CMS/LHEReaderCMSSW#How_to_use_weights
            event.LHEWeights  = [] 
            # muR_central    muF= central 
            # muR_central    muF= up 
            # muR_central    muF= down  
            # muR_up     muF=central  
            # muR_up     muF=up       
            # muR_up     muF=down     
            # muR_down   muF=central  
            # muR_down   muF=up       
            # muR_down   muF=down    
            #pass 
            #event.LHEWeights   = self.genInfo.weights()
            for id,w in enumerate(self.genInfo.weights()):
              #print w
              wgt  = WeightsInfo()
              wgt.wgt = w
              #wgt.id  = str( int(id + (1001 if id <= 9 else 2001)) ) 
              #print id, wgt.id, wgt.wgt
              wgt.id = "0"
              event.LHEWeights.append(wgt)

        return True

setattr(PDFWeightsAnalyzer,"defaultConfig",
    cfg.Analyzer(PDFWeightsAnalyzer,
                 PDFWeights = []
    )
)
