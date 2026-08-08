from content_engine.content_cleaner import (
    ContentCleaner
)


def test_clean_output_removes_ai_intro():

    cleaner = ContentCleaner()

    text = (
        "Here is the final post:\n\n"
        "Discipline creates freedom."
    )

    cleaned = cleaner.clean_output(
        text
    )

    assert "Here is the final post:" not in cleaned

    assert "Discipline creates freedom." in cleaned


def test_clean_output_removes_banned_phrases():

    cleaner = ContentCleaner()

    text = (
        "Newsflash: discipline matters.\n"
        "Here's the thing: systems win.\n"
        "As we all know, consistency matters."
    )

    cleaned = cleaner.clean_output(
        text
    )

    assert "Newsflash:" not in cleaned

    assert "Here's the thing:" not in cleaned

    assert "As we all know," not in cleaned


def test_clean_output_collapses_excessive_blank_lines():

    cleaner = ContentCleaner()

    text = (
        "First line.\n\n\n\n"
        "Second line."
    )

    cleaned = cleaner.clean_output(
        text
    )

    assert cleaned == (
        "First line.\n\n"
        "Second line."
    )


def test_clean_cta_keeps_only_first_protocol_x_cta():

    cleaner = ContentCleaner()

    text = (
        "Discipline creates freedom.\n\n"
        "Follow Protocol X for disciplined execution.\n\n"
        "Another point.\n\n"
        "Follow Protocol X for disciplined execution."
    )

    cleaned = cleaner.clean_cta(
        text
    )

    assert cleaned.count("Follow Protocol X") == 1

    assert "Discipline creates freedom." in cleaned

    assert "Another point." in cleaned