from content_engine.agents.asset_production.asset_production_manager import (
    AssetProductionManager
)


class ProductionBrain:


    def __init__(

        self,

        manager=None

    ):


        self.assets = (

            manager

            if manager

            else AssetProductionManager()

        )


        # Compatibility aliases.
        # Asset ownership moved to AssetProductionManager,
        # but older callers/tests still access ProductionBrain agents directly.

        self.formatter = self.assets.formatter

        self.image = self.assets.image

        self.video = self.assets.video

        self.carousel = self.assets.carousel

        self.newsletter = self.assets.newsletter

        self.thumbnail = self.assets.thumbnail

        self.repurpose = self.assets.repurpose

        self.podcast = self.assets.podcast

        self.youtube_title = self.assets.youtube_title

        self.youtube_description = self.assets.youtube_description



    ##################################################
    # ASSET GENERATION
    ##################################################

    def generate_assets(

        self,

        content,

        platform,

        topic

    ):

        return self.assets.generate_assets(

            content,

            platform,

            topic

        )