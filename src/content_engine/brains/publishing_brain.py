from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.models.content_context import (
    ContentContext
)

from content_engine.agents.publishing.publishing_manager import (
    PublishingManager
)


class PublishingBrain(BaseBrain):

    manager_class = PublishingManager

    def publish(
        self,
        content,
        platform=None
    ):

        if isinstance(
            content,
            ContentContext
        ):

            context = content

            return self.manager.publish(
                context.content,
                context.platform
            )

        return self.manager.publish(
            content,
            platform
        )