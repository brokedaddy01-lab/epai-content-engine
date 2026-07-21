from content_engine.providers.ollama_provider import (
    OllamaProvider
)


class WriterAgent:

    def __init__(self):

        self.provider = OllamaProvider()

    def build_prompt(
        self,
        row,
        brand
    ):

        topic = row["topic"]
        hook = row["hook"]
        cta = row["cta"]

        return f"""
You are the official writer for Protocol X.

Voice Blend:

50% Coach Blue
20% Stoicism
10% Eric Thomas
15% George Whitaker
5% Viking / Wolf / Taino symbolism

Mission:

{brand.mission}

Philosophy:

{brand.philosophy}

Core Values:

{", ".join(brand.values)}

Themes:

{", ".join(brand.themes)}

Rules:

- Build identity
- Build tribe
- Build disciplined operators
- Calm authority
- Masculine
- No fake motivation
- No influencer fluff
- Short powerful sentences

Structure:

Hook

Truth

Protocol

Execution

Reflection

CTA

Topic:

{topic}

Hook:

{hook}

CTA:

{cta}

Output ONLY the final post.
"""

    def write(
        self,
        row,
        brand
    ):

        prompt = self.build_prompt(
            row,
            brand
        )

        return self.provider.generate(
            prompt
        )

    def regenerate(
        self,
        row,
        brand,
        issues
    ):

        prompt = (
            self.build_prompt(
                row,
                brand
            )
            +
            f"""

Rewrite the post.

Avoid:

{issues}
"""
        )

        return self.provider.generate(
            prompt
        )