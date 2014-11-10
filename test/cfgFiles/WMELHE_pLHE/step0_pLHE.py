# Auto generated configuration file
# using:
# Revision: 1.381.2.13
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v
# with command line options: step1 --filein lhe:9204 --mc --eventcontent LHE --datatier GEN --conditions START53_V7C::All --step NONE --python_filename /afs/cern.ch/cms/PPD/PdmV/work/McM/submit/B2G-Summer12pLHE-00001/B2G-Summer12pLHE-00001_1_cfg.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(10)
        )

# Input source
process.source = cms.Source("LHESource",
                                fileNames = cms.untracked.vstring('/store/lhe/9204/8TeV_QDQDTojWjW_800_8_run15973_unweighted_events.lhe',
                                                                          '/store/lhe/9204/8TeV_QDQDTojWjW_800_8_run3874_unweighted_events.lhe')
                            )

process.options = cms.untracked.PSet(

    )

# Production Info
process.configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.381.2.13 $'),
            annotation = cms.untracked.string('step1 nevts:10'),
            name = cms.untracked.string('PyReleaseValidation')
        )

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                         outputCommands = process.LHEEventContent.outputCommands,
                                         fileName = cms.untracked.string('step1_NONE.root'),
                                         dataset = cms.untracked.PSet(
            filterName = cms.untracked.string(''),
                    dataTier = cms.untracked.string('GEN')
                )
                                     )

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7C::All', '')

# Path and EndPath definitions
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.LHEoutput_step)
