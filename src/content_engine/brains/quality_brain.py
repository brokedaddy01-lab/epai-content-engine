from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.quality.quality_manager import (
    QualityManager
)


class QualityBrain(BaseBrain):


    manager_class = QualityManager



    def analyze(

        self,

        content,

        review,

        platform

    ):

        return self.manager.analyze(

            content,

            review,

            platform

        )