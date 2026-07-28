class CTAAgent:

    def generate(

        self,
        platform
    ):

        ctas = {

            "linkedin":

                "Follow Protocol X for practical lessons on discipline and execution.",

            "facebook":

                "Comment 'PROTOCOL' if this resonated with you.",

            "instagram":

                "Save this and follow for more.",

            "x":

                "Repost if you needed this reminder.",

            "tiktok":

                "Follow for more operator protocols.",

            "youtube":

                "Subscribe for weekly discipline systems."
        }

        return ctas.get(

            platform,

            "Follow Protocol X."
        )