import sys
from dotenv import load_dotenv
import time
import gemini
import os

def to_write(text, delay=0.04):    
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def start():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "person":
            question = input("Digite algo: ")
            question = f"Preciso de uma resposta mais curta pois estou utilizando via api em um console linux quero em um contexto mais pessoal em no maximo 8 linhas. Pergunta: {question}"
            response = gemini.question(question)
            return to_write(response)

        else:
            to_write("precisa de ajuda?")
    else:
        question = input("Digite algo (tech): ")
        question = f"Você é um assistente técnico que responde no terminal Linux. Responda de forma direta e objetiva em até 3 linhas sem exemplos detalhados. Pergunta: {question}"
        response = gemini.question(question)
        to_write(response)

load_dotenv()
start()