import json
from pathlib import Path


class MemoryAgent:

    def __init__(
        self,
        memory_file="data/content_memory.json"
    ):

        self.memory_file = Path(
            memory_file
        )

        self.memory = self._load()


    def _load(self):

        if not self.memory_file.exists():

            return []

        try:

            with open(
                self.memory_file,
                "r",
                encoding="utf-8"
            ) as f:

                data = json.load(f)

                if isinstance(data, list):

                    return data

                if isinstance(data, dict):

                    return data.get(
                        "memories",
                        []
                    )

        except Exception:

            pass


        return []


    def retrieve(self):

        return self.memory


    def add(
        self,
        memory
    ):

        self.memory.append(
            memory
        )

        self._save()


    def store(
        self,
        memory
    ):

        self.add(
            memory
        )


    def _save(self):

        self.memory_file.parent.mkdir(
            exist_ok=True
        )

        with open(
            self.memory_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.memory,
                f,
                indent=4
            )


    def search(
        self,
        query
    ):

        query = query.lower()

        return [
            item
            for item in self.memory
            if query in str(item).lower()
        ]