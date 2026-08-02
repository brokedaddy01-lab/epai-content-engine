from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)


class BaseBrain:


    manager_class = None



    def __init__(

        self,

        manager=None

    ):


        if manager is not None:

            self.manager = manager


        else:

            self.manager = self.create_manager()



    def create_manager(self):


        if self.manager_class is None:

            raise ValueError(

                "manager_class must be defined"

            )


        try:

            return self.manager_class(

                ContentMemoryManager()

            )


        except TypeError:

            return self.manager_class()