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

        self.prompt_architect = PromptArchitectAgent()

        self.copywriter = CopywriterAgent()

        self.reviewer = ReviewerAgent()



    ##################################################
    # CREATE CONTENT WITH QUALITY LOOP
    ##################################################

    def create(

        self,
        row,
        brand

    ):


        prompt = (

            self.prompt_architect
            .build_copywriter_prompt(

                row,

                brand

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

            "content": response,

            "review": review,

            "attempts": attempts

        }