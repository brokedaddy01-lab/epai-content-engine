from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.asset_production.asset_production_manager import (
    AssetProductionManager
)


class ProductionBrain(BaseBrain):


    manager_class = AssetProductionManager



    ##################################################
    # ASSET GENERATION
    ##################################################

    def generate_assets(

        self,

        content,

        platform,

        topic

    ):

        return self.manager.generate_assets(

            content,

            platform,

            topic

        )