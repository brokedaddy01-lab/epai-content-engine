from content_engine.agents.publishing.campaign_agent import (
    CampaignAgent
)

from content_engine.agents.publishing.publishing_agent import (
    PublishingAgent
)

from content_engine.agents.publishing.scheduler_agent import (
    SchedulerAgent
)

from content_engine.agents.base_manager import BaseManager

class PublishingManager(BaseManager):


    def __init__(self):

        self.campaign = CampaignAgent()

        self.publisher = PublishingAgent()

        self.scheduler = SchedulerAgent()



    def create_campaign(
        self,
        data
    ):

        return (
            self.campaign
            .create_campaign(
                data
            )
        )



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



    def best_time(
        self,
        platform
    ):

        return (
            self.scheduler
            .best_times(
                platform
            )
        )