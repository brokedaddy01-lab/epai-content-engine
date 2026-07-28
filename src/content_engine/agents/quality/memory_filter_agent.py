class MemoryFilterAgent:


    def clean_hook(
        self,
        hook
    ):

        if not hook:

            return ""


        blocked_phrases = [

            "here is",

            "here's",

            "final",

            "final post",

            "final content",

            "content:",

            "post:",

            "script:",

            "video:",

            "title:",

            "headline:",

            "seo keyword",

            "keyword:",

            "keywords:",

            "topic:",

            "caption:",

            "description:",

            "hashtags:",

            "i cannot",

            "i can't",

            "i am",

            "i'm",

            "as an",

            "as a",

            "let me",

            "to get started",

            "i understand",

            "requirements",

            "guidelines",

            "instructions",

            "assistant",

            "ai",

            "artificial intelligence",

            "language model",

            "chatgpt",

            "openai",

            "follow protocol",

            "i'd be happy",

            "i would be happy",

            "happy to help",

            "other requests",

            "other questions",

            "sure",

            "absolutely",

            "#"

        ]


        lower = hook.lower()



        for phrase in blocked_phrases:

            if phrase in lower:

                return ""



        hook = hook.replace(
            "**",
            ""
        )


        hook = hook.replace(
            "\"",
            ""
        )


        hook = hook.strip()



        prefixes = [

            "title:",

            "hook:",

            "headline:",

            "opening:"

        ]


        lower_hook = hook.lower()



        for prefix in prefixes:

            if lower_hook.startswith(prefix):

                hook = hook[len(prefix):].strip()

                break



        if len(hook) < 30:

            return ""



        return hook





    def clean_topic(
        self,
        topic
    ):

        if not topic:

            return ""


        topic = topic.strip().lower()


        blocked = [

            "seo",

            "keyword",

            "title",

            "script",

            "video"

        ]


        for phrase in blocked:

            if phrase in topic:

                return ""



        return topic





    def clean_cta(
        self,
        cta
    ):

        if not cta:

            return ""


        cta = cta.strip()


        blocked = [

            "here is",

            "here's",

            "final",

            "content",

            "post",

            "script",

            "assistant",

            "ai",

            "artificial intelligence",

            "seo",

            "keyword"

        ]


        lower = cta.lower()



        for phrase in blocked:

            if phrase in lower:

                return ""



        return cta