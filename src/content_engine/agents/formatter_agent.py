class FormatterAgent:

    def format(
        self,
        text,
        platform
    ):

        platform = platform.lower()

        if platform == "linkedin":

            return text

        if platform == "facebook":

            return (
                text
                +
                "\n\nWhat standard are "
                "you enforcing today?"
            )

        if platform == "instagram":

            return (
                text
                +
                "\n\n"
                "#protocolx "
                "#discipline "
                "#operator "
                "#selfmastery"
            )

        if platform == "x":

            return text[:280]

        if platform == "tiktok":

            return (
                text
                +
                "\n\n"
                "Follow @ProtocolX "
                "for daily standards."
            )

        if platform == "youtube":

            return (
                text
                +
                "\n\nSubscribe for "
                "more Protocol X content."
            )

        return text