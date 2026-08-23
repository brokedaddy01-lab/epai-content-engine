import datetime

from content_engine.models.content_context import (
    ContentContext
)

from content_engine.content_cleaner import (
    ContentCleaner
)

from content_engine.content_assembler import (
    ContentAssembler
)


class ContentDirector:

    def __init__(self, registry):

        self.registry = registry

        self.cleaner = ContentCleaner()

        self.assembler = ContentAssembler(
            self.cleaner
        )

        self.strategy = registry.brain("strategy")

        self.creation = registry.brain("creation")

        self.intelligence = registry.brain("intelligence")

        self.quality = registry.brain("quality")

        self.optimization = registry.brain("optimization")

        self.production = registry.brain("production")

        self.publishing = registry.brain("publishing")

        self.context = None


    def clean_output(
        self,
        text
    ):

        return self.cleaner.clean_output(
            text
        )


    def clean_cta(
        self,
        text
    ):

        return self.cleaner.clean_cta(
            text
        )


    def save_memory(
        self,
        row,
        text,
        optimization,
        review
    ):

        self.intelligence.manager.content_memory.save_successful_content(

            row=row,

            text=text,

            optimization=optimization,

            review=review,

            quality=self.quality

        )


    def run(
        self,
        row,
        brand
    ):

        self.context = ContentContext(
            topic=row["topic"],
            platform=row["platform"],
            brand=brand
        )

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

        response = self.assembler.assemble(
            response,
            optimization
        )

        self.context.update_content(
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