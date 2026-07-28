class HookSimilarityAgent:


    def normalize(
        self,
        text
    ):

        if not text:

            return ""


        text = text.lower()


        remove = [

            "the",
            "your",
            "a",
            "an",
            "of",
            "to",
            "is",
            "and"

        ]


        words = text.split()


        cleaned = []


        for word in words:


            word = (
                word
                .replace(":", "")
                .replace(",", "")
                .replace(".", "")
            )


            if word not in remove:

                cleaned.append(
                    word
                )


        return " ".join(cleaned)



    def similarity(
        self,
        first,
        second
    ):


        first = self.normalize(
            first
        )


        second = self.normalize(
            second
        )


        if not first or not second:

            return 0



        first_words = set(
            first.split()
        )


        second_words = set(
            second.split()
        )



        intersection = (

            first_words
            &
            second_words

        )


        union = (

            first_words
            |
            second_words

        )


        if not union:

            return 0



        word_score = (

            len(intersection)

            /

            len(union)

            *

            100

        )



        first_phrase = first.split()

        second_phrase = second.split()



        phrase_bonus = 0



        for i in range(
            len(first_phrase) - 1
        ):


            pair = (

                first_phrase[i],

                first_phrase[i + 1]

            )


            if (

                pair[0]
                in second_phrase

                and

                pair[1]
                in second_phrase

            ):

                phrase_bonus += 10



        score = word_score + phrase_bonus



        if score > 100:

            score = 100



        return round(
            score,
            2
        )



    def is_similar(
        self,
        new_hook,
        existing_hook,
        threshold=55
    ):


        score = self.similarity(

            new_hook,

            existing_hook

        )


        return score >= threshold