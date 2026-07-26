from content_engine.agents.intelligence.performance_learning_agent import (
    PerformanceLearningAgent
)


class AnalyticsAgent:

    """
    Central analytics layer.

    Responsible for:

    - Performance scoring
    - Platform summaries
    - Future trend analysis
    - Strategy recommendations

    The orchestrator should only call this class.
    """

    def __init__(self):

        self.performance = PerformanceLearningAgent()

    ####################################################
    # CONTENT PERFORMANCE SCORE
    ####################################################

    def analyze(
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
            ) * 2

            +

            metrics.get(
                "shares",
                0
            ) * 4

            +

            metrics.get(
                "follows",
                0
            ) * 8

        )

        return {

            "performance": score

        }

    ####################################################
    # MEMORY ANALYTICS
    ####################################################

    def summarize_memory(
        self,
        memory_data
    ):

        return self.performance.learn(
            memory_data
        )

    ####################################################
    # PLATFORM LOOKUP
    ####################################################

    def platform_summary(
        self,
        memory_data,
        platform
    ):

        summary = self.summarize_memory(
            memory_data
        )

        return summary.get(
            platform,
            {}
        )

    ####################################################
    # GLOBAL SUMMARY
    ####################################################

    def overall_summary(
        self,
        memory_data
    ):

        summary = self.summarize_memory(
            memory_data
        )

        if not summary:

            return {}

        averages = [

            item["average_score"]

            for item in summary.values()

        ]

        return {

            "platforms":

                len(summary),

            "overall_average":

                round(

                    sum(averages)

                    /

                    len(averages),

                    2

                ),

            "best_platform":

                max(

                    summary,

                    key=lambda x:
                    summary[x]["average_score"]

                )

        }