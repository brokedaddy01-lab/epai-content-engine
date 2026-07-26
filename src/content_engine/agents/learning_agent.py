import json
from pathlib import Path


class LearningAgent:

    def __init__(self):

        self.file = Path(
            "data/learning_memory.json"
        )

        if not self.file.exists():

            self.save([])

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

    def learn(

        self,
        topic,
        score,
        platform
    ):

        data = self.load()

        data.append({

            "topic": topic,
            "score": score,
            "platform": platform

        })

        self.save(data)