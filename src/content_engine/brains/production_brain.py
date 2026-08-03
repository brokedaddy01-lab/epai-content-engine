from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.models.content_context import (
    ContentContext
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

        platform=None,

        topic=None

    ):

        if isinstance(

            content,

            ContentContext

        ):

            context = content

            return self.manager.generate_assets(

                context.content,

                context.platform,

                context.topic

            )


        return self.manager.generate_assets(

            content,

            platform,

            topic

        )