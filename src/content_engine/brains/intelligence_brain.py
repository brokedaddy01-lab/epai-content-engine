from content_engine.brains.base_brain import (
    BaseBrain
)

from content_engine.agents.intelligence.intelligence_manager import (
    IntelligenceManager
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)


class IntelligenceBrain(BaseBrain):

    manager_class = IntelligenceManager

    def create_manager(self):

        return self.manager_class(
            ContentMemoryManager()
        )

    def __init__(
        self,
        manager=None
    ):

        super().__init__(
            manager
        )

        #
        # Compatibility aliases
        #
        # Managers are now the source of truth.
        # These remain temporarily for existing
        # callers/tests during migration.
        #

        self.content_memory = (
            self.manager.content_memory
        )

        self.memory = (
            self.manager.memory
        )

        self.feedback = (
            self.manager.feedback
        )

        self.feedback_loop = (
            self.manager.feedback
        )

        self.performance = (
            self.manager.performance
        )

        self.performance_learning = (
            self.manager.learning
        )

        self.learning = (
            self.manager.learning
        )

        self.knowledge = (
            self.manager.knowledge
        )

        self.clusters = (
            self.manager.knowledge
        )