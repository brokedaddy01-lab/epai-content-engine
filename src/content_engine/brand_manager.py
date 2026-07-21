import yaml


def load_brand_voice(path):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


if __name__ == "__main__":
    brand = load_brand_voice(
        "data/brand_voice.yaml"
    )

    print(brand)