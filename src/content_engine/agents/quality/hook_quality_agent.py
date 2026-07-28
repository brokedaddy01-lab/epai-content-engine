class HookQualityAgent:


    def score(
        self,
        hook
    ):

        if not hook:

            return 0



        score = 100


        text = hook.strip()


        lower = text.lower()



        ################################################
        # LENGTH CHECKS
        ################################################

        if len(text) < 25:

            score -= 40



        if len(text) > 90:

            score -= 40



        ################################################
        # SENTENCE CHECK
        ################################################

        sentence_count = (
            text.count(".")
            +
            text.count("!")
            +
            text.count("?")
        )


        if sentence_count > 1:

            score -= 50



        ################################################
        # METADATA / AI OUTPUT BLOCKS
        ################################################

        blocked = [

            "as leaders",

            "we must recognize",

            "our actions are",

            "i cannot",

            "i can't",

            "i would be happy",

            "here is",

            "here's",

            "as an ai",

            "i am an ai",

            "the following",

            "seo keyword",

            "seo keywords",

            "keyword:",

            "keywords:",

            "topic:",

            "title:",

            "headline:",

            "caption:",

            "script:",

            "video:",

            "content:",

            "post:",

            "description:",

            "hashtags:",

            "instructions:",

            "requirements:",

            "guidelines:",

            "assistant",

            "chatgpt",

            "openai",

            "artificial intelligence"

        ]



        for phrase in blocked:

            if phrase in lower:

                score -= 100



        ################################################
        # MARKDOWN PENALTY
        ################################################

        if "**" in text:

            score -= 5



        ################################################
        # STRONG HOOK PATTERNS
        ################################################

        strong_patterns = [

            "the truth",

            "the unspoken",

            "stop",

            "your",

            "discipline",

            "consistency",

            "standards",

            "leadership",

            "execution",

            "mastery",

            "future",

            "identity",

            "systems"

        ]


        for pattern in strong_patterns:

            if pattern in lower:

                score += 5



        ################################################
        # HOOK SHOULD SOUND LIKE A TITLE / IDEA
        ################################################

        weak_patterns = [

            "personal growth habits",

            "growth habits",

            "weekly",

            "schedule",

            "calendar",

            "seo",

            "keyword",

            "template",

            "example"

        ]


        for pattern in weak_patterns:

            if pattern in lower:

                score -= 80



        ################################################
        # FINAL LIMITS
        ################################################

        if score > 100:

            score = 100



        if score < 0:

            score = 0



        return score