class GrowthAgent:


    def optimize(

        self,

        content,

        platform

    ):


        recommendations = []


        length = len(
            content.split()
        )


        if length < 100:

            recommendations.append(
                "Increase content depth and storytelling."
            )


        if length > 600:

            recommendations.append(
                "Consider shortening for higher retention."
            )


        if "?" not in content:

            recommendations.append(
                "Add a question to encourage comments."
            )


        return {


            "platform":

                platform,


            "recommendations":

                recommendations,


            "growth_score":

                max(

                    100 -

                    len(recommendations) * 10,

                    0

                )

        }