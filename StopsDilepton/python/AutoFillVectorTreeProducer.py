from PhysicsTools.Heppy.analyzers.core.TreeAnalyzerNumpy import TreeAnalyzerNumpy
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
#from ROOT import TriggerBitChecker
from PhysicsTools.Heppy.analyzers.core.autovars import *
from PhysicsTools.Heppy.analyzers.objects.autophobj  import *


class AutoFillVectorTreeProducer( TreeAnalyzerNumpy ):

    #-----------------------------------
    # BASIC TREE PRODUCER 
    #-----------------------------------
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(AutoFillVectorTreeProducer,self).__init__(cfg_ana, cfg_comp, looperName)

        ## Read whether we want 4-vectors 
        if not getattr(self.cfg_ana, 'saveTLorentzVectors', False):
            fourVectorType.removeVariable("p4")
 
        self.globalObjects = {}
        self.globalVariables = []
        self.collection         = cfg_ana.collection
        self.vector_collections = cfg_ana.vector_collections
        if hasattr(cfg_ana,"globalObjects"):
                self.globalObjects.update(cfg_ana.globalObjects)
        if hasattr(cfg_ana,"globalVariables"):
                self.globalVariables=cfg_ana.globalVariables[:]

    def beginLoop(self, setup) :
        super(AutoFillVectorTreeProducer, self).beginLoop(setup)

    def declareHandles(self):
        super(AutoFillVectorTreeProducer, self).declareHandles()
#        self.handles['TriggerResults'] = AutoHandle( ('TriggerResults','','HLT'), 'edm::TriggerResults' )
        self.mchandles['GenInfo'] = AutoHandle( ('generator','',''), 'GenEventInfoProduct' )
        k,v = self.collection
        if type(v) == tuple and isinstance(v[0], AutoHandle):
            self.handles[k] = v[0]

        for k,v in self.vector_collections:
            if type(v) == tuple and isinstance(v[0], AutoHandle):
                self.handles[k] = v[0]

    def declareCoreVariables(self, tr, isMC):
        """Here we declare the variables that we always want and that are hard-coded"""
        tr.var('run', int, storageType="i")
        tr.var('lumi', int, storageType="i")
        tr.var('evt', int, storageType="l")
        tr.var('isData', int)

        if not isMC:
            tr.var('intLumi', int, storageType="i")

        if isMC:
            ## cross section
            tr.var('xsec', float)
            ## PU weights
            tr.var("puWeight")
            ## number of true interactions
            tr.var("nTrueInt")
            ## generator weight
            tr.var("genWeight")

    def declareVariables(self,setup):
        isMC = self.cfg_comp.isMC 
        tree = self.tree
        self.declareCoreVariables(tree, isMC)

        for v in self.globalVariables:
            v.makeBranch(tree, isMC)
        for o in self.globalObjects.itervalues(): 
            o.makeBranches(tree, isMC)

        k, c = self.collection
        if type(c) == tuple: c = c[-1]
        #c.makeBranchesVector(tree, isMC)
        #def makeBranchesScalar(self,tree,isMC):
        if not isMC and c.objectType.mcOnly: raise RuntimeError("Attempt to declare mcOnly collection but sample is not MC.")
            #tree.var("n"+c.name, int)
        allvars = c.objectType.allVars(isMC)
        for v in allvars:
            h = v.help
            if c.help: h = "%s for %s" % ( h if h else v.name, c.help )
            tree.var("%s_%s" % (c.name, v.name), type=v.type, default=v.default, title=h, filler=v.filler, zipper=v.zipper)

        for k, c in self.vector_collections:
            if type(c) == tuple: c = c[-1]
            c.makeBranchesVector(tree, isMC)
 
    def fillCoreVariables(self, tr, event, isMC):
        """Here we fill the variables that we always want and that are hard-coded"""
        tr.fill('run', event.input.eventAuxiliary().id().run())
        tr.fill('lumi',event.input.eventAuxiliary().id().luminosityBlock())
        tr.fill('evt', event.input.eventAuxiliary().id().event())    
        tr.fill('isData', 0 if isMC else 1)

#       triggerResults = self.handles['TriggerResults'].product()
#       for T,TC in self.triggerBitCheckers:
#           tr.fill("HLT_"+T, TC.check(event.object(), triggerResults))

        if not isMC:
            tr.fill('intLumi', getattr(self.cfg_comp,'intLumi',1.0))

        if isMC:
            ## xsection, if available
            tr.fill('xsec', getattr(self.cfg_comp,'xSection',1.0))
            ## PU weights, check if a PU analyzer actually filled it
            if hasattr(event,"nPU"):
                    tr.fill("nTrueInt", event.nPU)
                    tr.fill("puWeight", event.puWeight)
            else :
                    tr.fill("nTrueInt", -1)
                    tr.fill("puWeight", 1.0)
                
            tr.fill("genWeight", self.mchandles['GenInfo'].product().weight())

    def process(self, event):
        if hasattr(self.cfg_ana,"filter") :    
            if not self.cfg_ana.filter(event) :
                return True #do not stop processing, just filter myself
        self.readCollections( event.input )
        self.fillTree(event)
         
    def fillTree(self, event, resetFirst=True):
        isMC = self.cfg_comp.isMC 
        if resetFirst: self.tree.reset()

        self.fillCoreVariables(self.tree, event, isMC)

        for v in self.globalVariables:
            if not isMC and v.mcOnly: continue
            v.fillBranch(self.tree, event, isMC)

        for on, o in self.globalObjects.iteritems(): 
            if not isMC and o.mcOnly: continue
            o.fillBranches(self.tree, getattr(event, on), isMC)

        cn, c  = self.collection
        #if type(c) == tuple and isinstance(c[0], AutoHandle):
        #    print "Hello"
        #    if not isMC and c[-1].mcOnly: raise RuntimeError("Attempt to fill mcOnly collection but sample is not MC.")  
        #    objects = self.handles[cn].product()
        #    setattr(event, cn, [objects[i] for i in xrange(objects.size())])
        #    c = c[-1]
            #if not isMC and c.mcOnly: 
            #c.fillBranchesScalar(self.tree, getattr(event, cn), isMC)
            #def fillBranchesScalar(self,treeNumpy,collection,isMC):
        collection = getattr(event, cn)
        if not isMC and c.objectType.mcOnly: return
        if c.filter != None: collection = [ o for o in collection if c.filter(o) ]
        if c.sortAscendingBy != None: collection  = sorted(collection, key=c.sortAscendingBy)
        if c.sortDescendingBy != None: collection = sorted(collection, key=c.sortDescendingBy, reverse=True)
        num = min(c.maxlen,len(collection))
        #tree.fill("n"+c.name, num)
        allvars = c.objectType.allVars(isMC)
        for i in xrange(num):
            o = collection[i]

            for v_cn, v_c in self.vector_collections:
                if type(v_c) == tuple and isinstance(v_c[0], AutoHandle):
                    #if not isMC and v_c[-1].mcOnly: continue
                    objects = getattr( v, v_cn ) if hasattr(v, v_cn ) else getattr( event, v_cn ) 
                    #setattr(event, v_cn, [objects[i] for i in xrange(objects.size())])
                    v_c = v_c[-1]
                if not isMC and v_c.mcOnly: v_continue
                v_c.fillBranchesVector(self.tree, getattr(event, v_cn) if hasattr(event, v_cn) else getattr(o, v_cn), isMC)

            for v in allvars:
                self.tree.fill("%s_%s" % (c.name, v.name), v(o))

            self.tree.tree.Fill()      
   


 
    def getPythonWrapper(self):
        """
        This function produces a string that contains a Python wrapper for the event.
        The wrapper is automatically generated based on the collections and allows the full
        event contents to be accessed from subsequent Analyzers using e.g.
        
        leps = event.selLeptons #is of type selLeptons
        pt0 = leps[0].pt

        One just needs to add the EventAnalyzer to the sequence.
        """

        isMC = self.cfg_comp.isMC 

        classes = ""
        anclass = ""
        anclass += "from PhysicsTools.HeppyCore.framework.analyzer import Analyzer\n"
        anclass += "class EventAnalyzer(Analyzer):\n"
        anclass += "    def __init__(self, cfg_ana, cfg_comp, looperName):\n"
        anclass += "        super(EventAnalyzer, self).__init__(cfg_ana, cfg_comp, looperName)\n"

        anclass += "    def process(self, event):\n"

        cname, coll  = self.collection
        classes += coll.get_py_wrapper_class(isMC)
        anclass += "        event.{0} = {0}.make_array(event)\n".format(coll.name)
        
        return classes + "\n" + anclass

