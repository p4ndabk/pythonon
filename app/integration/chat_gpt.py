import requests
import json
import os

api_key = os.getenv("GEMINI_API_KEY")

url = 'https://api.openai.com/v1/chat/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "Você é um assistente."},
        {"role": "user", "content": "Qual é a capital da França?"}
    ],
    "max_tokens": 100
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    resposta_json = response.json()
    resposta = resposta_json['choices'][0]['message']['content']
    print("Resposta:", resposta)
else:
    # Exibir erro
    print(f"Erro: {response.status_code} - {response.text}")
