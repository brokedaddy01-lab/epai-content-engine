import json
from pathlib import Path


class FeedbackLoopAgent:

    def __init__(self):

        self.file = Path(
            "data/content_feedback.json"
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

    def remember(

        self,
        feedback
    ):

        data = self.load()

        data.append(
            feedback
        )

        self.save(data)