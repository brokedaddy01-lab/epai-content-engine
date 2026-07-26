from content_engine.agents.learning_agent import (
    LearningAgent
)

from content_engine.agents.performance_agent import (
    PerformanceAgent
)

from content_engine.agents.topic_cluster_agent import (
    TopicClusterAgent
)


class ProtocolXBrain:

    def __init__(self):

        self.learning = (
            LearningAgent()
        )

        self.performance = (
            PerformanceAgent()
        )

        self.clusters = (
            TopicClusterAgent()
        )

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

    def best_topics(self):

        return (

            self.performance
            .best_posts()
        )