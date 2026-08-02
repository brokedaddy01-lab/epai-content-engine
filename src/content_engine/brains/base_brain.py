class BaseBrain:


    manager_class = None



    def __init__(

        self,

        manager=None

    ):


        if manager is not None:

            self.manager = manager

            return


        self.manager = self.create_manager()



    def create_manager(self):


        if self.manager_class is None:

            raise ValueError(

                "manager_class must be defined"

            )


        try:

            return self.manager_class()

        except TypeError as error:

            raise TypeError(

                f"{self.manager_class.__name__} requires dependency injection. "

                "Provide a manager instance."

            ) from error