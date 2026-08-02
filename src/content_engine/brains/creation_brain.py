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



    def create(

        self,

        row,

        brand

    ):

        return self.manager.create(

            row,

            brand

        )