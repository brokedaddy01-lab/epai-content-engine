class BaseBrain:


    """
    Base class for all EPAI Content Engine brains.

    Provides shared foundation for:

    - manager lifecycle
    - dependency injection
    - health checks
    - metadata
    """



    manager_class = None



    def __init__(

        self,

        manager=None

    ):


        if manager is not None:

            self.manager = manager


        elif self.manager_class is not None:

            self.manager = self.manager_class()


        else:

            raise ValueError(

                f"{self.__class__.__name__} "

                "must define manager_class"

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

                self.__class__.__name__,


            "manager":

                self.manager.__class__.__name__

        }



    ##################################################
    # METADATA
    ##################################################

    def info(

        self

    ):


        return {

            "brain":

                self.__class__.__name__,


            "manager":

                self.manager.__class__.__name__

        }