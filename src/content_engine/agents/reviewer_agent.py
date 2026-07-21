class ReviewerAgent:

    def review(
        self,
        text
    ):

        score = 100

        issues = []

        banned = [

            "believe in yourself",
            "you got this",
            "dream big",
            "never give up",
            "manifest",
            "universe"
        ]

        for phrase in banned:

            if phrase.lower() in text.lower():

                score -= 15

                issues.append(
                    phrase
                )

        if len(text) < 300:

            score -= 10

            issues.append(
                "too short"
            )

        return {

            "score": score,

            "issues": issues
        }