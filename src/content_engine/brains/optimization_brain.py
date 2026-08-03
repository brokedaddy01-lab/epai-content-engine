from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.models.content_context import (
    ContentContext
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

        platform=None,

        topic=None

    ):

        if isinstance(
            content,
            ContentContext
        ):

            context = content

            return self.manager.optimize(

                context.content,

                context.platform,

                context.topic

            )


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