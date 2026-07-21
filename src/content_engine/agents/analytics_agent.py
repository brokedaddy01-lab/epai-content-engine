class AnalyticsAgent:

    def score(
        self,
        text
    ):

        score = {

            "discipline": 0,

            "masculinity": 0,

            "tribe": 0,

            "virality": 0
        }

        words = text.lower()

        if "discipline" in words:

            score["discipline"] += 25

        if "standards" in words:

            score["discipline"] += 25

        if "brotherhood" in words:

            score["tribe"] += 25

        if "family" in words:

            score["tribe"] += 25

        return score