from content_engine.agents.memory_agent import (
    MemoryAgent
)


class FeedbackAgent:

    def __init__(self):

        self.memory = (
            MemoryAgent()
        )

    def learn(

        self,

        review,

        row
    ):

        if review.get(
            "score",
            100
        ) < 80:

            self.memory.remember_failure(

                row[
                    "hook"
                ]
            )

        else:

            self.memory.remember_success(

                hook=row[
                    "hook"
                ],

                topic=row[
                    "topic"
                ]
            )