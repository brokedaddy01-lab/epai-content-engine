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


class CreationBrain:


    def __init__(self):

        self.story_engine = StoryEngineAgent()

        self.prompt_architect = PromptArchitectAgent()

        self.copywriter = CopywriterAgent()

        self.reviewer = ReviewerAgent()



    ##################################################
    # CREATE CONTENT WITH STORY + QUALITY LOOP
    ##################################################

    def create(

        self,

        row,

        brand

    ):


        topic = (

            row.get(
                "topic",
                ""
            )

        )


        platform = (

            row.get(
                "platform",
                "social"
            )

        )


        audience = (

            row.get(
                "audience",
                "target audience"
            )

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



        review = (

            self.reviewer
            .review(

                response

            )

        )



        attempts = 1



        while (

            review["score"] < 90

            and

            attempts < 3

        ):


            response = (

                self.copywriter
                .regenerate(

                    prompt,

                    review["issues"]

                )

            )


            review = (

                self.reviewer
                .review(

                    response

                )

            )


            attempts += 1



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