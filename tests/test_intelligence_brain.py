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