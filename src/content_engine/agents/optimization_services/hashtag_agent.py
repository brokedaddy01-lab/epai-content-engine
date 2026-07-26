class HashtagAgent:

    def generate(

        self,
        topic,
        platform
    ):

        base = [

            "#Discipline",
            "#SelfImprovement",
            "#Leadership",
            "#PersonalDevelopment",
            "#MentalToughness",
            "#SuccessMindset"
        ]

        protocol = [

            "#ProtocolX",
            "#OperatorMindset",
            "#DisciplineOverMotivation"
        ]

        if platform in [

            "instagram",
            "tiktok"
        ]:

            base += [

                "#Motivation",
                "#MensMentalHealth",
                "#GrowthMindset",
                "#HighPerformance"
            ]

        return protocol + base