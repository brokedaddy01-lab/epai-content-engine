from content_engine.content_cleaner import (
    ContentCleaner
)


class ContentAssembler:

    def __init__(
        self,
        cleaner=None
    ):

        self.cleaner = (
            cleaner
            if cleaner is not None
            else ContentCleaner()
        )


    def assemble(
        self,
        content,
        optimization
    ):

        response = content

        response += (
            "\n\n"
            +
            optimization["follow_cta"]
        )

        response += (
            "\n\n"
            +
            " ".join(
                optimization["hashtags"]
            )
        )

        response = self.cleaner.clean_output(
            response
        )

        return self.cleaner.clean_cta(
            response
        )
