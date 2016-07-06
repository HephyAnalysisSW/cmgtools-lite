
import PhysicsTools.HeppyCore.framework.config as cfg
#xsec from: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SUSYCrossSections13TeVstopsbottom 
import subprocess
import os.path
#basedir="root://hephyse.oeaw.ac.at//dpm/oeaw.ac.at/home/cms/"
#basedir="root://xrootd.unl.edu//"
#basedir="root://cms-xrd-global.cern.ch/"

#import gfal2

def makePrivateMCComponentFromDPM(name,dataset,dpmdir,subdirs=[''],xSec=1,server= "hephyse.oeaw.ac.at",verbose=False):
    getFilesFunc=makeDPMGetFileListFunction(name, dpmdir, subdirs, server, verbose)

    component = cfg.MCComponent(
        dataset=dataset,
        name = name,
        files = getFilesFunc(), 
        xSection = xSec,
        nGenEvents = 1,
        triggers = [],
        effCorrFactor = 1,
    )
    if verbose:
      print "%s , xSec:%s , dataset: %s " %(name, xSec, dataset)
      print "    Component:", component
    return component


def makeDPMGetFileListFunction(name, dpmdir, subdirs, server, verbose):
    def Func( name=name, dpmdir=dpmdir, subdirs=subdirs,server=server, verbose=verbose  ):
        basedir="root://%s/"%server
        prot="xrd"
        dpmdir = "/cms/"+dpmdir
        lscommand= prot + " " + server + "  ls  " +dpmdir
        print lscommand
        dirs={}
        allfiles=[]
        for subdir in subdirs:
            #gfalout  = subprocess.Popen(["gfal-ls "+ basedir+"/"+dpmdir+'/'+subdir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            lsout = subprocess.Popen([ lscommand ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for f in lsout.stdout.readlines():
                #f = f[:-1]
                #print f
                f =  f.rsplit()
                if len(f)==0:
                    continue
                f=f[-1]
                if not f.endswith("root"):
                    continue
                filepath = basedir +"/" + f
                #print filepath
                allfiles.append( filepath )
        #print "looked for files in :", basedir+"/"+dpmdir+'/'+subdir
        if len(allfiles) == 0:
           raise RuntimeError, "Trying to make a component %s with no files" % name  + "\n Dir: " + basedir+"/"+dpmdir+'/'+subdir+'/'
        return allfiles
    return Func



T2DegStop_300_270 = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_270',                            
                        dataset =  "/T2DegStop_300_270_GEN-SIM/nrad-T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns-4dc17ff0fe241c35c03aa547f2361414/USER" ,
                        dpmdir  =  "/store/user/nrad/T2DegStop_300_270_GEN-SIM/T2DegStop_300_270_MINIAODv2-RunIISpring15-MCRUN2_74_V9-25ns/4dc17ff0fe241c35c03aa547f2361414/"  ,
                        subdirs =[''],
                        xSec    = 8.51615 ,
                    )

T2DegStop_300_240_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_240_FastSim',                            
                        dataset = '/T2DegStop_300_240_FastSim_v3/nrad-T2DegStop_300_240FS-eb69b0448a13fda070ca35fd76ab4e24/USER'  ,
                        dpmdir  = '/store/user/nrad/T2DegStop_300_240_FastSim_v3/T2DegStop_300_240FS/151202_112132/0000/'  ,
                        xSec    = 8.51615,
                    )
T2DegStop_300_270_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_270_FastSim',                            
                        dataset = '/T2DegStop_300_270_FastSim_v3/nrad-T2DegStop_300_270FS-eb69b0448a13fda070ca35fd76ab4e24/USER'  ,
                        dpmdir  = '/store/user/nrad/T2DegStop_300_270_FastSim_v3/T2DegStop_300_270FS/151202_111759/0000/'  ,
                        xSec    = 8.51615,
                    )
T2DegStop_300_290_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2DegStop_300_290_FastSim',                            
                        dataset = '/T2DegStop_300_290_FastSim_v3/nrad-T2DegStop_300_290FS-eb69b0448a13fda070ca35fd76ab4e24/USER'  ,
                        dpmdir  = '/store/user/nrad/T2DegStop_300_290_FastSim_v3/T2DegStop_300_290FS/151202_112032/0000/'   ,
                        xSec    = 8.51615,
                    )
T2tt_300_270_FastSim = makePrivateMCComponentFromDPM(
                        name    = 'T2tt_300_270_FastSim',                            
                        dataset =  '/T2tt_stop300_LSP270/nrad-CMSSW_7_4_4_FastSim_PU25ns_MCRUN2_74_V9_7414_MINIAODv2-eb69b0448a13fda070ca35fd76ab4e24/USER', 
                        dpmdir  =  '/store/user/nrad/T2tt_stop300_LSP270/CMSSW_7_4_4_FastSim_PU25ns_MCRUN2_74_V9_7414_MINIAODv2/160103_194008/0000', 
                        xSec    = 8.51615,
                    )




