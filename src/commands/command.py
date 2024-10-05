import sys
from dotenv import load_dotenv
import time
import src.integration.gemini as gemini
import src.software.excalidraw as excalidraw

def to_write(text, delay=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def tech():
    question = input("Digite algo (tech): ")
    question = f"Você é um assistente técnico que responde no terminal Linux. Responda de forma direta e objetiva em até 3 linhas sem exemplos detalhados. Pergunta: {question}"
    response = gemini.question(question)
    to_write(response)
    return response

def personal():
    question = input("Digite algo (personal): ")
    question = f"Você é um personal trainer virtual que responde sobre atividades físicas, nutrição e bem-estar. Responda de forma direta e objetiva em até 10 linhas, focando em resultados práticos. Pergunta: {question}"
    response = gemini.question(question)
    to_write(response)
    return response

def start():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        #abstrair para uma função
        if command == "personal":
            personal()
        if command == "generic":
            question = input("Digite algo (generic): ")
            question = question
            response = gemini.question(question)
            return to_write(response)
        if command == "save":
            return to_write(excalidraw.save())

        else:
            to_write("precisa de ajuda?")
    else:
        tech()