from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.publishing.publishing_manager import (
    PublishingManager
)


class PublishingBrain(BaseBrain):


    manager_class = PublishingManager



    ##################################################
    # CAMPAIGN CREATION
    ##################################################

    def create_campaign(

        self,

        data

    ):

        return self.manager.create_campaign(

            data

        )



    ##################################################
    # PUBLISH CONTENT
    ##################################################

    def publish(

        self,

        content,

        platform

    ):

        return self.manager.publish(

            content,

            platform

        )



    ##################################################
    # SCHEDULING
    ##################################################

    def schedule(

        self,

        content,

        platform,

        date

    ):

        return self.manager.schedule(

            content,

            platform,

            date

        )



    def best_time(

        self,

        platform

    ):

        return self.manager.best_time(

            platform

        )