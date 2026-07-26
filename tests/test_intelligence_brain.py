from content_engine.brains.intelligence_brain import IntelligenceBrain


def test_intelligence_brain_initializes():

    brain = IntelligenceBrain()

    assert brain is not None


def test_intelligence_agents_exist():

    brain = IntelligenceBrain()

    assert brain.learning is not None
    assert brain.memory is not None
    assert brain.performance is not None