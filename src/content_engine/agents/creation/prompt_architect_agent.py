from content_engine.prompts.prompt_engine import (
    PromptEngine
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)



class PromptArchitectAgent:


    def __init__(self):

        self.engine = PromptEngine()

        self.memory = ContentMemoryManager()



    def build_copywriter_prompt(

        self,

        row,

        brand,

        story_framework

    ):


        base_prompt = self.engine.build(

            row,

            brand

        )


        memory = (
            self.memory
            .get_prompt_context()
        )


        memory_block = f"""

━━━━━━━━━━━━━━━━━━

CONTENT MEMORY

Avoid repeating:

Topics:

{memory.get("recent_topics", [])}


Hooks:

{memory.get("recent_hooks", [])}


Rejected:

{memory.get("rejected_phrases", [])}


Create original content.

━━━━━━━━━━━━━━━━━━

"""


        story_block = f"""

━━━━━━━━━━━━━━━━━━

STORY FRAMEWORK

Topic:

{story_framework.get("topic")}


Audience:

{story_framework.get("audience")}


Platform:

{story_framework.get("platform")}


Instructions:

{story_framework.get("instruction")}

━━━━━━━━━━━━━━━━━━

"""


        return (

            base_prompt

            +

            memory_block

            +

            story_block

        )