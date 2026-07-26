from content_engine.providers.ollama_provider import (
    OllamaProvider
)


class CopywriterAgent:

    """
    Specialist responsible only for writing content.

    Receives completed prompts from the
    PromptArchitectAgent.
    """


    def __init__(self):

        self.provider = OllamaProvider()



    ####################################################
    # WRITE
    ####################################################

    def write(
        self,
        prompt
    ):

        return self.provider.generate(
            prompt
        )



    ####################################################
    # REWRITE
    ####################################################

    def regenerate(
        self,
        prompt,
        issues
    ):

        rewrite_prompt = (

            prompt

            +

            f"""

━━━━━━━━━━━━━━━━━━

QUALITY REVIEW FEEDBACK

The previous draft needs improvement.

Issues:

{chr(10).join(issues) if issues else "Improve overall quality."}


Rewrite requirements:

- Stronger hook
- Better storytelling
- More emotional impact
- More practical value
- Better brand alignment
- Stronger engagement

Return ONLY the finished content.

━━━━━━━━━━━━━━━━━━

"""
        )


        return self.provider.generate(
            rewrite_prompt
        )