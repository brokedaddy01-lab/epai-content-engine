class SchedulerAgent:


    def best_times(

        self,

        platform

    ):

        defaults = {


            "linkedin":

                "07:00 AM",


            "facebook":

                "08:00 PM",


            "instagram":

                "07:30 PM",


            "x":

                "08:00 AM",


            "tiktok":

                "09:00 PM",


            "youtube":

                "05:00 PM"

        }


        return defaults.get(

            platform,

            "08:00 AM"

        )



    def schedule(

        self,

        content,

        platform,

        date

    ):

        return {


            "status":

                "scheduled",


            "platform":

                platform,


            "date":

                date,


            "recommended_time":

                self.best_times(

                    platform

                )

        }