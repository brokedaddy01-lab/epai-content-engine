import json

from pathlib import Path

from content_engine.calendar_reader import (
    load_calendar
)

from content_engine.brand_manager import (
    load_brand_voice
)

from content_engine.generator import (
    generate_post
)


def main():

    calendar = load_calendar(
        "data/content_calendar.csv"
    )

    brand = load_brand_voice(
        "data/brand_voice.yaml"
    )

    output_dir = Path(
        "generated_posts"
    )

    output_dir.mkdir(
        exist_ok=True
    )

    for _, row in calendar.iterrows():

        result = generate_post(
            row,
            brand
        )

        base = (
            f"{row['date']}"
            f"_{row['platform']}"
        )

        post_file = (
            output_dir
            / f"{base}.txt"
        )

        review_file = (
            output_dir
            / f"{base}_review.json"
        )

        image_file = (
            output_dir
            /
            f"{base}_image_prompt.txt"
        )

        with open(
            post_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                result["post"]
            )

        with open(
            review_file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(

                result["review"],

                f,

                indent=4
            )

        with open(
            image_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(
                result["image_prompt"]
            )

        print(
            f"Created: {post_file}"
        )


if __name__ == "__main__":

    main()