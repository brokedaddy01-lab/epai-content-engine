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



            if not values:

                continue



            summary[platform] = {


                "posts":

                    len(values),



                "average_score":

                    round(

                        sum(values)

                        /

                        len(values),

                        2

                    ),



                "best_score":

                    max(values),



                "worst_score":

                    min(values)

            }



        return summary