import json
from pathlib import Path


class MemoryAgent:


    def __init__(self):

        self.file = Path(
            "data/content_memory.json"
        )


    def load(self):

        if not self.file.exists():

            return self.default_memory()


        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def default_memory(self):

        return {

            "successful_hooks": [],

            "failed_hooks": [],

            "successful_topics": [],

            "failed_topics": [],

            "successful_hashtags": {},

            "failed_hashtags": [],

            "successful_ctas": {},

            "failed_ctas": [],

            "rejected_phrases": [],

            "high_performing_posts": [],

            "low_performing_posts": [],

            "platform_performance": {}

        }



    def save(
        self,
        data
    ):

        self.file.parent.mkdir(
            parents=True,
            exist_ok=True
        )


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



    ##################################################
    # FILTER MEMORY
    ##################################################

    def valid_memory(
        self,
        text
    ):


        if not text:

            return False


        banned = [

            "here is",

            "here's",

            "final post",

            "video script",

            "content:",

            "i cannot",

            "i understand",

            "assistant",

            "ai"

        ]


        lower = text.lower()


        for phrase in banned:

            if phrase in lower:

                return False


        return True