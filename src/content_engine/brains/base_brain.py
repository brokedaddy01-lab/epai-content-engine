class BaseBrain:


    """
    Base class for all EPAI Content Engine brains.

    Provides shared foundation for:
    - manager lifecycle
    - future logging
    - metrics
    - tracing
    - configuration injection
    """


    manager_class = None



    def __init__(

        self,

        manager=None

    ):

        if manager is not None:

            self.manager = manager

        else:

            if self.manager_class is None:

                raise ValueError(
                    "Brain must define manager_class"
                )


            self.manager = (
                self.manager_class()
            )



    ##################################################
    # HEALTH CHECK
    ##################################################

    def health_check(

        self

    ):

        return {

            "status":
                "healthy",

            "brain":
                self.__class__.__name__

        }