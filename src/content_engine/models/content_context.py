class ContentContext:


    def __init__(

        self,

        topic="",

        platform="",

        brand=None,

        content="",

        metadata=None

    ):

        self.topic = topic

        self.platform = platform

        self.brand = brand or {}

        self.content = content

        self.metadata = metadata or {}



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