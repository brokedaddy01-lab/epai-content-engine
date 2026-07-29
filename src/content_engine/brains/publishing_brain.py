from content_engine.agents.publishing.publishing_manager import (
    PublishingManager
)



class PublishingBrain:


    def __init__(self):

        self.manager = PublishingManager()


        # Compatibility aliases.
        # Previous architecture exposed publishing agents directly.
        self.campaign = self.manager.campaign

        self.publisher = self.manager.publisher

        self.scheduler = self.manager.scheduler



    ##################################################
    # CREATE CAMPAIGN
    ##################################################

    def create_campaign(

        self,

        data

    ):

        return (

            self.manager
            .create_campaign(

                data

            )

        )



    ##################################################
    # PREPARE PUBLISHING
    ##################################################

    def publish(

        self,

        content,

        platform

    ):

        return (

            self.manager
            .publish(

                content,

                platform

            )

        )



    ##################################################
    # SCHEDULE CONTENT
    ##################################################

    def schedule(

        self,

        content,

        platform,

        date

    ):

        return (

            self.manager
            .schedule(

                content,

                platform,

                date

            )

        )



    ##################################################
    # BEST PUBLISH TIME
    ##################################################

    def best_time(

        self,

        platform

    ):

        return (

            self.manager
            .best_time(

                platform

            )

        )