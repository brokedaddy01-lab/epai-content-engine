from content_engine.brains.production_brain import ProductionBrain


def test_production_brain_initializes():

    brain = ProductionBrain()

    assert brain is not None


def test_production_agents_exist():

    brain = ProductionBrain()

    assert brain.formatter is not None
    assert brain.image is not None
    assert brain.video is not None
    assert brain.carousel is not None
    assert brain.newsletter is not None
    assert brain.thumbnail is not None
    assert brain.repurpose is not None
    assert brain.podcast is not None
    assert brain.youtube_title is not None
    assert brain.youtube_description is not None


def test_generate_assets_returns_complete_package():

    brain = ProductionBrain()

    assets = brain.generate_assets(
        content="Discipline creates freedom.",
        platform="facebook",
        topic="discipline"
    )

    assert "formatted" in assets
    assert "image_prompt" in assets
    assert "video_script" in assets
    assert "newsletter" in assets
    assert "carousel" in assets
    assert "thumbnail" in assets
    assert "repurposed" in assets
    assert "podcast" in assets
    assert "youtube_title" in assets
    assert "youtube_description" in assets