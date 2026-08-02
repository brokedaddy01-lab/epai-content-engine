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
        # These remain temporarily because tests,
        # orchestrator, and existing integrations
        # still reference these names.
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

        return self.manager.remember_content(

            hook,

            topic,

            hashtags,

            cta,

            platform,

            score

        )



    def remember_failure(

        self,

        hook

    ):

        return self.manager.remember_failure(

            hook

        )



    def prompt_context(

        self

    ):

        return self.manager.prompt_context()



    ##################################################
    # FEEDBACK
    ##################################################

    def learn(

        self,

        review,

        row

    ):

        return self.manager.learn(

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

        return self.manager.search(

            query

        )



    ##################################################
    # PERFORMANCE
    ##################################################

    def performance_summary(

        self

    ):

        return self.manager.performance_summary()



    def learn_from_performance(

        self,

        data

    ):

        return self.manager.learn_from_performance(

            data

        )