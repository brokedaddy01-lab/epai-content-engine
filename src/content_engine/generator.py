import json

from content_engine.agents.writer_agent import (
    WriterAgent
)

from content_engine.agents.reviewer_agent import (
    ReviewerAgent
)

from content_engine.agents.formatter_agent import (
    FormatterAgent
)

from content_engine.agents.image_agent import (
    ImageAgent
)

writer = WriterAgent()

reviewer = ReviewerAgent()

formatter = FormatterAgent()

image_agent = ImageAgent()


def clean_output(text):

    replacements = {

        "Here is the final post:": "",

        "Here's the post:": "",

        '"': ""
    }

    for old, new in replacements.items():

        text = text.replace(
            old,
            new
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

    if review["score"] < 80:

        response = writer.regenerate(

            row,
            brand,
            review["issues"]
        )

        review = reviewer.review(
            response
        )

    formatted = formatter.format(

        response,

        row["platform"]
    )

    image_prompt = (
        image_agent.generate_prompt(
            formatted
        )
    )

    return {

        "post": formatted,

        "review": review,

        "image_prompt": image_prompt
    }