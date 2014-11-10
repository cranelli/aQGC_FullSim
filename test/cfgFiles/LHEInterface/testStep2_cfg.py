#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("Gen")

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring('file:lheEvents.root')
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(100))

process.load("Configuration.StandardSequences.Services_cff")

process.RandomNumberGeneratorService.generator = cms.PSet(
	initialSeed = cms.untracked.uint32(123456789),
	engineName = cms.untracked.string('HepJamesRandom')
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.generator = cms.EDFilter("LHEProducer", #Changed
	eventsToPrint = cms.untracked.uint32(1),

	hadronisation = cms.PSet(
		generator = cms.string('Pythia8'),

		maxEventsToPrint = cms.untracked.int32(1),
		herwigVerbosity = cms.untracked.int32(2),
		pythiaPylistVerbosity = cms.untracked.int32(2),

		parameterSets = cms.vstring(
			'pythiaCMSDefaults'
		),

		pythiaCMSDefaults = cms.vstring(
			'Check:event = off'
		)
	)
)

process.load("Configuration.StandardSequences.Generator_cff")

process.p0 = cms.Path(
	process.generator *
	process.pgen
)

process.load("Configuration.StandardSequences.VtxSmearedNoSmear_cff")

process.genParticles.abortOnUnknownPDGCode = False

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

#process.printList = cms.EDAnalyzer("ParticleListDrawer",
#	src = cms.InputTag("genParticles"),
#	maxEventsToPrint = cms.untracked.int32(1)
#)

#process.printTree = cms.EDAnalyzer("ParticleTreeDrawer",
#	src = cms.InputTag("genParticles"),
#	printP4 = cms.untracked.bool(False),
#	printPtEtaPhi = cms.untracked.bool(False),
#	printVertex = cms.untracked.bool(False), #Changed
#	printStatus = cms.untracked.bool(False),
#	printIndex = cms.untracked.bool(False),
#	status = cms.untracked.vint32(3) #Changed
#)

#process.p = cms.Path(
#	process.printList *
#	process.printTree
#)

#process.printDecay = cms.EDAnalyzer("ParticleDecayDrawer",
#                                    src = cms.InputTag("genParticles"),
#                                    printP4 = cms.untracked.bool(False),
#                                    printPtEtaPhi = cms.untracked.bool(False),
#                                    printVertex = cms.untracked.bool(False)
#                                    )

process.load("Configuration.EventContent.EventContent_cff")

process.GEN = cms.OutputModule("PoolOutputModule",
	process.FEVTSIMEventContent,
	dataset = cms.untracked.PSet(dataTier = cms.untracked.string('GEN')),
	SelectEvents = cms.untracked.PSet(SelectEvents = cms.vstring('p0')),
	fileName = cms.untracked.string('step2Output.root')
)

process.outpath = cms.EndPath(process.GEN)

process.schedule = cms.Schedule(process.p0, process.outpath)
