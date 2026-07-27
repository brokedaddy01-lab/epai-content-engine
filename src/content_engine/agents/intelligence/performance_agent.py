import json

from pathlib import Path



class PerformanceAgent:


    def __init__(self):

        self.file = Path(
            "data/performance_memory.json"
        )


        if not self.file.exists():

            self.save([])



    def load(self):

        try:

            with open(

                self.file,

                "r",

                encoding="utf-8"

            ) as f:

                return json.load(f)


        except Exception:

            return []



    def save(
        self,
        data
    ):

        self.file.parent.mkdir(
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



    def track(
        self,
        metrics
    ):

        data = self.load()


        data.append(
            metrics
        )


        self.save(
            data
        )



    def best_posts(self):

        data = self.load()


        return sorted(

            data,

            key=lambda x:

            x.get(

                "follows",

                0

            ),

            reverse=True

        )