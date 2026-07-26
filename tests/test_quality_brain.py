from content_engine.brains.quality_brain import QualityBrain


def test_quality_brain_initializes():

    brain = QualityBrain()

    assert brain is not None


def test_quality_agents_exist():

    brain = QualityBrain()

    assert brain.hook_quality is not None
    assert brain.performance is not None
    assert brain.virality is not None