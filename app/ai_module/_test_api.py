import sys
import os
from dotenv import load_dotenv

load_dotenv()

sys.path.append(r"D:\Projects\Git\nexa_lift")
api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("OPENAI_ORG_ID")


from app.ai_module.openai_integration import OpenAIIntegration

openai_integrator = OpenAIIntegration(api_key, organization, model="gpt-3.5-turbo-1106") #model="gpt-4-1106-preview")

openai_integrator.get_response("I want to do a workout that will help me get stronger.")



import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
    organization=organization,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

chat_completion.choices[0].message.content