from content_engine.agents.quality_services.hook_quality_agent import (
    HookQualityAgent
)

from content_engine.agents.quality_services.memory_filter_agent import (
    MemoryFilterAgent
)

from content_engine.agents.quality_services.performance_scoring_agent import (
    PerformanceScoringAgent
)

from content_engine.agents.quality_services.virality_agent import (
    ViralityAgent
)


class QualityBrain:


    def __init__(self):

        self.hook_quality = HookQualityAgent()

        self.memory_filter = MemoryFilterAgent()

        self.performance = PerformanceScoringAgent()

        self.virality = ViralityAgent()



    ##################################################
    # HOOK QUALITY
    ##################################################

    def score_hook(

        self,

        hook

    ):

        return (

            self.hook_quality
            .score(
                hook
            )

        )



    ##################################################
    # MEMORY CLEANING
    ##################################################

    def clean_hook(

        self,

        hook

    ):

        return (

            self.memory_filter
            .clean_hook(
                hook
            )

        )



    def clean_topic(

        self,

        topic

    ):

        return (

            self.memory_filter
            .clean_topic(
                topic
            )

        )



    def clean_cta(

        self,

        cta

    ):

        return (

            self.memory_filter
            .clean_cta(
                cta
            )

        )



    ##################################################
    # PERFORMANCE
    ##################################################

    def score_content(

        self,

        content

    ):

        return (

            self.performance
            .score(
                content
            )

        )



    ##################################################
    # VIRALITY
    ##################################################

    def optimize_virality(

        self,

        content,

        platform

    ):

        return (

            self.virality
            .optimize(

                content,

                platform

            )

        )
    