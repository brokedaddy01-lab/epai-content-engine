class ReviewerAgent:

    def review(self, text):

        score = 100

        issues = []

        scores = {
            "discipline_score": 0,
            "operator_score": 0,
            "tribe_score": 0,
            "virality_score": 0,
            "cta_score": 0
        }

        lower = text.lower()

        discipline_words = [
            "discipline",
            "consistency",
            "execution",
            "standards",
            "protocol"
        ]

        operator_words = [
            "operator",
            "build",
            "mission",
            "responsibility",
            "ownership"
        ]

        tribe_words = [
            "brotherhood",
            "family",
            "tribe",
            "legacy",
            "pack"
        ]

        viral_words = [
            "most people",
            "the truth",
            "nobody",
            "you"
        ]

        cta_words = [
            "what",
            "comment",
            "share",
            "reflect"
        ]

        for word in discipline_words:

            if word in lower:
                scores["discipline_score"] += 20

        for word in operator_words:

            if word in lower:
                scores["operator_score"] += 20

        for word in tribe_words:

            if word in lower:
                scores["tribe_score"] += 20

        for word in viral_words:

            if word in lower:
                scores["virality_score"] += 20

        for word in cta_words:

            if word in lower:
                scores["cta_score"] += 20

        banned = [
            "believe in yourself",
            "dream big",
            "manifest",
            "you got this"
        ]

        for phrase in banned:

            if phrase in lower:

                score -= 15

                issues.append(phrase)

        total_score = (
            score
            + scores["discipline_score"] // 5
            + scores["operator_score"] // 5
            + scores["tribe_score"] // 5
        )

        return {

            "score": total_score,

            "issues": issues,

            "metrics": scores
        }