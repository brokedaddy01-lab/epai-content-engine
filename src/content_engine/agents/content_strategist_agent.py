from content_engine.agents.trend_scraper_agent import (
    TrendScraperAgent
)

from content_engine.agents.topic_cluster_agent import (
    TopicClusterAgent
)


class ContentStrategistAgent:

    def __init__(self):

        self.trends = (
            TrendScraperAgent()
        )

        self.clusters = (
            TopicClusterAgent()
        )

    def build_strategy(self):

        return {

            "pillars": [

                "discipline",
                "leadership",
                "identity",

                "fitness",

                "entrepreneurship"
            ],

            "trends":

                self.trends.fetch(),

            "clusters":

                self.clusters.clusters()
        }
    