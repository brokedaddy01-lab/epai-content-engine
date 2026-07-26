import datetime
import re

from content_engine.agents.hook_quality_agent import (
    HookQualityAgent
)

from content_engine.agents.copywriter_agent import (
    CopywriterAgent
)

from content_engine.agents.prompt_architect_agent import (
    PromptArchitectAgent
)

from content_engine.agents.content_memory_manager import (
    ContentMemoryManager
)

from content_engine.agents.memory_filter_agent import (
    MemoryFilterAgent
)

from content_engine.agents.reviewer_agent import (
    ReviewerAgent
)

from content_engine.agents.virality_agent import (
    ViralityAgent
)

from content_engine.agents.growth_agent import (
    GrowthAgent
)

from content_engine.agents.formatter_agent import (
    FormatterAgent
)

from content_engine.agents.image_agent import (
    ImageAgent
)

from content_engine.agents.newsletter_agent import (
    NewsletterAgent
)

from content_engine.agents.video_script_agent import (
    VideoScriptAgent
)

from content_engine.agents.carousel_agent import (
    CarouselAgent
)



class ContentOrchestrator:


    def __init__(self):

        self.hook_quality = HookQualityAgent()
        
        self.copywriter = CopywriterAgent()

        self.prompt_architect = PromptArchitectAgent()

        self.memory = ContentMemoryManager()

        self.memory_filter = MemoryFilterAgent()

        self.reviewer = ReviewerAgent()

        self.virality = ViralityAgent()

        self.growth = GrowthAgent()

        self.formatter = FormatterAgent()

        self.image = ImageAgent()

        self.newsletter = NewsletterAgent()

        self.video = VideoScriptAgent()

        self.carousel = CarouselAgent()



    ####################################################
    # CLEAN AI OUTPUT
    ####################################################

    def clean_output(
        self,
        text
    ):

        remove_phrases = [

            "Here is the content that meets the requirements:",

            "Here is the final post:",

            "Here's the post:",

            "Here is your post:",

            "Here is the finished content",

            "Here is the completed post",

            "Final Post:",

            "Analysis:",

            "Explanation:",

            "This post meets all requirements:",

            "The content above"

        ]


        for phrase in remove_phrases:

            text = text.replace(
                phrase,
                ""
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



    ####################################################
    # CTA CLEANER
    ####################################################

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


            cleaned.append(
                line
            )


        return "\n".join(
            cleaned
        ).strip()



    ####################################################
    # SAVE MEMORY
    ####################################################

       ####################################################
    # SAVE MEMORY
    ####################################################

    def save_memory(
        self,
        row,
        text,
        growth,
        review
    ):

        if review["score"] < 90:

            return


        lines = text.splitlines()


        hook = ""


        for line in lines:

            cleaned = line.strip()


            if not cleaned:

                continue


            lower = cleaned.lower()


            blocked = [

                "here is",

                "here's",

                "final",

                "content:",

                "post:",

                "script:",

                "video:",

                "i cannot",

                "i can't",

                "as an",

                "i am",

                "i'm",

                "follow protocol",

                "#"

            ]


            if any(

                phrase in lower

                for phrase in blocked

            ):

                continue


            if len(cleaned) < 30:

                continue


            hook = cleaned

            break



        hook = self.memory_filter.clean_hook(
            hook
        )


        hook_score = self.hook_quality.score(
            hook
        )


        if hook_score < 50:

            return



        topic = self.memory_filter.clean_topic(
            row["topic"]
        )


        cta = self.memory_filter.clean_cta(
            growth["follow_cta"]
        )



        self.memory.remember_success(

            hook=hook,

            topic=topic,

            hashtags=growth["hashtags"],

            cta=cta,

            platform=row["platform"],

            score=review["score"]

        )

    ####################################################
    # QUALITY LOOP
    ####################################################

    def generate_with_quality_gate(
        self,
        row,
        brand
    ):


        attempts = 0

        max_attempts = 3


        prompt = self.prompt_architect.build_copywriter_prompt(
            row,
            brand
        )


        response = self.copywriter.write(
            prompt
        )


        response = self.clean_output(
            response
        )


        review = self.reviewer.review(
            response
        )


        attempts += 1



        while (

            review["score"] < 90

            and

            attempts < max_attempts

        ):


            response = self.copywriter.regenerate(

                prompt,

                review["issues"]

            )


            response = self.clean_output(
                response
            )


            review = self.reviewer.review(
                response
            )


            attempts += 1



        return response, review, attempts



    ####################################################
    # MAIN PIPELINE
    ####################################################

    def run(
        self,
        row,
        brand
    ):


        response, review, attempts = self.generate_with_quality_gate(

            row,

            brand

        )



        viral = self.virality.optimize(

            response,

            row["platform"]

        )


        growth = self.growth.optimize(

            response,

            row["platform"]

        )



        response += (

            "\n\n"

            +

            growth["follow_cta"]

        )


        response += (

            "\n\n"

            +

            " ".join(
                growth["hashtags"]
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

            growth,

            review

        )



        formatted = self.formatter.format(

            response,

            row["platform"]

        )



        campaign = {

            "brand":
                brand["brand_name"],

            "platform":
                row["platform"],

            "topic":
                row["topic"],

            "keyword":
                row.get(
                    "keyword",
                    ""
                ),

            "created":
                str(
                    datetime.datetime.now()
                ),

            "review_score":
                review["score"],

            "quality_attempts":
                attempts

        }



        return {

            "post":
                formatted,

            "review":
                review,

            "virality":
                viral,

            "campaign":
                campaign,

            "image_prompt":
                self.image.generate_prompt(
                    formatted
                ),

            "video_script":
                self.video.generate(
                    formatted
                ),

            "newsletter":
                self.newsletter.generate(
                    formatted
                ),

            "carousel":
                self.carousel.generate(
                    row["topic"]
                )

        }