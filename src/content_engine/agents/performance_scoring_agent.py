class PerformanceScoringAgent:

    def score(

        self,
        metrics
    ):

        score = (

            metrics.get(
                "likes",
                0
            )

            +

            metrics.get(
                "comments",
                0
            ) * 3

            +

            metrics.get(
                "shares",
                0
            ) * 5

            +

            metrics.get(
                "follows",
                0
            ) * 10
        )

        return score