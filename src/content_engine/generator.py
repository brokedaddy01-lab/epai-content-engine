from content_engine.agents.writer_agent import (
    WriterAgent
)

from content_engine.agents.reviewer_agent import (
    ReviewerAgent
)

from content_engine.agents.virality_agent import (
    ViralityAgent
)

from content_engine.agents.growth_agent import (
    GrowthAgent
)

from content_engine.agents.formatter_agent import (
    FormatterAgent
)

from content_engine.agents.image_agent import (
    ImageAgent
)


writer = WriterAgent()

reviewer = ReviewerAgent()

virality = ViralityAgent()

growth = GrowthAgent()

formatter = FormatterAgent()

image_agent = ImageAgent()


def clean_output(text: str):

    replacements = {

        "Here is the final post:": "",

        "Here's the final post:": "",

        "Here is your post:": "",

        "Here's your post:": "",

        "Here is the final Protocol X message:": "",

        "Final Post:": "",

        '"': "",

        "**Final Reflection:**": "",

        "**PROTOCOL X**": ""
    }

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )

    while "  " in text:

        text = text.replace(
            "  ",
            " "
        )

    return text.strip()


def generate_post(
    row,
    brand
):

    response = writer.write(
        row,
        brand
    )

    response = clean_output(
        response
    )

    review = reviewer.review(
        response
    )

    review_score = review.get(
        "score",
        100
    )

    review_issues = review.get(
        "issues",
        []
    )

    #
    # Auto regeneration
    #

    if review_score < 80:

        response = writer.regenerate(

            row,
            brand,
            review_issues
        )

        response = clean_output(
            response
        )

        review = reviewer.review(
            response
        )

    #
    # Virality scoring
    #

    viral = virality.optimize(

        response,

        row["platform"]
    )

    #
    # SEO + growth optimization
    #

    growth_result = growth.optimize(

        response,

        row["platform"]
    )

    #
    # Follow CTA
    #

    if growth_result.get(
        "follow_cta"
    ):

        response += (

            "\n\n"
            +
            growth_result[
                "follow_cta"
            ]
        )

    #
    # Hashtags
    #

    hashtags = growth_result.get(
        "hashtags",
        []
    )

    if hashtags:

        response += (

            "\n\n"
            +
            " ".join(
                hashtags
            )
        )

    #
    # Platform formatting
    #

    formatted = formatter.format(

        response,

        row["platform"]
    )

    #
    # Image generation prompt
    #

    image_prompt = (

        image_agent.generate_prompt(
            formatted
        )
    )

    return {

        "post": formatted,

        "review": review,

        "virality": viral,

        "image_prompt": image_prompt
    }