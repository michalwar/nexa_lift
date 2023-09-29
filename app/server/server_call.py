import sys

sys.path.append(r"D:\Projects\Git\nexa_lift")

from flask import Flask, request, jsonify, render_template

import os
from dotenv import load_dotenv

from app.ai_module.openai_integration import OpenAIIntegration
from app.ai_module.prompts_eng import olympic_main_prompt
from app.ai_module.prompts_parse import parse_workout_response

load_dotenv(dotenv_path="../ai_module/.env")

app = Flask(__name__)

# Initialize the AI module with the necessary credentials
api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("OPENAI_ORG_ID")
ai_integrator = OpenAIIntegration(api_key=api_key, organization=organization)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        response = ai_integrator.get_response(olympic_main_prompt)
        workout_plan = parse_workout_response(response)
        return render_template('index.html', workout_plan=workout_plan)
    return render_template('index.html', workout_plan=None)

import json
print(response)

text = response.replace("{...}", "null")
json.loads(text)



if __name__ == "__main__":
    app.run(debug=True)
