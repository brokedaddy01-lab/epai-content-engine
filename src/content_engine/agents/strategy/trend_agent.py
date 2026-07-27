class TrendAgent:


    def __init__(self):

        self.core_topics = [

            "discipline",

            "masculinity",

            "self mastery",

            "mental toughness",

            "high performance",

            "entrepreneurship",

            "leadership",

            "fitness",

            "AI productivity",

            "financial growth"

        ]


    ##################################################
    # BASE TOPICS
    ##################################################

    def get_topics(self):

        return self.core_topics



    ##################################################
    # MERGE SCRAPED TRENDS
    ##################################################

    def analyze(

        self,

        scraped_trends=None

    ):

        topics = list(
            self.core_topics
        )


        if scraped_trends:

            for platform, values in scraped_trends.items():

                for item in values:

                    if item not in topics:

                        topics.append(
                            item
                        )


        return topics



    ##################################################
    # TOP TREND CATEGORIES
    ##################################################

    def prioritize(

        self,

        scraped_trends=None

    ):

        topics = self.analyze(
            scraped_trends
        )


        return {

            "priority_topics":
                topics[:10],

            "total_topics":
                len(topics)

        }