import json
from pathlib import Path

from content_engine.calendar_reader import (
    load_calendar
)

from content_engine.brand_manager import (
    load_brand
)

from content_engine.orchestrator import (
    ContentOrchestrator
)


def main():

    calendar = load_calendar(
        "data/content_calendar.csv"
    )

    orchestrator = (
        ContentOrchestrator()
    )

    output_dir = Path(
        "generated_posts"
    )

    output_dir.mkdir(
        exist_ok=True
    )

    for _, row in calendar.iterrows():

        brand_name = row.get(
            "brand",
            "protocol_x"
        )

        brand = load_brand(
            brand_name
        )

        result = orchestrator.run(
            row,
            brand
        )

        base = (
            f"{row['date']}"
            f"_{row['platform']}"
        )

        files = {

            f"{base}.txt":
                result["post"],

            f"{base}_image_prompt.txt":
                result["image_prompt"],

            f"{base}_video.txt":
                result["video_script"],

            f"{base}_newsletter.txt":
                result["newsletter"]
        }

        for name, content in files.items():

            with open(
                output_dir / name,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(
                    str(content)
                )

        json_files = {

            f"{base}_review.json":
                result["review"],

            f"{base}_campaign.json":
                result["campaign"],

            f"{base}_carousel.json":
                result["carousel"]
        }

        for name, content in json_files.items():

            with open(
                output_dir / name,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    content,
                    f,
                    indent=4
                )

        print(
            f"Created: {base}"
        )


if __name__ == "__main__":
    main()