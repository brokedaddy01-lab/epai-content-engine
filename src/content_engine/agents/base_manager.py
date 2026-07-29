class BaseManager:
    """
    Base class for all managers.

    Provides a common parent so every manager shares the
    same interface and can grow consistently.
    """

    VERSION = "1.0"

    def name(self):

        return self.__class__.__name__

    def version(self):

        return self.VERSION

    def health(self):

        return {

            "manager": self.name(),

            "status": "healthy",

            "version": self.version()

        }