import random

from content_engine.agents.memory_agent import (
    MemoryAgent
)

from content_engine.agents.trend_agent import (
    TrendAgent
)

from content_engine.agents.hook_agent import (
    HookAgent
)


class ContentStrategistAgent:

    def __init__(self):

        self.memory = (
            MemoryAgent()
        )

        self.trends = (
            TrendAgent()
        )

        self.hooks = (
            HookAgent()
        )

    def build_strategy(self):

        memory = (
            self.memory.load()
        )

        topics = (
            self.trends.get_topics()
        )

        return {

            "topic":

                random.choice(
                    topics
                ),

            "hook":

                self.hooks.generate(),

            "avoid":

                memory.get(
                    "rejected_phrases",
                    []
                ),

            "successful_topics":

                memory.get(
                    "successful_topics",
                    []
                ),

            "goal":

                "followers",

            "objective":

                "Grow Protocol X audience"
        }