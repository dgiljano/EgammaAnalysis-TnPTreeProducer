from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

submitVersion ="2019_1_15"

doEleTree = 'doEleID=True'
doPhoTree = 'doPhoID=False'
doHLTTree = 'doTrigger=False'
doRECO    = 'doRECO=False'

mainOutputDir = '/store/user/dgiljano/TnP/2017_data_MC/%s' % submitVersion

config.General.transferLogs = False

config.JobType.pluginName  = 'Analysis'

# Name of the CMSSW configuration file
config.JobType.psetName  = '/scratch/giljanovic/CMSSW_10_2_9/src/EgammaAnalysis/TnPTreeProducer/python/TnPTreeProducer_cfg.py'
config.Data.allowNonValidInputDataset = False

config.Data.inputDBS = 'global'
config.Data.publication = False

#config.Data.publishDataName = 
config.Site.storageSite = 'T2_FR_GRIF_LLR'

config.JobType.allowUndistributedCMSSW = True

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea = 'crab_%s' % submitVersion

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)


    ##### submit MC
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'mc')
    config.Data.splitting     = 'FileBased'
    config.Data.unitsPerJob   = 20
    config.JobType.pyCfgParams  = ['isMC=True','isAOD=False',doEleTree,doPhoTree,doHLTTree,doRECO]


    config.General.requestName  = 'DY1JetsToLL_M50_madgraphMLM'
    config.Data.inputDataset    = '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-PU2017-94X_mc2017_realistic_v11-v1/MINIAODSIM'
    submit(config) 

    config.General.requestName  = 'DY1JetsToLL_M50_madgraphMLM_ext1'
    config.Data.inputDataset    = '/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-PU2017_94X_mc2017_realistic_v11_ext1-v1/MINIAODSIM'
    submit(config) 

    config.General.requestName  = 'DYJetsToLL_M50_amcatnloFXFX'
#    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17DRPremix-PU2017_94X_mc2017_realistic_v11-v1/AODSIM'
    config.Data.inputDataset    = '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM'
    submit(config) 



    
