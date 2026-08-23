from content_engine.agents.base_manager import (
    BaseManager
)

from content_engine.agents.intelligence.memory_agent import (
    MemoryAgent
)

from content_engine.agents.quality.hook_similarity_agent import (
    HookSimilarityAgent
)


class ContentMemoryManager(BaseManager):

    def __init__(self):

        self.memory = MemoryAgent()

        self.similarity = HookSimilarityAgent()


    def store(
        self,
        content
    ):

        self.memory.add(
            content
        )


    def retrieve(
        self
    ):

        return (
            self.memory.retrieve()
        )


    def remember_success(
        self,
        hook,
        topic,
        hashtags,
        cta,
        platform,
        score
    ):

        self.store(

            {

                "hook": hook,

                "topic": topic,

                "hashtags": hashtags,

                "cta": cta,

                "platform": platform,

                "score": score

            }

        )


    def remember_failure(
        self,
        hook
    ):

        self.store(

            {

                "hook": hook,

                "rejected": True

            }

        )


    def save_successful_content(
        self,
        row,
        text,
        optimization,
        review,
        quality
    ):

        if review["score"] < 90:

            return


        lines = text.splitlines()

        hook = ""


        for line in lines:

            cleaned = line.strip()

            if len(cleaned) < 30:

                continue

            hook = cleaned

            break


        hook = quality.clean_hook(
            hook
        )

        hook_score = quality.score_hook(
            hook
        )


        if hook_score < 50:

            return


        self.remember_success(

            hook=hook,

            topic=row["topic"],

            hashtags=optimization["hashtags"],

            cta=optimization["follow_cta"],

            platform=row["platform"],

            score=review["score"]

        )


    def get_prompt_context(
        self
    ):

        memories = self.retrieve()


        recent_topics = []

        recent_hooks = []

        rejected_phrases = []


        for item in memories:

            if not isinstance(
                item,
                dict
            ):

                continue


            if "topic" in item:

                recent_topics.append(
                    item["topic"]
                )


            if "hook" in item:

                recent_hooks.append(
                    item["hook"]
                )


            if "rejected_phrases" in item:

                rejected_phrases.extend(
                    item["rejected_phrases"]
                )


        return {

            "recent_topics":
                recent_topics[-10:],


            "recent_hooks":
                recent_hooks[-10:],


            "rejected_phrases":
                rejected_phrases[-10:]

        }