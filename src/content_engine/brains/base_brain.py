class BaseBrain:


    """
    Base class for all EPAI Content Engine brains.

    Provides shared foundation for:
    - lifecycle management
    - future logging
    - metrics
    - tracing
    - configuration injection
    """



    def __init__(

        self

    ):

        pass



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