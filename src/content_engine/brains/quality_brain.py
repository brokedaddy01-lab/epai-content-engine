from content_engine.agents.quality.quality_manager import (
    QualityManager
)



class QualityBrain:


    def __init__(
        self,
        manager=None
    ):


        if manager is None:

            self.manager = QualityManager()

        else:

            self.manager = manager



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



    def score_hook(
        self,
        hook
    ):

        return self.manager.score_hook(
            hook
        )



    def compare_hooks(
        self,
        first,
        second
    ):

        return self.manager.compare_hooks(
            first,
            second
        )



    def is_duplicate_hook(
        self,
        new_hook,
        existing_hook,
        threshold=55
    ):

        return self.manager.is_duplicate_hook(
            new_hook,
            existing_hook,
            threshold
        )



    def clean_hook(
        self,
        hook
    ):

        return self.manager.clean_hook(
            hook
        )



    def clean_topic(
        self,
        topic
    ):

        return self.manager.clean_topic(
            topic
        )



    def clean_cta(
        self,
        cta
    ):

        return self.manager.clean_cta(
            cta
        )



    def score_content(
        self,
        content
    ):

        return self.manager.score_content(
            content
        )



    def optimize_virality(
        self,
        content,
        platform
    ):

        return self.manager.optimize_virality(
            content,
            platform
        )



    def predict_virality(
        self,
        review,
        viral,
        platform
    ):

        return self.manager.predict_virality(
            review,
            viral,
            platform
        )