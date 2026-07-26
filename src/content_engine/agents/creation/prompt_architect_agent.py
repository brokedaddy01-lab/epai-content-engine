from content_engine.prompts.prompt_engine import (
    PromptEngine
)

from content_engine.agents.content_memory_manager import (
    ContentMemoryManager
)



class PromptArchitectAgent:

    """
    Builds specialized prompts for
    content generation agents.

    The Prompt Architect owns:
    - prompt construction
    - memory injection
    - brand context
    """



    def __init__(self):

        self.engine = PromptEngine()

        self.memory = ContentMemoryManager()



    ####################################################
    # BUILD COPYWRITER PROMPT
    ####################################################

    def build_copywriter_prompt(

        self,
        row,
        brand

    ):


        base_prompt = self.engine.build(

            row,

            brand

        )


        memory_context = (

            self.memory
            .get_prompt_context()

        )


        memory_block = f"""

━━━━━━━━━━━━━━━━━━

CONTENT MEMORY

Avoid repeating:

Recent Topics:

{memory_context["recent_topics"]}


Recent Hooks:

{memory_context["recent_hooks"]}


Avoid These Phrases:

{memory_context["rejected_phrases"]}


Create something original.

━━━━━━━━━━━━━━━━━━

"""


        return (

            base_prompt

            +

            memory_block

        )