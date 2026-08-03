from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.models.content_context import (
    ContentContext
)

from content_engine.agents.quality.quality_manager import (
    QualityManager
)


class QualityBrain(BaseBrain):


    manager_class = QualityManager



    def analyze(

        self,

        content,

        review=None,

        platform=None

    ):

        if isinstance(

            content,

            ContentContext

        ):

            context = content

            return self.manager.analyze(

                context.content,

                context.metadata.get(
                    "review",
                    {}
                ),

                context.platform

            )


        return self.manager.analyze(

            content,

            review,

            platform

        )



    def score_hook(

        self,

        hook

    ):

        return self.manager.score_hook(

            hook

        )



    def compare_hooks(

        self,

        first,

        second

    ):

        return self.manager.compare_hooks(

            first,

            second

        )



    def is_duplicate_hook(

        self,

        new_hook,

        existing_hook,

        threshold=55

    ):

        return self.manager.is_duplicate_hook(

            new_hook,

            existing_hook,

            threshold

        )



    def clean_hook(

        self,

        hook

    ):

        return self.manager.clean_hook(

            hook

        )



    def clean_topic(

        self,

        topic

    ):

        return self.manager.clean_topic(

            topic

        )



    def clean_cta(

        self,

        cta

    ):

        return self.manager.clean_cta(

            cta

        )



    def score_content(

        self,

        content

    ):

        return self.manager.score_content(

            content

        )



    def optimize_virality(

        self,

        content,

        platform

    ):

        return self.manager.optimize_virality(

            content,

            platform

        )



    def predict_virality(

        self,

        review,

        viral,

        platform

    ):

        return self.manager.predict_virality(

            review,

            viral,

            platform

        )