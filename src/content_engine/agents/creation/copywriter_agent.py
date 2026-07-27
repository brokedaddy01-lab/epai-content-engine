from content_engine.providers.ollama_provider import (
    OllamaProvider
)


class CopywriterAgent:


    def __init__(self):

        self.provider = OllamaProvider()



    def write(

        self,

        prompt

    ):

        return self.provider.generate(
            prompt
        )



    def regenerate(

        self,

        prompt,

        issues=None

    ):


        if not issues:

            issues = [
                "Improve overall quality"
            ]


        feedback = "\n".join(
            issues
        )


        rewrite_prompt = f"""

{prompt}


━━━━━━━━━━━━━━━━━━

QUALITY REVIEW FEEDBACK

Fix these issues:

{feedback}


Requirements:

- Stronger opening hook
- Better storytelling
- More emotional depth
- More practical value
- Better audience connection
- Stronger CTA

Return ONLY the finished content.

━━━━━━━━━━━━━━━━━━

"""


        return self.provider.generate(
            rewrite_prompt
        )