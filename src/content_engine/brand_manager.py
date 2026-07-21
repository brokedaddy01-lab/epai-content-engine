import yaml

from content_engine.models.brand_context import (
    BrandContext
)


def load_brand_voice(path):

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        data = yaml.safe_load(f)

    return BrandContext(

        brand_name=data["brand_name"],

        mission=data["identity"]["mission"],

        philosophy=data["identity"]["philosophy"],

        tone=data["tone"],

        values=data["core_values"],

        themes=data["themes"],

        signature_phrases=data[
            "signature_phrases"
        ],

        rules=data["rules"],

        voice_mix=data["voice_mix"]
    )