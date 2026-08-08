from content_engine.brains.intelligence_brain import (
    IntelligenceBrain
)


def test_intelligence_agents_exist():

    brain = IntelligenceBrain()

    assert brain.performance is not None

    assert brain.performance_learning is not None

    assert brain.memory is not None

    assert brain.feedback is not None

    assert brain.feedback_loop is not None

    assert brain.knowledge is not None

    assert brain.clusters is not None


def test_intelligence_compatibility_aliases_reference_manager_components():

    brain = IntelligenceBrain()

    assert brain.content_memory is brain.manager.content_memory

    assert brain.memory is brain.manager.memory

    assert brain.feedback is brain.manager.feedback

    assert brain.feedback_loop is brain.manager.feedback

    assert brain.performance is brain.manager.performance

    assert brain.performance_learning is brain.manager.learning

    assert brain.learning is brain.manager.learning

    assert brain.knowledge is brain.manager.knowledge

    assert brain.clusters is brain.manager.knowledge