from content_engine.agents.strategy.audience_agent import (
    AudienceAgent
)

from content_engine.agents.strategy.content_planner_agent import (
    ContentPlannerAgent
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

from content_engine.agents.strategy.trend_scraper_agent import (
    TrendScraperAgent
)



class StrategyBrain:


    def __init__(self):

        self.audience = AudienceAgent()

        self.planner = ContentPlannerAgent()

        self.strategist = ContentStrategistAgent()

        self.hooks = HookAgent()

        self.seo = SEOAgent()

        self.clusters = TopicClusterAgent()

        self.trends = TrendAgent()

        self.trend_scraper = TrendScraperAgent()



    ##################################################
    # MONTHLY CONTENT PLAN
    ##################################################

    def create_plan(self):

        return (

            self.planner
            .monthly_plan()

        )



    ##################################################
    # HOOK GENERATION
    ##################################################

    def generate_hook(

        self,
        topic

    ):

        return (

            self.hooks
            .generate(

                topic

            )

        )



    ##################################################
    # SEO OPTIMIZATION
    ##################################################

    def optimize_content(

        self,
        content,
        keyword

    ):

        return (

            self.seo
            .optimize(

                content,

                keyword

            )

        )



    ##################################################
    # TREND DISCOVERY
    ##################################################

    def discover_trends(self):

        return (

            self.trend_scraper
            .fetch()

        )



    ##################################################
    # TOPIC CLUSTERS
    ##################################################

    def topic_clusters(self):

        return self.clusters



    ##################################################
    # STRATEGY ACCESS
    ##################################################

    def strategy_agent(self):

        return self.strategist



    ##################################################
    # AUDIENCE ACCESS
    ##################################################

    def audience_agent(self):

        return self.audience