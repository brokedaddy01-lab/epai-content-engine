from content_engine.brains.strategy_brain import StrategyBrain


def test_strategy_brain_initializes():

    brain = StrategyBrain()

    assert brain is not None


def test_strategy_agents_exist():

    brain = StrategyBrain()

    assert brain.audience is not None
    assert brain.planner is not None
    assert brain.hooks is not None