from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.optimization.optimization_manager import (
    OptimizationManager
)


class OptimizationBrain(BaseBrain):


    manager_class = OptimizationManager



    ##################################################
    # FULL OPTIMIZATION
    ##################################################

    def optimize(

        self,

        content,

        platform,

        topic=None

    ):

        return self.manager.optimize(

            content,

            platform,

            topic

        )



    ##################################################
    # CTA ONLY
    ##################################################

    def generate_cta(

        self,

        platform

    ):

        return self.manager.generate_cta(

            platform

        )



    ##################################################
    # HASHTAGS ONLY
    ##################################################

    def generate_hashtags(

        self,

        topic,

        platform

    ):

        return self.manager.generate_hashtags(

            topic,

            platform

        )