from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)


class FeedbackAgent:


    def __init__(self):

        self.memory = ContentMemoryManager()



    ##################################################
    # LEARN FROM CONTENT REVIEW
    ##################################################

    def learn(

        self,

        review,

        row

    ):


        score = (

            review.get(

                "score",

                100

            )

        )


        hook = (

            row.get(

                "hook",

                ""

            )

        )


        topic = (

            row.get(

                "topic",

                ""

            )

        )



        if score < 80:


            self.memory.remember_failure(

                hook

            )


        else:


            self.memory.remember_success(

                hook=hook,

                topic=topic,

                hashtags=row.get(

                    "hashtags",

                    []

                ),

                cta=row.get(

                    "cta",

                    ""

                ),

                platform=row.get(

                    "platform",

                    ""

                ),

                score=score

            )