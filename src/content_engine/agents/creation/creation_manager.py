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


class CreationManager:


    def __init__(

        self,

        memory

    ):

        self.memory = memory


        self.story_engine = StoryEngineAgent()


        self.prompt_architect = PromptArchitectAgent(

            memory

        )


        self.copywriter = CopywriterAgent()


        self.reviewer = ReviewerAgent()



    def create(

        self,

        row,

        brand

    ):


        story = self.story_engine.build_story(

            row.get(

                "topic",

                ""

            ),

            brand.get(

                "audience",

                "disciplined operators"

            ),

            row.get(

                "platform",

                ""

            )

        )


        prompt = self.prompt_architect.build_copywriter_prompt(

            row,

            brand,

            story

        )


        content = self.copywriter.write(

            prompt

        )


        review = self.reviewer.review(

            content

        )


        return {

            "content": content,

            "story": story,

            "prompt": prompt,

            "review": review

        }