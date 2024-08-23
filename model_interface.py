import requests



def get_model_prediction(prompt):
    url = "http://localhost:1234/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "your_model_name",
        "messages": [
            {"role": "system", "content": "You are an assistant analyzing browser history to predict user behavior."},
            {"role": "user", "content": prompt}
        ],
        #'max_tokens':50,
        'temperature':0.6,
        #"stop": [".\n"],
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()