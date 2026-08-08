import re


class ContentCleaner:

    def clean_output(self, text):

        remove_patterns = [
            r"^Here is the.*?:\s*",
            r"^Here'?s the.*?:\s*",
            r"^Final Post:\s*",
            r"^Analysis:\s*",
            r"^Explanation:\s*",
            r"^The following.*?:\s*",
            r"^Below is.*?:\s*"
        ]

        for pattern in remove_patterns:

            text = re.sub(
                pattern,
                "",
                text,
                flags=re.IGNORECASE | re.MULTILINE
            )

        banned_phrases = [
            "Newsflash:",
            "Here's the thing:",
            "Here's the hard truth:",
            "As we all know,",
            "My friends,"
        ]

        for phrase in banned_phrases:

            text = text.replace(
                phrase,
                ""
            )

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text
        )

        return text.strip()

    def clean_cta(self, text):

        lines = text.splitlines()

        seen = False

        cleaned = []

        for line in lines:

            if "follow protocol x" in line.lower():

                if seen:

                    continue

                seen = True

            cleaned.append(line)

        return "\n".join(cleaned).strip()