from content_engine.agents.intelligence.memory_agent import (
    MemoryAgent
)

from content_engine.agents.intelligence.feedback_agent import (
    FeedbackAgent
)

from content_engine.agents.intelligence.performance_agent import (
    PerformanceAgent
)

from content_engine.agents.intelligence.performance_learning_agent import (
    PerformanceLearningAgent
)

from content_engine.agents.intelligence.knowledge_agent import (
    KnowledgeAgent
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)

from content_engine.agents.base_manager import BaseManager


class IntelligenceManager(BaseManager):


    def __init__(self):

        self.content_memory = ContentMemoryManager()

        self.memory = MemoryAgent()

        self.feedback = FeedbackAgent(

            self.content_memory

        )

        self.performance = PerformanceAgent()

        self.learning = PerformanceLearningAgent()

        self.knowledge = KnowledgeAgent()



    ##################################################
    # MEMORY
    ##################################################

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

            hook=hook,

            topic=topic,

            hashtags=hashtags,

            cta=cta,

            platform=platform,

            score=score

        )



    def remember_failure(

        self,

        hook

    ):

        return self.content_memory.remember_failure(

            hook

        )



    def prompt_context(

        self

    ):

        return self.content_memory.get_prompt_context()



    ##################################################
    # FEEDBACK
    ##################################################

    def learn(

        self,

        review,

        row

    ):

        return self.feedback.learn(

            review,

            row

        )



    ##################################################
    # KNOWLEDGE
    ##################################################

    def search(

        self,

        query

    ):

        return self.knowledge.search(

            query

        )



    ##################################################
    # PERFORMANCE
    ##################################################

    def performance_summary(

        self

    ):

        return self.performance.summary()



    def learn_from_performance(

        self,

        data

    ):

        return self.learning.learn(

            data

        )