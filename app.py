from flask import Flask, jsonify, request
from db_connector import fetch_browsing_history
from model_interface import get_model_prediction

app = Flask(__name__)




def prepare_prompt(history):
    prompt = "The user has recently visited the following websites:\n"
    for entry in history:
        prompt += f"- {entry['page_title']} ({entry['page_url']}) on {entry['visit_date']} at {entry['visit_time']} for {entry['visit_count']} times, and transition type is {entry['transition_type']}.\n"
    prompt += "Based on this browsing history, what do you predict the user might do next?" #(give me your answer in 50 words)"
    return prompt





@app.route('/predict', methods=['GET'])
def predict_behavior():
    #print("Received request at /predict")
    history = fetch_browsing_history()
    if not history:
        return jsonify({"error": "No browsing history found"}), 404
    
    prompt = prepare_prompt(history)
    prediction_response = get_model_prediction(prompt)
    
    prediction = prediction_response['choices'][0]['message']['content']
    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    app.run(debug=True)