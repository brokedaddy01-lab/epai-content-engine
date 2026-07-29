from content_engine.agents.intelligence.intelligence_manager import (
    IntelligenceManager
)

from content_engine.agents.strategy.topic_cluster_agent import (
    TopicClusterAgent
)



class IntelligenceBrain:


    def __init__(
        self,
        manager=None
    ):


        if manager is None:

            self.manager = IntelligenceManager()

        else:

            self.manager = manager



        # Compatibility aliases.
        # Existing callers expect direct access.

        self.performance = (
            self.manager.performance
        )


        self.performance_learning = (
            self.manager.learning
        )


        self.memory = (
            self.manager.content_memory
        )


        self.feedback = (
            self.manager.feedback
        )



        # Compatibility alias.
        # Previous architecture exposed feedback_loop.
        # FeedbackLoopAgent was merged into FeedbackAgent.

        self.feedback_loop = (
            self.feedback
        )



        self.knowledge = (
            self.manager.knowledge
        )



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

        return (
            self.manager
            .remember_content(
                hook,
                topic,
                hashtags,
                cta,
                platform,
                score
            )
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