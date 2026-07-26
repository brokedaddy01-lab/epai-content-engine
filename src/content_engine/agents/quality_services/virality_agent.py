class ViralityAgent:

    def optimize(

        self,
        text,
        platform
    ):

        score = 50

        if "Most people" in text:

            score += 10

        if "Nobody" in text:

            score += 10

        if len(text) < 1500:

            score += 5

        return {

            "virality_score":
                score,

            "platform":
                platform
        }