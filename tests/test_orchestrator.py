from content_engine.orchestrator import ContentOrchestrator


def test_orchestrator_initializes():

    orchestrator = ContentOrchestrator()

    assert orchestrator is not None


def test_orchestrator_has_all_brains():

    orchestrator = ContentOrchestrator()

    assert orchestrator.strategy is not None
    assert orchestrator.creation is not None
    assert orchestrator.intelligence is not None
    assert orchestrator.quality is not None
    assert orchestrator.optimization is not None
    assert orchestrator.production is not None
    assert orchestrator.publishing is not None


def test_orchestrator_reuses_director_brains():

    orchestrator = ContentOrchestrator()

    assert orchestrator.strategy is orchestrator.director.strategy
    assert orchestrator.creation is orchestrator.director.creation
    assert orchestrator.intelligence is orchestrator.director.intelligence
    assert orchestrator.quality is orchestrator.director.quality
    assert orchestrator.optimization is orchestrator.director.optimization
    assert orchestrator.production is orchestrator.director.production
    assert orchestrator.publishing is orchestrator.director.publishing