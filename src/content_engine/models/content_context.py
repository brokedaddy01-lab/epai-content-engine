from dataclasses import dataclass, field


@dataclass
class ContentContext:


    topic: str = ""

    platform: str = ""

    brand: dict = field(
        default_factory=dict
    )

    content: str = ""

    metadata: dict = field(
        default_factory=dict
    )


    def update_content(
        self,
        content
    ):

        self.content = content



    def add_metadata(
        self,
        key,
        value
    ):

        self.metadata[key] = value



    def to_dict(
        self
    ):

        return {

            "topic":
                self.topic,

            "platform":
                self.platform,

            "brand":
                self.brand,

            "content":
                self.content,

            "metadata":
                self.metadata

        }