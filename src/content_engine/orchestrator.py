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
        # access brain references.

        self.strategy = self.registry.brain(

            "strategy"

        )


        self.creation = self.registry.brain(

            "creation"

        )


        self.intelligence = self.registry.brain(

            "intelligence"

        )


        self.quality = self.registry.brain(

            "quality"

        )


        self.optimization = self.registry.brain(

            "optimization"

        )


        self.production = self.registry.brain(

            "production"

        )


        self.publishing = self.registry.brain(

            "publishing"

        )



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