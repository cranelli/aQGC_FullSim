# Auto generated configuration file
# using: 
# Revision: 1.381.2.28 
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: step0 --conditions auto:startup -s NONE --eventcontent RAWSIM --datatier GEN --filein file:SM_LNuAA.lhe --fileout file:SM_LNuAA_Gen.root --no_exec --mc
import FWCore.ParameterSet.Config as cms
import SplittingInfo 
process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
# Input source
print SplittingInfo.LISTEVENTRANGES[0]
process.source = cms.Source("PoolSource",
                            secondaryFileNames = cms.untracked.vstring(),
                            fileNames = cms.untracked.vstring('file:../reweighted_events_step0.root'),
                            eventsToProcess = cms.untracked.VEventRange(SplittingInfo.LISTEVENTRANGES[0])
                            )


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.381.2.28 $'),
    annotation = cms.untracked.string('step_SplitEvents nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
                                        splitLevel = cms.untracked.int32(0),
                                        eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                        outputCommands = process.RAWSIMEventContent.outputCommands,
                                        fileName = cms.untracked.string('file:../RootFiles/SplitEDMFiles/'
                                                                        'reweighted_events_step0_part1.root'),
                                        dataset = cms.untracked.PSet(
    filterName = cms.untracked.string(''),
    dataTier = cms.untracked.string('GEN')
    )
)

# Additional output definition

# Other statements
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')

# Path and EndPath definitions
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.RAWSIMoutput_step)

