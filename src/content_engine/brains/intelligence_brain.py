from content_engine.agents.intelligence.performance_agent import (
    PerformanceAgent
)

from content_engine.agents.intelligence.performance_learning_agent import (
    PerformanceLearningAgent
)

from content_engine.agents.intelligence.content_memory_manager import (
    ContentMemoryManager
)

from content_engine.agents.intelligence.feedback_agent import (
    FeedbackAgent
)

from content_engine.agents.intelligence.knowledge_agent import (
    KnowledgeAgent
)

from content_engine.agents.strategy.topic_cluster_agent import (
    TopicClusterAgent
)


class IntelligenceBrain:


    def __init__(self):

        self.performance = PerformanceAgent()

        self.performance_learning = (
            PerformanceLearningAgent()
        )

        self.memory = ContentMemoryManager()

        self.feedback = FeedbackAgent()

        # Compatibility alias.
        # Previous architecture exposed feedback_loop.
        # FeedbackLoopAgent was merged into FeedbackAgent.
        self.feedback_loop = self.feedback

        self.knowledge = KnowledgeAgent()


        # Compatibility alias.
        # TopicClusterAgent ownership moved to StrategyBrain,
        # but older callers/tests still access IntelligenceBrain.clusters.
        self.clusters = TopicClusterAgent()



    def memory_context(self):

        return (
            self.memory
            .get_prompt_context()
        )



    def remember_content(
        self,
        hook,
        topic,
        hashtags,
        cta,
        platform,
        score
    ):

        self.memory.remember_success(

            hook=hook,

            topic=topic,

            hashtags=hashtags,

            cta=cta,

            platform=platform,

            score=score

        )



    def best_content(self):

        return (
            self.performance
            .best_posts()
        )



    def analyze_performance(
        self,
        memory_data
    ):

        return (
            self.performance_learning
            .learn(
                memory_data
            )
        )



    def feedback_agent(self):

        return self.feedback



    def feedback_loop_agent(self):

        return self.feedback



    def knowledge_agent(self):

        return self.knowledge



    def topic_clusters(self):

        return self.clusters