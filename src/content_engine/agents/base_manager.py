class BaseManager:
    """
    Base class for all manager classes.

    Provides a common interface for diagnostics,
    versioning, health checks, and runtime
    introspection.
    """

    VERSION = "1.0"

    ##################################################
    # IDENTIFICATION
    ##################################################

    def name(self):

        return self.__class__.__name__

    def version(self):

        return self.VERSION

    ##################################################
    # HEALTH
    ##################################################

    def health(self):

        return {

            "manager": self.name(),

            "status": "healthy",

            "version": self.version()

        }

    ##################################################
    # INTROSPECTION
    ##################################################

    def capabilities(self):

        return [

            name

            for name in dir(self)

            if (

                callable(getattr(self, name))

                and not name.startswith("_")

            )

        ]

    def info(self):

        return {

            "manager": self.name(),

            "version": self.version(),

            "status": "healthy",

            "capabilities": self.capabilities()

        }