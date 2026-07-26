from content_engine.brains.optimization_brain import OptimizationBrain


def test_optimization_brain_initializes():

    brain = OptimizationBrain()

    assert brain is not None


def test_optimization_agents_exist():

    brain = OptimizationBrain()

    assert brain.growth is not None
    assert brain.cta is not None
    assert brain.hashtags is not None