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



class QualityManager:


    def __init__(self):

        self.hook_quality = HookQualityAgent()

        self.hook_similarity = HookSimilarityAgent()

        self.memory_filter = MemoryFilterAgent()

        self.performance = PerformanceScoringAgent()

        self.virality = ViralityAgent()

        self.virality_prediction = ViralityPredictionAgent()



    def score_hook(
        self,
        hook
    ):

        return self.hook_quality.score(
            hook
        )



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



    def score_content(
        self,
        content
    ):

        return self.performance.score(
            content
        )



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