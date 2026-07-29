from content_engine.agents.intelligence.memory_agent import (
    MemoryAgent
)

from content_engine.agents.intelligence.knowledge_agent import (
    KnowledgeAgent
)

from content_engine.agents.intelligence.performance_agent import (
    PerformanceAgent
)

from content_engine.agents.intelligence.performance_learning_agent import (
    PerformanceLearningAgent
)

from content_engine.agents.intelligence.feedback_agent import (
    FeedbackAgent
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)

from content_engine.agents.base_manager import BaseManager


class IntelligenceManager(BaseManager):


    def __init__(self):

        self.memory = MemoryAgent()

        self.knowledge = KnowledgeAgent()

        self.performance = PerformanceAgent()

        self.learning = PerformanceLearningAgent()

        self.feedback = FeedbackAgent()

        self.content_memory = ContentMemoryManager()



    def remember_content(
        self,
        hook,
        topic,
        hashtags,
        cta,
        platform,
        score
    ):

        return self.content_memory.remember_success(
            hook,
            topic,
            hashtags,
            cta,
            platform,
            score
        )



    def retrieve_memory(self):

        return self.content_memory.retrieve()



    def get_context(self):

        return self.content_memory.get_prompt_context()