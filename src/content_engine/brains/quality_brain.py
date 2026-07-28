from content_engine.agents.quality.hook_quality_agent import (
    HookQualityAgent
)

from content_engine.agents.quality.hook_similarity_agent import (
    HookSimilarityAgent
)

from content_engine.agents.quality.memory_filter_agent import (
    MemoryFilterAgent
)

from content_engine.agents.quality.performance_scoring_agent import (
    PerformanceScoringAgent
)

from content_engine.agents.quality.virality_agent import (
    ViralityAgent
)

from content_engine.agents.quality.virality_prediction_agent import (
    ViralityPredictionAgent
)


class QualityBrain:


    def __init__(self):

        self.hook_quality = HookQualityAgent()

        self.hook_similarity = HookSimilarityAgent()

        self.memory_filter = MemoryFilterAgent()

        self.performance = PerformanceScoringAgent()

        self.virality = ViralityAgent()

        self.virality_prediction = ViralityPredictionAgent()



    ##################################################
    # FULL QUALITY ANALYSIS
    ##################################################

    def analyze(
        self,
        content,
        review,
        platform
    ):

        hook = ""

        for line in content.splitlines():

            cleaned = line.strip()

            if cleaned:

                hook = cleaned

                break


        content_score = self.score_content(
            content
        )


        hook_score = self.score_hook(
            hook
        )


        viral = self.optimize_virality(
            content,
            platform
        )


        prediction = self.predict_virality(
            review,
            viral,
            platform
        )


        return {

            "review_score":
                review["score"],

            "content_score":
                content_score,

            "hook_score":
                hook_score,

            "virality":
                viral,

            "prediction":
                prediction

        }



    ##################################################
    # HOOK QUALITY
    ##################################################

    def score_hook(
        self,
        hook
    ):

        return self.hook_quality.score(
            hook
        )



    ##################################################
    # HOOK SIMILARITY
    ##################################################

    def compare_hooks(
        self,
        first,
        second
    ):

        return self.hook_similarity.similarity(
            first,
            second
        )



    def is_duplicate_hook(
        self,
        new_hook,
        existing_hook,
        threshold=55
    ):

        return self.hook_similarity.is_similar(
            new_hook,
            existing_hook,
            threshold
        )



    ##################################################
    # MEMORY CLEANING
    ##################################################

    def clean_hook(
        self,
        hook
    ):

        return self.memory_filter.clean_hook(
            hook
        )



    def clean_topic(
        self,
        topic
    ):

        return self.memory_filter.clean_topic(
            topic
        )



    def clean_cta(
        self,
        cta
    ):

        return self.memory_filter.clean_cta(
            cta
        )



    ##################################################
    # PERFORMANCE
    ##################################################

    def score_content(
        self,
        content
    ):

        return self.performance.score(
            content
        )



    ##################################################
    # VIRALITY
    ##################################################

    def optimize_virality(
        self,
        content,
        platform
    ):

        return self.virality.optimize(
            content,
            platform
        )



    def predict_virality(
        self,
        review,
        viral,
        platform
    ):

        return self.virality_prediction.predict(
            review,
            viral,
            platform
        )