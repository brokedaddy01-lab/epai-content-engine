from content_engine.brains.publishing_brain import PublishingBrain


def test_publishing_brain_initializes():

    brain = PublishingBrain()

    assert brain is not None


def test_publishing_agents_exist():

    brain = PublishingBrain()

    assert brain.campaign is not None
    assert brain.publisher is not None
    assert brain.scheduler is not None