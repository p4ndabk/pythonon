import google.generativeai as genai
import os

def question(question):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(question)

    return response.text

def questionStrem():
    genai.configure(api_key="sua-api-key")

    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content("Qual o sentido da vida?", stream=True)

    for chunk in response:
        print(chunk.text)
        print("_"*80)