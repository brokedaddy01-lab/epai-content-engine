from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.strategy.strategy_manager import (
    StrategyManager
)


class StrategyBrain(BaseBrain):

    manager_class = StrategyManager