import ollama

from .base import BaseProvider


class OllamaProvider(BaseProvider):

    def __init__(self, model="qwen3:14b"):

        self.model = model

    def generate(self, prompt: str) -> str:

        system_prompt = ""

        user_prompt = prompt

        separator = "━━━━━━━━━━━━━━━━━━"

        if separator in prompt:

            parts = prompt.split(separator, 1)

            system_prompt = parts[0].strip()

            user_prompt = separator + parts[1]

        response = ollama.chat(

            model=self.model,

            messages=[

                {
                    "role": "system",
                    "content": system_prompt
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ]

        )

        return response["message"]["content"].strip()