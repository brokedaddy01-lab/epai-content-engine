class ReviewerAgent:


    def review(
        self,
        text
    ):

        issues = []


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


        lower = text.lower()



        ####################################################
        # HOOK EVALUATION
        ####################################################

        first_lines = (
            text.splitlines()[:5]
        )

        hook_text = " ".join(
            first_lines
        ).lower()


        hook_patterns = [

            "most people",

            "nobody",

            "stop",

            "the truth",

            "hard truth",

            "you think",

            "your",

            "discipline"

        ]


        for phrase in hook_patterns:

            if phrase in hook_text:

                metrics["hook_score"] += 10



        if metrics["hook_score"] < 20:

            issues.append(
                "Hook lacks emotional tension"
            )



        ####################################################
        # BRAND ALIGNMENT
        ####################################################

        discipline_words = [

            "discipline",

            "consistency",

            "execution",

            "standards",

            "protocol",

            "habits",

            "self discipline"

        ]


        operator_words = [

            "operator",

            "mission",

            "responsibility",

            "ownership",

            "execute",

            "systems",

            "protocols"

        ]


        stoic_words = [

            "stoic",

            "stoicism",

            "control",

            "virtue",

            "character",

            "actions",

            "standards"

        ]


        tribe_words = [

            "brotherhood",

            "family",

            "tribe",

            "legacy",

            "pack",

            "community"

        ]


        viral_words = [

            "most people",

            "nobody",

            "you",

            "stop",

            "truth"

        ]


        cta_words = [

            "comment",

            "share",

            "follow",

            "subscribe",

            "reflect",

            "your thoughts"

        ]



        for word in discipline_words:

            if word in lower:

                metrics["discipline_score"] += 10



        for word in operator_words:

            if word in lower:

                metrics["operator_score"] += 10



        for word in stoic_words:

            if word in lower:

                metrics["stoic_score"] += 10



        for word in tribe_words:

            if word in lower:

                metrics["tribe_score"] += 10



        for word in viral_words:

            if word in lower:

                metrics["virality_score"] += 10



        for word in cta_words:

            if word in lower:

                metrics["cta_score"] += 10



        ####################################################
        # GENERIC AI LANGUAGE PENALTIES
        ####################################################

        banned_phrases = [

            "believe in yourself",

            "dream big",

            "manifest",

            "you got this",

            "here's the thing",

            "as we all know",

            "success isn't easy",

            "my friends",

            "newsflash",

            "what if you're not motivated",

            "fleeting feeling",

            "foundation of success",

            "take action today"

        ]



        score = 100



        for phrase in banned_phrases:

            if phrase in lower:

                score -= 8

                issues.append(
                    f"Remove generic phrase: {phrase}"
                )



        ####################################################
        # AI SELF EXPLANATION DETECTION
        ####################################################

        ai_leak_patterns = [

            "this post meets",

            "this content meets",

            "the tone is",

            "the language is",

            "the requirements",

            "the post also includes"

        ]


        for phrase in ai_leak_patterns:

            if phrase in lower:

                score -= 20

                issues.append(
                    "Remove AI explanation"
                )



        ####################################################
        # PRACTICAL VALUE CHECK
        ####################################################

        action_words = [

            "step",

            "protocol",

            "system",

            "routine",

            "create",

            "build",

            "identify"

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



        ####################################################
        # LENGTH CHECK
        ####################################################

        word_count = len(
            text.split()
        )


        if word_count < 120:

            score -= 5

            issues.append(
                "Content is too short"
            )


        if word_count > 500:

            score -= 5

            issues.append(
                "Content is too long"
            )



        ####################################################
        # CTA CHECK
        ####################################################

        if not any(
            word in lower
            for word in cta_words
        ):

            score -= 10

            issues.append(
                "Missing engagement CTA"
            )



        ####################################################
        # FINAL SCORE
        ####################################################

        alignment_bonus = (

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



        final_score = score + alignment_bonus



        final_score = max(
            0,
            min(
                final_score,
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