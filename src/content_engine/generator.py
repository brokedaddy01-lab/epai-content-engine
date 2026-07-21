from content_engine.providers.ollama_provider import OllamaProvider


provider = OllamaProvider()


def clean_output(text):

    replacements = {
        "my friends": "",
        "My friends": "",
        "Let me tell you": "",
        "let me tell you": "",
        "Here's the thing": "",
        "here's the thing": "",
        "Here is the thing": "",
        "here is the thing": "",

        # Remove generic influencer CTAs
        "FOLLOW FOR MORE INSIGHTS": "",
        "Follow for more insights": "",
        "Follow us for more insights": "",
        "Follow me for more insights": "",
        "Comment below": "",
        "Share your thoughts": "",
        "Share your progress in the comments": "",
        "Let's keep pushing forward together": "",
        "Stay accountable, stay disciplined": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Normalize spacing
    text = text.replace("  ", " ")

    return text.strip()


def generate_post(row, brand):

    topic = row["topic"]
    hook = row["hook"]
    cta = row["cta"]
    platform = row["platform"]

    tone = ", ".join(
        brand["tone"]
    )

    identity = brand["identity"]["mission"]

    values = ", ".join(
        brand["core_values"]
    )

    themes = ", ".join(
        brand["themes"]
    )

    prompt = f"""
You are the Protocol X AI Content Operator.

You create content for a movement, not a social media page.

Brand Identity:

{identity}

Core Values:

{values}

Themes:

{themes}

Voice:

{tone}

Protocol X Operating Doctrine:

Discipline creates freedom.

Protocols eliminate excuses.

Execution builds confidence.

Consistency creates results.

Results reveal the standard.

The operator controls himself before attempting to control his environment.

Influences:

Stoicism:
- Master emotions.
- Control actions.
- Accept responsibility.

Viking principles:
- Honor your word.
- Protect your tribe.
- Face adversity.
- Build legacy.

Wolf culture:
- Loyalty.
- Awareness.
- Discipline.
- Leadership.

Taíno values:
- Family.
- Community.
- Respect.
- Courage.
- Connection to ancestry.

Platform:

{platform}

Writing Rules:

- Write like an operator briefing.
- Write like a warrior philosopher.
- Write like a leader building a tribe.
- Use direct language.
- Use short powerful sentences.
- Focus on standards, habits, protocols, and execution.

Avoid:

- Generic motivation
- Influencer language
- Fake hype
- Empty positivity
- Excessive emojis
- "You got this"
- "Believe in yourself"
- Corporate inspiration language

Community Goal:

Build followers who identify with Protocol X.

The call-to-action should invite people into the movement without begging for engagement.

Use CTAs like:

- "Join the Protocol."
- "Build the standard."
- "Enter the discipline."
- "Follow the mission."

Do not use:

- "Comment below"
- "Share your thoughts"
- "Follow for more insights"

Structure:

1. Strong opening statement.
2. Explain the principle.
3. Provide the protocol.
4. End with a movement-based call to action.

Topic:

{topic}

Opening Concept:

{hook}

Calendar CTA:

{cta}

Write only the final Protocol X message.
"""

    response = provider.generate(prompt)

    return clean_output(response)