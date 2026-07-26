class StoryEngineAgent:


    def framework(self):

        return {

            "structure": [

                "HOOK",

                "PROBLEM",

                "PERSONAL LESSON",

                "PROTOCOL",

                "ACTION",

                "CTA"

            ]

        }



    def build_story(

        self,

        topic,

        audience,

        platform

    ):

        return {

            "topic": topic,

            "audience": audience,

            "platform": platform,

            "framework": self.framework(),

            "instruction":

                """
Create content using this story structure:

1. Hook:
Capture attention immediately.

2. Problem:
Identify the pain, struggle, or mistake.

3. Personal Lesson:
Explain the realization or transformation.

4. Protocol:
Provide the system, method, or framework.

5. Action:
Give the audience a clear next step.

6. CTA:
Create engagement and continuation.
"""

        }