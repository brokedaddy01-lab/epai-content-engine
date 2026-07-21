from content_engine.providers.ollama_provider import (
    OllamaProvider
)


class WriterAgent:

    def __init__(self):

        self.provider = (
            OllamaProvider()
        )

    def write(
        self,
        row,
        brand
    ):

        topic = row["topic"]

        hook = row["hook"]

        cta = row["cta"]

        prompt = f"""
You are the official writer for
Protocol X.

MISSION:

{brand.mission}

PHILOSOPHY:

{brand.philosophy}

CORE VALUES:

{", ".join(brand.values)}

THEMES:

{", ".join(brand.themes)}

VOICE MIX:

Coach Blue:
{brand.voice_mix["coach_blue"]}%

Stoicism:
{brand.voice_mix["stoicism"]}%

Eric Thomas:
{brand.voice_mix["eric_thomas"]}%

George Whitaker:
{brand.voice_mix["george_whitaker"]}%

Ancestral Symbolism:
{brand.voice_mix["ancestral_values"]}%

WRITING RULES:

{chr(10).join(
"- " + r for r in brand.rules
)}

CONTENT TOPIC:

{topic}

HOOK:

{hook}

CTA:

{cta}

POST STRUCTURE:

Hook

Truth

Protocol

Execution

Reflection

CTA

Output ONLY the final post.
"""

        response = (
            self.provider.generate(
                prompt
            )
        )

        return response