from content_engine.agents.creation.story_engine_agent import (
    StoryEngineAgent
)

from content_engine.agents.creation.prompt_architect_agent import (
    PromptArchitectAgent
)

from content_engine.agents.creation.copywriter_agent import (
    CopywriterAgent
)

from content_engine.agents.creation.reviewer_agent import (
    ReviewerAgent
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)



class CreationBrain:


    def __init__(

        self,

        quality_threshold=90,

        max_attempts=3

    ):


        self.story_engine = StoryEngineAgent()

        self.prompt_architect = PromptArchitectAgent()

        self.copywriter = CopywriterAgent()

        self.reviewer = ReviewerAgent()

        self.memory = ContentMemoryManager()


        self.quality_threshold = (
            quality_threshold
        )

        self.max_attempts = (
            max_attempts
        )



    ##################################################
    # CREATE CONTENT
    ##################################################

    def create(

        self,

        row,

        brand

    ):


        topic = row.get(
            "topic",
            ""
        )


        platform = row.get(
            "platform",
            "social"
        )


        audience = row.get(
            "audience",
            "target audience"
        )



        story = (

            self.story_engine
            .build_story(

                topic,

                audience,

                platform

            )

        )



        prompt = (

            self.prompt_architect
            .build_copywriter_prompt(

                row,

                brand,

                story

            )

        )



        response = (

            self.copywriter
            .write(

                prompt

            )

        )


        if not response:

            return {

                "content": "",

                "review": {

                    "score": 0,

                    "issues": [
                        "Generation failed"
                    ]

                },

                "attempts": 0,

                "story": story

            }



        review = (

            self.reviewer
            .review(

                response

            )

        )



        attempts = 1



        while (

            review["score"]

            <

            self.quality_threshold

            and

            attempts

            <

            self.max_attempts

        ):


            response = (

                self.copywriter
                .regenerate(

                    prompt,

                    review.get(
                        "issues",
                        []
                    )

                )

            )


            review = (

                self.reviewer
                .review(

                    response

                )

            )


            attempts += 1



        ##################################################
        # STORE LEARNING MEMORY
        ##################################################

        if review["score"] >= self.quality_threshold:


            self.memory.remember_success(

                hook=response.splitlines()[0]
                if response
                else "",

                topic=topic,

                hashtags=row.get(
                    "hashtags",
                    []
                ),

                cta=row.get(
                    "cta",
                    ""
                ),

                platform=platform,

                score=review["score"]

            )



        return {


            "content":

                response,


            "review":

                review,


            "attempts":

                attempts,


            "story":

                story

        }