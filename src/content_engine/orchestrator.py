from content_engine.registry import (
    ManagerRegistry
)

from content_engine.content_director import (
    ContentDirector
)


class ContentOrchestrator:


    def __init__(self):

        self.registry = ManagerRegistry()


        self.director = ContentDirector(

            self.registry

        )


        # Backwards compatibility
        # Existing tests and callers can still
        # access the Director's brain references.

        self.strategy = self.director.strategy

        self.creation = self.director.creation

        self.intelligence = self.director.intelligence

        self.quality = self.director.quality

        self.optimization = self.director.optimization

        self.production = self.director.production

        self.publishing = self.director.publishing



    def clean_output(

        self,

        text

    ):

        return self.director.clean_output(

            text

        )



    def clean_cta(

        self,

        text

    ):

        return self.director.clean_cta(

            text

        )



    def run(

        self,

        row,

        brand

    ):

        return self.director.run(

            row,

            brand

        )