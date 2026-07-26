from content_engine.agents.publishing.campaign_agent import (
    CampaignAgent
)

from content_engine.agents.publishing.publishing_agent import (
    PublishingAgent
)

from content_engine.agents.publishing.scheduler_agent import (
    SchedulerAgent
)



class PublishingBrain:


    def __init__(self):

        self.campaign = CampaignAgent()

        self.publisher = PublishingAgent()

        self.scheduler = SchedulerAgent()



    ##################################################
    # CREATE CAMPAIGN
    ##################################################

    def create_campaign(

        self,

        data

    ):

        return (

            self.campaign
            .create(

                data

            )

        )



    ##################################################
    # PUBLISH CONTENT
    ##################################################

    def publish(

        self,

        content,

        platform

    ):

        return (

            self.publisher
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

            self.scheduler
            .schedule(

                content,

                platform,

                date

            )

        )