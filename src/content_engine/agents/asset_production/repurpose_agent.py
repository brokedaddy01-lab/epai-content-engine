class RepurposeAgent:


    def generate(

        self,

        content

    ):

        return {

            "linkedin":

                content,


            "facebook":

                content,


            "x":

                content[:260],


            "instagram":

                content,


            "tiktok":

                content,


            "youtube":

                content

        }


    def repurpose(

        self,

        content

    ):

        return self.generate(

            content

        )