from content_engine.brains.quality_brain import QualityBrain


def test_quality_brain_initializes():

    brain = QualityBrain()

    assert brain is not None

    assert brain.manager is not None


def test_quality_manager_exists():

    brain = QualityBrain()

    assert brain.manager is not None