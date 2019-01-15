from CRABClient.UserUtilities import config, getUsernameFromSiteDB
import sys
config = config()

submitVersion ="2019_1_15"

doEleTree = 'doEleID=True'
doPhoTree = 'doPhoID=True'
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


    ##### now submit DATA
    config.Data.outLFNDirBase = '%s/%s/' % (mainOutputDir,'data')
    config.Data.splitting     = 'LumiBased'
    config.Data.lumiMask      = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/Final/Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'
    config.Data.unitsPerJob   = 90
    config.JobType.pyCfgParams  = ['isMC=False','isAOD=True',doEleTree,doPhoTree,doHLTTree,doRECO,'GT=94X_dataRun2_ReReco_EOY17_v6']

#    config.General.requestName  = 'RunB_2017'
#    config.Data.inputDataset    = '/SingleElectron/Run2017B-17Nov2017-v1/AOD'
#    submit(config)

    config.General.requestName  = 'RunC_2017_retry'
    config.Data.inputDataset    = '/SingleElectron/Run2017C-17Nov2017-v1/AOD'
    submit(config)

#    config.General.requestName  = 'RunD_2017'
#    config.Data.inputDataset    = '/SingleElectron/Run2017D-17Nov2017-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunE_2017_retry'
#    config.Data.inputDataset    = '/SingleElectron/Run2017E-17Nov2017-v1/AOD'
#    submit(config)

#    config.General.requestName  = 'RunF_2017'
#    config.Data.inputDataset    = '/SingleElectron/Run2017F-17Nov2017-v1/AOD'
#    submit(config)




    
