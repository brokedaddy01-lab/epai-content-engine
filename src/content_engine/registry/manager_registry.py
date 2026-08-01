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


from content_engine.brains.strategy_brain import (
    StrategyBrain
)

from content_engine.brains.intelligence_brain import (
    IntelligenceBrain
)

from content_engine.brains.creation_brain import (
    CreationBrain
)

from content_engine.brains.optimization_brain import (
    OptimizationBrain
)

from content_engine.brains.production_brain import (
    ProductionBrain
)

from content_engine.brains.publishing_brain import (
    PublishingBrain
)

from content_engine.brains.quality_brain import (
    QualityBrain
)



class ManagerRegistry:


    _instance = None



    def __new__(cls):

        if cls._instance is None:

            cls._instance = super(
                ManagerRegistry,
                cls
            ).__new__(
                cls
            )

            cls._instance._initialize()


        return cls._instance



    def _initialize(self):

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
    # MANAGER ACCESS
    ##################################################

    def get(

        self,

        name

    ):

        return self.managers.get(

            name

        )



    ##################################################
    # BRAIN FACTORY
    ##################################################

    def brain(

        self,

        name

    ):

        brains = {

            "strategy":
                StrategyBrain,

            "intelligence":
                IntelligenceBrain,

            "creation":
                CreationBrain,

            "optimization":
                OptimizationBrain,

            "production":
                ProductionBrain,

            "publishing":
                PublishingBrain,

            "quality":
                QualityBrain

        }


        brain_class = brains.get(

            name

        )


        if brain_class is None:

            raise ValueError(

                f"Unknown brain: {name}"

            )


        return brain_class(

            self.get(

                name

            )

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