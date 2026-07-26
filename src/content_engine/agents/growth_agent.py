class GrowthAgent:

    def optimize(

        self,

        text,

        platform
    ):

        follow_cta = {

            "linkedin":

                "\n\nFollow Protocol X for disciplined execution and leadership lessons.",

            "facebook":

                "\n\nJoin the Protocol X tribe and share your thoughts below.",

            "instagram":

                "\n\nFollow and save this for later.",

            "x":

                "\n\nRepost if this resonates.",

            "tiktok":

                "\n\nFollow for more operator protocols.",

            "youtube":

                "\n\nSubscribe for weekly Protocol X teachings."
        }

        hashtags = {

            "linkedin": [

                "#Discipline",

                "#Leadership",

                "#SelfImprovement"
            ],

            "facebook": [

                "#ProtocolX",

                "#PersonalGrowth",

                "#Discipline"
            ],

            "instagram": [

                "#Discipline",

                "#Mindset",

                "#Stoicism",

                "#SelfMastery",

                "#Leadership",

                "#Success",

                "#Entrepreneur"
            ],

            "x": [

                "#Discipline",

                "#Stoicism"
            ],

            "tiktok": [

                "#Mindset",

                "#Discipline",

                "#SelfImprovement",

                "#Masculinity",

                "#Motivation",

                "#ProtocolX"
            ],

            "youtube": [

                "#Discipline",

                "#Leadership",

                "#SelfImprovement",

                "#Mindset",

                "#ProtocolX"
            ]
        }

        return {

            "follow_cta":

                follow_cta.get(
                    platform,
                    ""
                ),

            "hashtags":

                hashtags.get(
                    platform,
                    []
                )
        }