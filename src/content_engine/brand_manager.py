import yaml
from pathlib import Path


def load_brand(
    brand_name
):

    file = (
        Path(
            "data/brands"
        )
        /
        f"{brand_name}.yaml"
    )

    with open(
        file,
        "r",
        encoding="utf-8"
    ) as f:

        return yaml.safe_load(
            f
        )