from content_engine.agents.strategy.audience_agent import (
    AudienceAgent
)

from content_engine.agents.strategy.content_strategist_agent import (
    ContentStrategistAgent
)

from content_engine.agents.strategy.hook_agent import (
    HookAgent
)

from content_engine.agents.strategy.seo_agent import (
    SEOAgent
)

from content_engine.agents.strategy.topic_cluster_agent import (
    TopicClusterAgent
)

from content_engine.agents.strategy.trend_agent import (
    TrendAgent
)

from content_engine.agents.base_manager import BaseManager

class StrategyManager(BaseManager):


    def __init__(self):

        self.audience = AudienceAgent()

        self.strategist = ContentStrategistAgent()

        self.hooks = HookAgent()

        self.seo = SEOAgent()

        self.clusters = TopicClusterAgent()

        self.trends = TrendAgent()



    ##################################################
    # HOOK GENERATION
    ##################################################

    def generate_hook(
        self,
        topic
    ):

        return self.hooks.generate(
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

        return self.seo.optimize(
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

        return self.trends.analyze(
            source_data
        )



    def trend_summary(
        self,
        source_data=None
    ):

        return self.trends.prioritize(
            source_data
        )



    ##################################################
    # TOPIC CLUSTERS
    ##################################################

    def topic_clusters(self):

        return self.clusters
