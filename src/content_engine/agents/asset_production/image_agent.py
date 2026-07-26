class ImageAgent:

    def generate_prompt(
        self,
        post
    ):

        prompt = f"""
Create an image concept.

Brand:

Protocol X

Style:

Dark.

Masculine.

Cinematic.

Themes:

Functional strength.

Stoicism.

Brotherhood.

Discipline.

Viking symbolism.

Wolf symbolism.

Leadership.

Legacy.

Content:

{post}
"""

        return prompt