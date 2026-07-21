class FormatterAgent:

    def format(
        self,
        text,
        platform
    ):

        platform = (
            platform.lower()
        )

        if platform == "linkedin":

            return text

        if platform == "facebook":

            return (
                text
                + "\n\n"
                + "What standard are "
                  "you enforcing today?"
            )

        if platform == "instagram":

            return (
                text
                + "\n\n"
                + "#protocolx "
                + "#discipline "
                + "#operator "
                + "#selfmastery "
                + "#masculinity"
            )

        if platform == "x":

            return text[:280]

        return text