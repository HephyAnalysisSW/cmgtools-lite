import PhysicsTools.HeppyCore.framework.config as cfg
import subprocess
import os.path

from RootTools.fwlite.Database import Database

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
        dirs={}
        allfiles=[]
        cache = Database("signal_cache.db", "fileCache", ["name"])
        nFiles = cache.contains({'name':name})
        if nFiles:
            print 'Found sample in cache, adding %i file'%nFiles
            files = cache.getDicts({'name':name})
            for f in files:
                allfiles.append(f["value"])
        else:
            for subdir in subdirs:
                #gfalout  = subprocess.Popen(["gfal-ls "+ basedir+"/"+dpmdir+'/'+subdir ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                lsout = subprocess.Popen([ lscommand ], shell = True , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for f in lsout.stdout.readlines():
                    f =  f.rsplit()
                    if len(f)==0:
                        continue
                    f=f[-1]
                    if not f.endswith("root"):
                        continue
                    filepath = basedir +"/" + f
                    allfiles.append( filepath )
                    cache.add({"name":name}, filepath, save=True)
        #print "looked for files in :", basedir+"/"+dpmdir+'/'+subdir
        if len(allfiles) == 0:
           raise RuntimeError, "Trying to make a component %s with no files" % name  + "\n Dir: " + basedir+"/"+dpmdir+'/'+subdir+'/'
        return allfiles
    return Func

TTZToLLNuNuXsec = 0.2728

ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000',
                        dataset =  '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  =  '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000/ewkDM_mAOD/170908_200429/0000',
                        xSec    = 0.8641 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000',
                        dataset =  '/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  =  '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000/ewkDM_mAOD/170908_200353/0000',
                        xSec    = 0.9281 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700/ewkDM_mAOD/170908_200317/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700/ewkDM_mAOD/170908_200242/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700/ewkDM_mAOD/170908_200131/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700/ewkDM_mAOD/170908_200055/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000/ewkDM_mAOD/170908_200206/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000/ewkDM_mAOD/170908_200018/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000/ewkDM_mAOD/170908_195942/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000',
                        dataset = '/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000/ewkDM_mAOD/170908_195905/0000',
                        xSec    =  0.8 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000 = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000',
                        dataset = '/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000/ewkDM_mAOD/170908_195828/0000',
                        xSec    = 1.6832 * TTZToLLNuNuXsec,
                    )

ewkDM_ttZ_ll = makePrivateMCComponentFromDPM(
                        name    = 'ewkDM_ttZ_ll',
                        dataset = '/ewkDM_ttZ_ll/schoef-ewkDM_mAOD-0b8c51c13c712fe6e73a79b549018f23/USER',
                        dpmdir  = '/store/user/schoef/ewkDM_ttZ_ll/ewkDM_mAOD/170908_200504/0000',
                        xSec    = TTZToLLNuNuXsec,
                    )

signalSamples = [\
    ewkDM_ttZ_ll,
    ewkDM_ttZ_ll_DC2A_0p200000_DC2V_0p200000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_m0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2V_0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p250000,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_m0p176700,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_m0p176700_DC2V_0p176700,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_m0p176700,
    ewkDM_ttZ_ll_DC1A_0p600000_DC1V_m0p240000_DC2A_0p176700_DC2V_0p176700,
    ewkDM_ttZ_ll_DC1A_0p500000_DC1V_m1p000000,
    ewkDM_ttZ_ll_DC1A_0p500000_DC1V_0p500000]
