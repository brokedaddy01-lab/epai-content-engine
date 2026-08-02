from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.creation.creation_manager import (
    CreationManager
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)


class CreationBrain(BaseBrain):


    manager_class = CreationManager



    def create_manager(self):

        return self.manager_class(

            ContentMemoryManager()

        )



    def __init__(

        self,

        manager=None,

        quality_threshold=90,

        max_attempts=3

    ):


        super().__init__(

            manager

        )


        # Compatibility aliases

        self.story_engine = (

            self.manager.story_engine

        )


        self.prompt_architect = (

            self.manager.prompt_architect

        )


        self.copywriter = (

            self.manager.copywriter

        )


        self.reviewer = (

            self.manager.reviewer

        )


        self.memory = (

            self.manager.memory

        )



    ##################################################
    # CREATION
    ##################################################

    def create(

        self,

        row,

        brand

    ):

        return (

            self.manager.create(

                row,

                brand

            )

        )