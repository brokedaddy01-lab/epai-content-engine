import json
from pathlib import Path


class KnowledgeAgent:

    def __init__(self):

        self.file = Path(
            "data/protocolx_knowledge.json"
        )

        if not self.file.exists():

            self.save(
                {}
            )

    def load(self):

        with open(

            self.file,
            "r",
            encoding="utf-8"

        ) as f:

            return json.load(f)

    def save(
        self,
        data
    ):

        with open(

            self.file,
            "w",
            encoding="utf-8"

        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )

    def remember(

        self,
        key,
        value
    ):

        data = self.load()

        data[key] = value

        self.save(data)