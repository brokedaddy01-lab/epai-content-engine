from content_engine.agents.strategy.strategy_manager import (
    StrategyManager
)

from content_engine.agents.intelligence.intelligence_manager import (
    IntelligenceManager
)

from content_engine.agents.creation.creation_manager import (
    CreationManager
)

from content_engine.agents.optimization.optimization_manager import (
    OptimizationManager
)

from content_engine.agents.asset_production.asset_production_manager import (
    AssetProductionManager
)

from content_engine.agents.publishing.publishing_manager import (
    PublishingManager
)

from content_engine.agents.quality.quality_manager import (
    QualityManager
)



class ManagerRegistry:


    def __init__(self):

        self.managers = {

            "strategy":
                StrategyManager(),

            "intelligence":
                IntelligenceManager(),

            "creation":
                CreationManager(),

            "optimization":
                OptimizationManager(),

            "production":
                AssetProductionManager(),

            "publishing":
                PublishingManager(),

            "quality":
                QualityManager()

        }



    ##################################################
    # ACCESS
    ##################################################

    def get(
        self,
        name
    ):

        return self.managers.get(
            name
        )



    ##################################################
    # DISCOVERY
    ##################################################

    def list_managers(
        self
    ):

        return list(
            self.managers.keys()
        )



    ##################################################
    # HEALTH
    ##################################################

    def health(
        self
    ):

        return {

            name:
                manager.health()

            for name, manager
            in self.managers.items()

        }



    ##################################################
    # INFO
    ##################################################

    def info(
        self
    ):

        return {

            name:
                manager.info()

            for name, manager
            in self.managers.items()

        }