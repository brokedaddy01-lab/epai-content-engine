class ViralityPredictionAgent:


    def predict(
        self,
        review,
        viral,
        platform
    ):


        score = 50


        score += (

            review.get(
                "score",
                0
            )

            *

            .30

        )


        score += (

            viral.get(
                "virality_score",
                0
            )

            *

            .20

        )


        return {


            "platform":

                platform,


            "viral_probability":

                round(

                    score,

                    2

                )

        }