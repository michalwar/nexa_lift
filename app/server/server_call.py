import sys
sys.path.append(r"D:\Projects\Git\nexa_lift")

from flask import Flask, request, jsonify, render_template

import os
from dotenv import load_dotenv
from app.ai_module.openai_integration import OpenAIIntegration

load_dotenv(dotenv_path="./app/ai_module/.env")

app = Flask(__name__)

# Initialize the AI module with the necessary credentials
api_key = os.getenv("OPENAI_API_KEY")
organization = os.getenv("OPENAI_ORG_ID")
ai_integrator = OpenAIIntegration(api_key=api_key, organization=organization)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        response = ai_integrator.get_response(query)
        return render_template('index.html', response=response)
    return render_template('index.html', response=None)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    query = data.get("query", "")

    # Fetch response from your AI model
    response = ai_integrator.get_response(query)
    
    return jsonify({
        "response": response
    })

if __name__ == '__main__':
    app.run(debug=True)