class PerformanceLearningAgent:


    def learn(
        self,
        data
    ):

        platform_data = data.get(
            "platform_performance",
            {}
        )


        summary = {}


        for platform, scores in platform_data.items():

            if not scores:

                continue


            values = [

                item.get(
                    "score",
                    0
                )

                for item in scores

            ]


            average = round(

                sum(values)

                /

                len(values),

                2

            )


            highest = max(values)

            lowest = min(values)


            summary[platform] = {

                "posts":

                    len(values),

                "average_score":

                    average,

                "best_score":

                    highest,

                "worst_score":

                    lowest

            }


        return summary