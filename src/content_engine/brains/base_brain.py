class BaseBrain:

    manager_class = None

    def create_manager(self):

        if self.manager_class is None:

            raise NotImplementedError(
                "manager_class must be defined."
            )

        return self.manager_class()

    def __init__(

        self,

        manager=None

    ):

        self.manager = (

            manager

            if manager is not None

            else self.create_manager()

        )

    def __getattr__(

        self,

        name

    ):

        if hasattr(

            self.manager,

            name

        ):

            return getattr(

                self.manager,

                name

            )

        raise AttributeError(

            f"{self.__class__.__name__} has no attribute '{name}'"

        )