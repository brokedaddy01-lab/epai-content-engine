from content_engine.agents.optimization.optimization_manager import (
    OptimizationManager
)


class OptimizationBrain:


    def __init__(self):


        self.manager = OptimizationManager()



        # Compatibility aliases

        self.growth = (

            self.manager.growth

        )


        self.cta = (

            self.manager.cta

        )


        self.hashtags = (

            self.manager.hashtags

        )



    ##################################################
    # FULL OPTIMIZATION
    ##################################################

    def optimize(

        self,

        content,

        platform,

        topic=None

    ):

        return (

            self.manager
            .optimize(

                content,

                platform,

                topic

            )

        )



    ##################################################
    # CTA ONLY
    ##################################################

    def generate_cta(

        self,

        platform

    ):

        return (

            self.manager
            .generate_cta(

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

            self.manager
            .generate_hashtags(

                topic,

                platform

            )

        )