from content_engine.agents.creation.creation_manager import (
    CreationManager
)


class CreationBrain:


    def __init__(

        self,

        quality_threshold=90,

        max_attempts=3

    ):


        self.manager = CreationManager(

            quality_threshold,

            max_attempts

        )


        # Compatibility aliases.
        # Keeps older tests/callers working.

        self.story_engine = (
            self.manager.story_engine
        )

        self.prompt_architect = (
            self.manager.prompt_architect
        )

        self.copywriter = (
            self.manager.copywriter
        )

        self.reviewer = (
            self.manager.reviewer
        )

        self.memory = (
            self.manager.memory
        )



    def create(

        self,

        row,

        brand

    ):

        return (

            self.manager
            .create(

                row,

                brand

            )

        )