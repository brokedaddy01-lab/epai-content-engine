from content_engine.agents.strategy.strategy_manager import (
    StrategyManager
)


class StrategyBrain:


    def __init__(
        self,
        manager=None
    ):

        self.manager = (

            manager

            if manager is not None

            else StrategyManager()

        )


        # Compatibility aliases

        self.audience = self.manager.audience

        self.strategist = self.manager.strategist

        self.hooks = self.manager.hooks

        self.seo = self.manager.seo

        self.clusters = self.manager.clusters

        self.trends = self.manager.trends



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
    # SEO
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

    def topic_clusters(self):

        return self.manager.topic_clusters()



    ##################################################
    # STRATEGY ACCESS
    ##################################################

    def strategy_agent(self):

        return self.manager.strategy_agent()



    ##################################################
    # AUDIENCE ACCESS
    ##################################################

    def audience_agent(self):

        return self.manager.audience_agent()