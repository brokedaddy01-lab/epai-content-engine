from pathlib import Path

from content_engine.prompts.prompt_library import (
    PromptLibrary
)


class PromptEngine:

    def __init__(self):

        self.library = PromptLibrary()

        self.directory = (
            Path(__file__).parent
        )

    ####################################################
    # LOAD SYSTEM PROMPT
    ####################################################

    def load_system_prompt(self):

        file = (
            self.directory
            / "system_prompt.md"
        )

        if not file.exists():

            return ""

        return file.read_text(
            encoding="utf-8"
        ).strip()

    ####################################################
    # BUILD FINAL PROMPT
    ####################################################

    def build(
        self,
        row,
        brand
    ):

        system_prompt = (
            self.load_system_prompt()
        )

        topic_prompt = (
            self.library.load(
                row["topic"]
            )
        )

        mission = (
            brand["identity"]["mission"]
        )

        philosophy = (
            brand["identity"].get(
                "philosophy",
                ""
            )
        )

        audience = ", ".join(

            brand["identity"].get(
                "audience",
                []
            )

        )

        values = ", ".join(

            brand.get(
                "core_values",
                []
            )

        )

        themes = ", ".join(

            brand.get(
                "themes",
                []
            )

        )

        tone = ", ".join(

            brand.get(
                "tone",
                []
            )

        )

        keyword = row.get(
            "keyword",
            ""
        )

        return f"""
{system_prompt}

━━━━━━━━━━━━━━━━━━

BRAND

Name:
{brand["brand_name"]}

Mission:
{mission}

Philosophy:
{philosophy}

Audience:
{audience}

Values:
{values}

Themes:
{themes}

Voice:
{tone}

━━━━━━━━━━━━━━━━━━

CONTENT REQUEST

Platform:
{row["platform"]}

Topic:
{row["topic"]}

SEO Keyword:
{keyword}

Hook:
{row["hook"]}

CTA:
{row["cta"]}

━━━━━━━━━━━━━━━━━━

TOPIC EXPERTISE

{topic_prompt}

━━━━━━━━━━━━━━━━━━

Return ONLY the final content.
"""