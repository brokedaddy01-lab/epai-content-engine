from content_engine.agents.intelligence.learning_agent import (
    LearningAgent
)

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

from content_engine.agents.intelligence.feedback_loop_agent import (
    FeedbackLoopAgent
)

from content_engine.agents.strategy.topic_cluster_agent import (
    TopicClusterAgent
)



class IntelligenceBrain:


    def __init__(self):

        self.learning = LearningAgent()

        self.performance = PerformanceAgent()

        self.performance_learning = (
            PerformanceLearningAgent()
        )

        self.memory = ContentMemoryManager()

        self.feedback = FeedbackAgent()

        self.feedback_loop = FeedbackLoopAgent()

        self.knowledge = KnowledgeAgent()

        self.clusters = TopicClusterAgent()



    ##################################################
    # MEMORY CONTEXT
    ##################################################

    def memory_context(self):

        return (
            self.memory
            .get_prompt_context()
        )



    ##################################################
    # SAVE SUCCESSFUL CONTENT
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

        self.memory.remember_success(

            hook=hook,

            topic=topic,

            hashtags=hashtags,

            cta=cta,

            platform=platform,

            score=score

        )



    ##################################################
    # LEARNING
    ##################################################

    def remember(
        self,
        topic,
        score,
        platform
    ):

        self.learning.learn(

            topic,

            score,

            platform

        )



    ##################################################
    # PERFORMANCE
    ##################################################

    def best_content(self):

        return (
            self.performance
            .best_posts()
        )



    ##################################################
    # PERFORMANCE ANALYSIS
    ##################################################

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



    ##################################################
    # FEEDBACK
    ##################################################

    def feedback_agent(self):

        return self.feedback



    ##################################################
    # KNOWLEDGE
    ##################################################

    def knowledge_agent(self):

        return self.knowledge



    ##################################################
    # FEEDBACK LOOP
    ##################################################

    def feedback_loop_agent(self):

        return self.feedback_loop



    ##################################################
    # TOPIC CLUSTERS
    ##################################################

    def topic_clusters(self):

        return self.clusters