class VideoScriptAgent:

    def generate(
        self,
        post
    ):

        script = f"""
HOOK:

Most people fail because they rely on motivation.

Motivation fades.

Protocols create execution.

━━━━━━━━━━━━━━━━━━

BODY:

{post}

━━━━━━━━━━━━━━━━━━

CTA:

Follow Protocol X.

Discipline.
Protocols.
Execution.
Consistency.
Results.

Nobody is coming to save you.
"""

        return script.strip()