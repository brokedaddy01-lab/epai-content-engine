from content_engine.agents.content_strategist_agent import (
    ContentStrategistAgent
)

from content_engine.agents.trend_scraper_agent import (
    TrendScraperAgent
)

from content_engine.agents.hook_agent import (
    HookAgent
)

from content_engine.agents.seo_agent import (
    SEOAgent
)


class ContentDirectorAgent:

    def __init__(self):

        self.strategist = (
            ContentStrategistAgent()
        )

        self.trends = (
            TrendScraperAgent()
        )

        self.hooks = (
            HookAgent()
        )

        self.seo = (
            SEOAgent()
        )

    def plan(

        self,
        row
    ):

        return {

            "strategy":

                self.strategist
                .build_strategy(),

            "trends":

                self.trends.fetch(),

            "hooks":

                self.hooks.generate(
                    row["topic"]
                ),

            "seo":

                self.seo.optimize(

                    "",

                    row["keyword"]
                )
        }