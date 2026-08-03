import datetime
import re


class ContentDirector:


    def __init__(self, registry):

        self.registry = registry

        self.strategy = registry.brain("strategy")

        self.creation = registry.brain("creation")

        self.intelligence = registry.brain("intelligence")

        self.quality = registry.brain("quality")

        self.optimization = registry.brain("optimization")

        self.production = registry.brain("production")

        self.publishing = registry.brain("publishing")


    def clean_output(self, text):

        remove_patterns = [
            r"^Here is the.*?:\s*",
            r"^Here'?s the.*?:\s*",
            r"^Final Post:\s*",
            r"^Analysis:\s*",
            r"^Explanation:\s*",
            r"^The following.*?:\s*",
            r"^Below is.*?:\s*"
        ]

        for pattern in remove_patterns:

            text = re.sub(
                pattern,
                "",
                text,
                flags=re.IGNORECASE | re.MULTILINE
            )

        banned_phrases = [
            "Newsflash:",
            "Here's the thing:",
            "Here's the hard truth:",
            "As we all know,",
            "My friends,"
        ]

        for phrase in banned_phrases:

            text = text.replace(
                phrase,
                ""
            )

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

        return text.strip()


    def clean_cta(self, text):

        lines = text.splitlines()

        seen = False

        cleaned = []

        for line in lines:

            if "follow protocol x" in line.lower():

                if seen:

                    continue

                seen = True

            cleaned.append(line)

        return "\n".join(cleaned).strip()


    def save_memory(
        self,
        row,
        text,
        optimization,
        review
    ):

        if review["score"] < 90:

            return

        lines = text.splitlines()

        hook = ""

        for line in lines:

            cleaned = line.strip()

            if len(cleaned) < 30:

                continue

            hook = cleaned

            break

        hook = self.quality.clean_hook(hook)

        hook_score = self.quality.score_hook(hook)

        if hook_score < 50:

            return

        self.intelligence.remember_content(
            hook=hook,
            topic=row["topic"],
            hashtags=optimization["hashtags"],
            cta=optimization["follow_cta"],
            platform=row["platform"],
            score=review["score"]
        )


    def run(
        self,
        row,
        brand
    ):

        result = self.creation.create(
            row,
            brand
        )

        response = self.clean_output(
            result["content"]
        )

        review = result["review"]

        quality_report = self.quality.analyze(
            response,
            review,
            row["platform"]
        )

        optimization = self.optimization.optimize(
            response,
            row["platform"],
            row.get(
                "topic",
                ""
            )
        )

        response += (
            "\n\n"
            +
            optimization["follow_cta"]
        )

        response += (
            "\n\n"
            +
            " ".join(
                optimization["hashtags"]
            )
        )

        response = self.clean_output(
            response
        )

        response = self.clean_cta(
            response
        )

        self.save_memory(
            row,
            response,
            optimization,
            review
        )

        assets = self.production.generate_assets(
            response,
            row["platform"],
            row["topic"]
        )

        campaign = {

            "brand":
                brand["brand_name"],

            "platform":
                row["platform"],

            "topic":
                row["topic"],

            "created":
                str(
                    datetime.datetime.now()
                ),

            "review_score":
                review["score"]

        }

        return {

            "post":
                assets["formatted"],

            "review":
                review,

            "quality":
                quality_report,

            "campaign":
                campaign,

            "assets":
                assets

        }