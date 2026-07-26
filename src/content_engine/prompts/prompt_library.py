from pathlib import Path


class PromptLibrary:

    def __init__(self):

        self.directory = (
            Path(__file__).parent
        )

        self.default_topic = (
            "mindset.md"
        )

    ####################################################
    # LOAD MARKDOWN PROMPT
    ####################################################

    def load(
        self,
        topic: str
    ) -> str:

        filename = (
            topic.lower()
            .replace(" ", "_")
            + ".md"
        )

        file = (
            self.directory
            / filename
        )

        if not file.exists():

            file = (
                self.directory
                / self.default_topic
            )

        return file.read_text(
            encoding="utf-8"
        ).strip()

    ####################################################
    # AVAILABLE TOPICS
    ####################################################

    def topics(self):

        return sorted(

            file.stem

            for file in self.directory.glob(
                "*.md"
            )

            if file.name != "system_prompt.md"

        )