import pandas as pd


def load_calendar(path):
    return pd.read_csv(path)


if __name__ == "__main__":
    calendar = load_calendar(
        "data/content_calendar.csv"
    )

    print(calendar)