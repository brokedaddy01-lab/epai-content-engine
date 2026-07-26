from content_engine.agents.content_strategist_agent import (
    ContentStrategistAgent
)


class ProtocolXContentDirector:

    def __init__(self):

        self.strategist = (
            ContentStrategistAgent()
        )

    def create_campaign(self):

        strategy = (

            self.strategist
            .build_strategy()
        )

        return {

            "mission":

                "Grow Protocol X into the leading discipline and self mastery brand.",

            "objective":

                "Increase followers, subscribers, and engagement.",

            "strategy":

                strategy
        }