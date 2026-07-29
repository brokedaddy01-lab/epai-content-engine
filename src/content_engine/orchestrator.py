import datetime
import re


from content_engine.brains.strategy_brain import (
    StrategyBrain
)

from content_engine.brains.creation_brain import (
    CreationBrain
)

from content_engine.brains.intelligence_brain import (
    IntelligenceBrain
)

from content_engine.brains.quality_brain import (
    QualityBrain
)

from content_engine.brains.optimization_brain import (
    OptimizationBrain
)

from content_engine.brains.production_brain import (
    ProductionBrain
)

from content_engine.brains.publishing_brain import (
    PublishingBrain
)

from content_engine.registry import (
    ManagerRegistry
)



class ContentOrchestrator:


    def __init__(self):

        self.registry = ManagerRegistry()


        self.strategy = StrategyBrain(

            self.registry.get(

                "strategy"

            )

        )


        self.creation = CreationBrain(

            manager=self.registry.get(

                "creation"

            )

        )


        self.intelligence = IntelligenceBrain(

            manager=self.registry.get(

                "intelligence"

            )

        )


        self.quality = QualityBrain(

            manager=self.registry.get(

                "quality"

            )

        )


        self.optimization = OptimizationBrain(

            manager=self.registry.get(

                "optimization"

            )

        )


        self.production = ProductionBrain(

            manager=self.registry.get(

                "production"

            )

        )


        self.publishing = PublishingBrain(

            manager=self.registry.get(

                "publishing"

            )

        )



    ##################################################
    # CLEAN AI OUTPUT
    ##################################################

    def clean_output(

        self,

        text

    ):

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



    ##################################################
    # CTA CLEANER
    ##################################################

    def clean_cta(

        self,

        text

    ):

        lines = text.splitlines()

        seen = False

        cleaned = []


        for line in lines:

            if "follow protocol x" in line.lower():

                if seen:

                    continue

                seen = True


            cleaned.append(line)


        return "\n".join(

            cleaned

        ).strip()



    ##################################################
    # MEMORY SAVE
    ##################################################

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



        hook = self.quality.clean_hook(

            hook

        )


        hook_score = self.quality.score_hook(

            hook

        )


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



    ##################################################
    # MAIN PIPELINE
    ##################################################

    def run(

        self,

        row,

        brand

    ):


        ##################################################
        # CREATION
        ##################################################

        result = self.creation.create(

            row,

            brand

        )


        response = self.clean_output(

            result["content"]

        )


        review = result["review"]



        ##################################################
        # QUALITY ANALYSIS
        ##################################################

        quality_report = self.quality.analyze(

            response,

            review,

            row["platform"]

        )



        ##################################################
        # OPTIMIZATION
        ##################################################

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



        ##################################################
        # INTELLIGENCE
        ##################################################

        self.save_memory(

            row,

            response,

            optimization,

            review

        )



        ##################################################
        # PRODUCTION
        ##################################################

        assets = self.production.generate_assets(

            response,

            row["platform"],

            row["topic"]

        )



        ##################################################
        # CAMPAIGN
        ##################################################

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



        ##################################################
        # RETURN
        ##################################################

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