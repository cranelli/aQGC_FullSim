# Auto generated configuration file
# using:
# Revision: 1.381.2.13
# Source: /local/reps/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v
# with command line options: Configuration/GenProduction/python/EightTeV/LNuGG_enhanced_ISR_8TeV_madgraph_cff.py -s LHE --conditions START53_V7C::All --datatier GEN --eventcontent LHE --python_filename /afs/cern.ch/cms/CAF/CMSPHYS/PHYS_GENERATOR/prep/Summer12_WMLHE-20130517122229_1/config_12_1_cfg.py --fileout step1.root --no_exec -n 50000
import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(50000)
        )

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

    )

# Production Info
process.configurationMetadata = cms.untracked.PSet(
        version = cms.untracked.string('$Revision: 1.381.2.13 $'),
            annotation = cms.untracked.string('Configuration/GenProduction/python/EightTeV/LNuGG_enhanced_ISR_8TeV_madgraph_cff.py nevts:50000'),
            name = cms.untracked.string('PyReleaseValidation')
        )

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
                                         splitLevel = cms.untracked.int32(0),
                                         eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                         outputCommands = process.LHEEventContent.outputCommands,
                                         fileName = cms.untracked.string('step1.root'),
                                         dataset = cms.untracked.PSet(
            filterName = cms.untracked.string(''),
                    dataTier = cms.untracked.string('GEN')
                )
                                     )

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'START53_V7C::All', '')

process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
                                                 nEvents = cms.uint32(50000),
                                                 args = cms.vstring('slc5_ia32_gcc434/madgraph/V5_1.4.8/8TeV_Summer12/Waa_enhanced_ISR_madgraph/v4',
                                                                            'ppWaa_enhanced_ISR',
                                                                            'false',
                                                                            'false',
                                                                            'wjets',
                                                                            '5',
                                                                            '20',
                                                                            'true',
                                                                            '0',
                                                                            '1'),
                                                 scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_madgraph_gridpack.sh'),
                                                 numberOfParameters = cms.uint32(10),
                                                 outputFile = cms.string('ppWaa_enhanced_ISR_final.lhe')
                                             )


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.endjob_step,process.LHEoutput_step)
