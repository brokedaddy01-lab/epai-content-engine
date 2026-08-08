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