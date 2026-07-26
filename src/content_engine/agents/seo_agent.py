class SEOAgent:

    def optimize(

        self,
        content,
        keyword

    ):

        semantic = [

            "discipline",
            "self improvement",
            "leadership",
            "consistency",
            "mental toughness",
            "habits",
            "stoicism",
            "personal growth"
        ]

        instructions = f"""

Primary Keyword:

{keyword}

Semantic Keywords:

{", ".join(semantic)}

Goals:

- naturally repeat keyword
- improve discoverability
- improve LinkedIn SEO
- improve YouTube searchability
- improve TikTok search

"""

        return instructions