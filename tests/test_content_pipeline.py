from content_engine.orchestrator import ContentOrchestrator


def get_brand():

    return {

        "brand_name":
            "Protocol X",

        "identity":
        {

            "mission":
                "Build disciplined operators through systems, protocols, and execution."

        },

        "core_values":
        [

            "Discipline",

            "Integrity",

            "Consistency",

            "Execution"

        ],

        "themes":
        [

            "Stoicism",

            "Leadership",

            "Self Mastery",

            "Performance"

        ]

    }


def get_row(topic, platform):

    return {

        "topic":
            topic,

        "platform":
            platform,

        "keyword":
            "discipline",

        "hook":
            "The strongest operators build systems before they chase results.",

        "cta":
            "Follow Protocol X for disciplined execution."

    }


def test_content_pipeline_returns_complete_package():

    orchestrator = ContentOrchestrator()


    result = orchestrator.run(

        get_row(
            "discipline",
            "facebook"
        ),

        get_brand()

    )


    assert "post" in result

    assert "review" in result

    assert "campaign" in result

    assert "assets" in result


def test_campaign_metadata_created():

    orchestrator = ContentOrchestrator()


    result = orchestrator.run(

        get_row(
            "leadership",
            "linkedin"
        ),

        get_brand()

    )


    campaign = result["campaign"]


    assert campaign["brand"] == "Protocol X"

    assert campaign["platform"] == "linkedin"

    assert campaign["topic"] == "leadership"

    assert "created" in campaign


def test_assets_package_exists():

    orchestrator = ContentOrchestrator()


    result = orchestrator.run(

        get_row(
            "execution",
            "instagram"
        ),

        get_brand()

    )


    assets = result["assets"]


    assert assets is not None

    assert "formatted" in assets


def test_clean_output_removes_ai_phrases():

    orchestrator = ContentOrchestrator()


    text = (

        "Here is the final post:\n\n"

        "Discipline creates freedom."

    )


    cleaned = orchestrator.clean_output(

        text

    )


    assert "Here is the final post:" not in cleaned

    assert "Discipline creates freedom." in cleaned


def test_clean_output_removes_banned_phrases():

    orchestrator = ContentOrchestrator()


    text = (

        "Newsflash: Discipline creates freedom.\n\n"

        "Here's the hard truth: systems create consistency."

    )


    cleaned = orchestrator.clean_output(

        text

    )


    assert "Newsflash:" not in cleaned

    assert "Here's the hard truth:" not in cleaned

    assert "Discipline creates freedom." in cleaned

    assert "systems create consistency." in cleaned


def test_clean_output_collapses_excessive_blank_lines():

    orchestrator = ContentOrchestrator()


    text = (

        "Discipline creates freedom.\n\n\n\n"

        "Systems create consistency."

    )


    cleaned = orchestrator.clean_output(

        text

    )


    assert cleaned == (

        "Discipline creates freedom.\n\n"

        "Systems create consistency."

    )


def test_clean_cta_keeps_only_first_protocol_x_cta():

    orchestrator = ContentOrchestrator()


    text = (

        "Discipline creates freedom.\n\n"

        "Follow Protocol X for disciplined execution.\n\n"

        "More content.\n\n"

        "Follow Protocol X for disciplined execution."

    )


    cleaned = orchestrator.clean_cta(

        text

    )


    assert cleaned.count("Follow Protocol X") == 1

    assert "Discipline creates freedom." in cleaned

    assert "More content." in cleaned