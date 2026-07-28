class PerformanceScoringAgent:
    """
    Calculates content quality score before publishing.

    This does NOT measure real-world engagement.
    Real performance learning belongs to IntelligenceBrain.
    """

    def score(
        self,
        content
    ):

        score = 0


        text = str(
            content
        )


        # Length quality

        if len(text) >= 100:

            score += 20


        if len(text) >= 500:

            score += 10


        # Structure indicators

        if "?" in text:

            score += 10


        if "\n" in text:

            score += 10


        # Hook indicators

        strong_hooks = [

            "Most people",

            "Nobody",

            "The truth",

            "Stop",

            "Why"

        ]


        for phrase in strong_hooks:

            if phrase.lower() in text.lower():

                score += 10

                break



        return min(
            score,
            100
        )