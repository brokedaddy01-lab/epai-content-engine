from content_engine.registry import ManagerRegistry


def test_all_managers_registered():

    registry = ManagerRegistry()

    managers = registry.list_managers()

    assert "strategy" in managers
    assert "creation" in managers
    assert "intelligence" in managers
    assert "quality" in managers
    assert "optimization" in managers
    assert "production" in managers
    assert "publishing" in managers


def test_all_managers_have_health():

    registry = ManagerRegistry()

    health = registry.health()

    for manager in health.values():

        assert manager["status"] == "healthy"


def test_registry_is_singleton():

    first = ManagerRegistry()

    second = ManagerRegistry()

    assert first is second


def test_intelligence_uses_registry_content_memory():

    registry = ManagerRegistry()

    assert (
        registry.managers["intelligence"].content_memory
        is registry.content_memory
    )


def test_brain_forwards_manager_capabilities():

    registry = ManagerRegistry()

    strategy = registry.brain("strategy")

    assert strategy.topic_clusters() == (
        strategy.manager.topic_clusters()
    )


def test_direct_creation_and_intelligence_brains_have_independent_memory():

    from content_engine.brains.creation_brain import CreationBrain
    from content_engine.brains.intelligence_brain import IntelligenceBrain

    creation = CreationBrain()
    intelligence = IntelligenceBrain()

    assert (
        creation.manager.memory
        is not intelligence.manager.content_memory
    )


def test_orchestrator_reuses_director_brains():

    from content_engine.orchestrator import ContentOrchestrator

    orchestrator = ContentOrchestrator()

    assert orchestrator.strategy is orchestrator.director.strategy

    assert orchestrator.creation is orchestrator.director.creation

    assert (
        orchestrator.intelligence
        is orchestrator.director.intelligence
    )

    assert orchestrator.quality is orchestrator.director.quality

    assert (
        orchestrator.optimization
        is orchestrator.director.optimization
    )

    assert (
        orchestrator.production
        is orchestrator.director.production
    )

    assert (
        orchestrator.publishing
        is orchestrator.director.publishing
    )