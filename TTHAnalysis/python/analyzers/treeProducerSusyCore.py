from PhysicsTools.Heppy.analyzers.core.AutoFillTreeProducer  import * 

susyCore_globalVariables = [
            NTupleVariable("rho",  lambda ev: ev.rho, float, help="kt6PFJets rho"),
            NTupleVariable("rhoCN",  lambda ev: ev.rhoCN, float, help="fixed grid rho central neutral"),
            NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"), 

            NTupleVariable("GenSusyMScan1", lambda ev : ev.genSusyMScan1, int, mcOnly=True, help="Susy mass 1 in scan"),
            NTupleVariable("GenSusyMScan2", lambda ev : ev.genSusyMScan2, int, mcOnly=True, help="Susy mass 2 in scan"),
            NTupleVariable("GenSusyMScan3", lambda ev : ev.genSusyMScan3, int, mcOnly=True, help="Susy mass 3 in scan"),
            NTupleVariable("GenSusyMScan4", lambda ev : ev.genSusyMScan4, int, mcOnly=True, help="Susy mass 4 in scan"),
            NTupleVariable("GenSusyMGluino", lambda ev : ev.genSusyMGluino, int, mcOnly=True, help="Susy Gluino mass"),
            NTupleVariable("GenSusyMGravitino", lambda ev : ev.genSusyMGravitino, int, mcOnly=True, help="Susy Gravitino mass"),
            NTupleVariable("GenSusyMStop", lambda ev : ev.genSusyMStop, int, mcOnly=True, help="Susy Stop mass"),
            NTupleVariable("GenSusyMSbottom", lambda ev : ev.genSusyMSbottom, int, mcOnly=True, help="Susy Sbottom mass"),
            NTupleVariable("GenSusyMStop2", lambda ev : ev.genSusyMStop2, int, mcOnly=True, help="Susy Stop2 mass"),
            NTupleVariable("GenSusyMSbottom2", lambda ev : ev.genSusyMSbottom2, int, mcOnly=True, help="Susy Sbottom2 mass"),
            NTupleVariable("GenSusyMSquark", lambda ev : ev.genSusyMSquark, int, mcOnly=True, help="Susy Squark mass"),
            NTupleVariable("GenSusyMNeutralino", lambda ev : ev.genSusyMNeutralino, int, mcOnly=True, help="Susy Neutralino mass"),
            NTupleVariable("GenSusyMNeutralino2", lambda ev : ev.genSusyMNeutralino2, int, mcOnly=True, help="Susy Neutralino2 mass"),
            NTupleVariable("GenSusyMNeutralino3", lambda ev : ev.genSusyMNeutralino3, int, mcOnly=True, help="Susy Neutralino3 mass"),
            NTupleVariable("GenSusyMNeutralino4", lambda ev : ev.genSusyMNeutralino4, int, mcOnly=True, help="Susy Neutralino4 mass"),
            NTupleVariable("GenSusyMChargino", lambda ev : ev.genSusyMChargino, int, mcOnly=True, help="Susy Chargino mass"),
            NTupleVariable("GenSusyMChargino2", lambda ev : ev.genSusyMChargino2, int, mcOnly=True, help="Susy Chargino2 mass"),
]

susyCore_globalObjects = {
            "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after type 1 corrections"),
}

susyCore_collections = {
            "genleps"         : NTupleCollection("genLep",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays"),                                                                                                
            "gentauleps"      : NTupleCollection("genLepFromTau", genParticleWithLinksType, 10, help="Generated leptons (e/mu) from decays of taus from W/Z/h decays"),                                                                       
            "gentaus"         : NTupleCollection("genTau",     genParticleWithLinksType, 10, help="Generated leptons (tau) from W/Z decays"),                            
            "generatorSummary" : NTupleCollection("GenPart", genParticleWithLinksType, 100 , help="Hard scattering particles, with ancestry and links"),
}
