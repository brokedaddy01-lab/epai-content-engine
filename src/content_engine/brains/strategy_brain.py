from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.strategy.strategy_manager import (
    StrategyManager
)


class StrategyBrain(BaseBrain):


    manager_class = StrategyManager



    ##################################################
    # HOOK GENERATION
    ##################################################

    def generate_hook(

        self,

        topic

    ):

        return self.manager.generate_hook(

            topic

        )



    ##################################################
    # SEO OPTIMIZATION
    ##################################################

    def optimize_content(

        self,

        content,

        keyword

    ):

        return self.manager.optimize_content(

            content,

            keyword

        )



    ##################################################
    # TREND INTELLIGENCE
    ##################################################

    def discover_trends(

        self,

        source_data=None

    ):

        return self.manager.discover_trends(

            source_data

        )



    def trend_summary(

        self,

        source_data=None

    ):

        return self.manager.trend_summary(

            source_data

        )



    ##################################################
    # TOPIC CLUSTERS
    ##################################################

    def topic_clusters(

        self

    ):

        return self.manager.topic_clusters()