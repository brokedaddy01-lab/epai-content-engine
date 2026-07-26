from content_engine.brains.creation_brain import CreationBrain


def test_creation_brain_initializes():

    brain = CreationBrain()

    assert brain is not None


def test_creation_brain_has_agents():

    brain = CreationBrain()

    assert brain.prompt_architect is not None
    assert brain.copywriter is not None
    assert brain.reviewer is not None