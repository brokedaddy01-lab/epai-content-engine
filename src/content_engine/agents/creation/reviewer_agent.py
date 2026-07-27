class ReviewerAgent:


    def review(

        self,

        text

    ):

        issues = []


        lower = text.lower()


        metrics = {

            "hook_score": 0,

            "discipline_score": 0,

            "operator_score": 0,

            "stoic_score": 0,

            "tribe_score": 0,

            "virality_score": 0,

            "cta_score": 0,

            "quality_score": 0

        }


        score = 100



        ##################################################
        # HOOK
        ##################################################

        first_lines = " ".join(
            text.splitlines()[:5]
        ).lower()


        hook_patterns = [

            "most people",
            "nobody",
            "stop",
            "truth",
            "hard truth",
            "you think",
            "discipline"

        ]


        for phrase in hook_patterns:

            if phrase in first_lines:

                metrics["hook_score"] += 10


        if metrics["hook_score"] < 20:

            issues.append(
                "Hook lacks emotional tension"
            )



        ##################################################
        # BRAND SIGNALS
        ##################################################

        categories = {

            "discipline_score":[

                "discipline",
                "consistency",
                "execution",
                "standards",
                "protocol",
                "habits"

            ],

            "operator_score":[

                "operator",
                "mission",
                "ownership",
                "systems",
                "responsibility"

            ],

            "stoic_score":[

                "stoic",
                "stoicism",
                "control",
                "virtue",
                "character"

            ],

            "tribe_score":[

                "brotherhood",
                "family",
                "tribe",
                "legacy",
                "community"

            ],

            "virality_score":[

                "most people",
                "nobody",
                "truth",
                "you"

            ],

            "cta_score":[

                "comment",
                "share",
                "follow",
                "subscribe",
                "thoughts"

            ]

        }


        for metric, words in categories.items():

            for word in words:

                if word in lower:

                    metrics[metric] += 10



        ##################################################
        # AI / GENERIC DETECTION
        ##################################################

        banned = [

            "believe in yourself",
            "dream big",
            "you got this",
            "here's the thing",
            "as we all know",
            "take action today"

        ]


        for phrase in banned:

            if phrase in lower:

                score -= 8

                issues.append(
                    f"Remove generic phrase: {phrase}"
                )



        ##################################################
        # PRACTICAL VALUE
        ##################################################

        action_words = [

            "step",
            "protocol",
            "system",
            "routine",
            "build",
            "create"

        ]


        if any(
            word in lower
            for word in action_words
        ):

            metrics["quality_score"] += 10

        else:

            score -= 10

            issues.append(
                "Needs practical action steps"
            )



        ##################################################
        # LENGTH
        ##################################################

        count = len(
            text.split()
        )


        if count < 120:

            score -= 5

            issues.append(
                "Content too short"
            )


        if count > 500:

            score -= 5

            issues.append(
                "Content too long"
            )



        ##################################################
        # CTA
        ##################################################

        if metrics["cta_score"] == 0:

            score -= 10

            issues.append(
                "Missing engagement CTA"
            )



        ##################################################
        # FINAL SCORE
        ##################################################

        bonus = (

            metrics["hook_score"]

            +

            metrics["discipline_score"]

            +

            metrics["operator_score"]

            +

            metrics["stoic_score"]

            +

            metrics["tribe_score"]

            +

            metrics["virality_score"]

            +

            metrics["cta_score"]

        ) // 10



        final_score = max(

            0,

            min(

                score + bonus,

                100

            )

        )


        metrics["quality_score"] = final_score


        return {

            "score":
                final_score,

            "issues":
                issues,

            "metrics":
                metrics

        }