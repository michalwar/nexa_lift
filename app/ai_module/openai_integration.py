import sys
sys.path.append(r"D:\Projects\Git\nexa_lift")

import os
import openai
import json

from app.ai_module.prompts_eng import olympic_main_prompt

from dotenv import load_dotenv




load_dotenv(dotenv_path="./app/ai_module/.env")

api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("OPENAI_ORG_ID")


class OpenAIIntegration:
    """Class to interact with OpenAI's API."""

    def __init__(
        self,
        api_key: str,
        organization: str,
        model: str = "gpt-3.5-turbo-16k"
        ):
        """
        Initialize OpenAI Integration.

        Parameters:
        ------
            model: Model name to be used with OpenAI, defaults to "gpt-3.5-turbo".
            api_key: OpenAI API key.
            organization: OpenAI organization ID.
        """
        self.api_key = api_key
        self.organization = organization
        self.model = model

        if not self.api_key or not self.organization:
            raise ValueError(
                "API Key and Organization ID must be set as environment variables."
            )

        # Set up the OpenAI configuration
        openai.api_key = self.api_key
        openai.organization = self.organization

    def get_response(self, prompt: str) -> str:
        """
        Retrieve a response from the AI based on the provided prompt.

        Parameters:
        ------
            prompt: Input prompt for the AI.

        Returns:
        ------
            response: AI's response as a string, or None if there's an error.
        """
        messages = [{"role": "user", "content": prompt}]

        try:
            response = openai.ChatCompletion.create(model=self.model, messages=messages)
            return response["choices"][0]["message"]["content"]
        except openai.error.OpenAIError as e:
            # Log the exception for debugging or monitoring purposes
            print(f"OpenAI Error: {e}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        return None

    def _load_prompt_template_as_str(self, file_name: str) -> str:
        path_file = paths.DIR_PROMPT_TEMPLATES / file_name
        with open(path_file, "r", encoding=misc.ENCODING) as file:
            contents = file.read()
        return contents


# Example usage:
if __name__ == "__main__":
    openai_integrator = OpenAIIntegration(
        api_key=api_key, organization=organization
    )
    input_text = (
        "How well do you know workout plans, especially for Olympic weightlifting?"
    )
    input_text = olympic_main_prompt
    response = openai_integrator.get_response(input_text)
    if response:
        print("AI Response:", response)

    else:
        print("Failed to get a response.")


