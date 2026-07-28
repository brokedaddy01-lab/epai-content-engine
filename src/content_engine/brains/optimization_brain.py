from content_engine.agents.optimization.growth_agent import (
    GrowthAgent
)

from content_engine.agents.optimization.cta_agent import (
    CTAAgent
)

from content_engine.agents.optimization.hashtag_agent import (
    HashtagAgent
)


class OptimizationBrain:


    def __init__(self):

        self.growth = GrowthAgent()

        self.cta = CTAAgent()

        self.hashtags = HashtagAgent()



    ##################################################
    # FULL OPTIMIZATION
    ##################################################

    def optimize(

        self,

        content,

        platform,

        topic=None

    ):


        growth = (

            self.growth
            .optimize(

                content,

                platform

            )

        )


        cta = (

            self.cta
            .generate(

                platform

            )

        )


        hashtags = (

            self.hashtags
            .generate(

                topic or "",

                platform

            )

        )


        return {


            "follow_cta":

                cta,


            "hashtags":

                hashtags,


            "growth":

                growth

        }



    ##################################################
    # CTA ONLY
    ##################################################

    def generate_cta(

        self,

        platform

    ):

        return (

            self.cta
            .generate(

                platform

            )

        )



    ##################################################
    # HASHTAGS ONLY
    ##################################################

    def generate_hashtags(

        self,

        topic,

        platform

    ):

        return (

            self.hashtags
            .generate(

                topic,

                platform

            )

        )