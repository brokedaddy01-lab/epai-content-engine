from content_engine.brains.strategy_brain import (
    StrategyBrain
)


def test_strategy_agents_exist():

    brain = StrategyBrain()

    assert brain.audience is not None

    assert brain.strategist is not None

    assert brain.hooks is not None

    assert brain.seo is not None

    assert brain.clusters is not None

    assert brain.trends is not None