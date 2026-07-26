from content_engine.agents.intelligence.memory_agent import (
    MemoryAgent
)

from content_engine.agents.hook_similarity_agent import (
    HookSimilarityAgent
)


class ContentMemoryManager:


    def __init__(

        self

    ):

        self.memory = MemoryAgent()

        self.similarity = HookSimilarityAgent()



    def get_prompt_context(

        self

    ):

        data = self.memory.load()


        return {

            "recent_hooks":

                self.get_recent_hooks(
                    data
                ),


            "recent_topics":

                data.get(
                    "successful_topics",
                    []
                )[-10:],


            "rejected_phrases":

                data.get(
                    "rejected_phrases",
                    []
                )[-10:]

        }



    def get_recent_hooks(

        self,

        data

    ):


        hooks = data.get(

            "successful_hooks",

            []

        )


        cleaned = []


        for hook in hooks:


            if isinstance(

                hook,

                dict

            ):


                cleaned.append(

                    hook.get(

                        "text",

                        ""

                    )

                )


            else:


                cleaned.append(

                    hook

                )


        return cleaned[-10:]



    def remember_success(

        self,

        hook=None,

        topic=None,

        hashtags=None,

        cta=None,

        platform=None,

        score=None

    ):


        data = self.memory.load()



        if hook:


            data.setdefault(

                "successful_hooks",

                []

            )


            existing = None


            for item in data[

                "successful_hooks"

            ]:


                existing_text = ""


                if isinstance(

                    item,

                    dict

                ):

                    existing_text = item.get(

                        "text",

                        ""

                    )


                else:

                    existing_text = item



                if self.similarity.is_similar(

                    hook,

                    existing_text

                ):


                    existing = item

                    break



            if existing:


                if isinstance(

                    existing,

                    dict

                ):


                    existing["uses"] = (

                        existing.get(

                            "uses",

                            1

                        )

                        +

                        1

                    )


                    if score:


                        old_score = existing.get(

                            "avg_score",

                            score

                        )


                        existing["avg_score"] = round(

                            (

                                old_score

                                +

                                score

                            )

                            /

                            2,

                            2

                        )


            else:


                data[

                    "successful_hooks"

                ].append(

                    {

                        "text": hook,

                        "uses": 1,

                        "avg_score": score or 0

                    }

                )



        if topic:


            data.setdefault(

                "successful_topics",

                []

            )


            if topic not in data[

                "successful_topics"

            ]:


                data[

                    "successful_topics"

                ].append(

                    topic

                )



        if hashtags:


            data.setdefault(

                "successful_hashtags",

                {}

            )


            if isinstance(

                data[

                    "successful_hashtags"

                ],

                list

            ):


                old = data[

                    "successful_hashtags"

                ]


                data[

                    "successful_hashtags"

                ] = {}


                for tag in old:


                    data[

                        "successful_hashtags"

                    ][tag] = (

                        data[

                            "successful_hashtags"

                        ].get(

                            tag,

                            0

                        )

                        +

                        1

                    )



            for tag in hashtags:


                data[

                    "successful_hashtags"

                ][tag] = (

                    data[

                        "successful_hashtags"

                    ].get(

                        tag,

                        0

                    )

                    +

                    1

                )



        if cta:


            data.setdefault(

                "successful_ctas",

                {}

            )


            if isinstance(

                data[

                    "successful_ctas"

                ],

                list

            ):


                old = data[

                    "successful_ctas"

                ]


                data[

                    "successful_ctas"

                ] = {}


                for item in old:


                    data[

                        "successful_ctas"

                    ][item] = (

                        data[

                            "successful_ctas"

                        ].get(

                            item,

                            0

                        )

                        +

                        1

                    )



            cta = cta.strip()


            data[

                "successful_ctas"

            ][cta] = (

                data[

                    "successful_ctas"

                ].get(

                    cta,

                    0

                )

                +

                1

            )



        if platform and score:


            data.setdefault(

                "platform_performance",

                {}

            )


            data[

                "platform_performance"

            ].setdefault(

                platform,

                []

            )


            data[

                "platform_performance"

            ][platform].append(

                {

                    "score": score

                }

            )



        self.memory.save(

            data

        )