import sys
from dotenv import load_dotenv
import os
import time
import subprocess
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

def fender():
    try:
        directory = os.getenv('FENDER_DIRECTORY') + '/.docker'
        os.chdir(directory)
                
        subprocess.run(['docker-compose', '-f', 'docker-compose-arm.yaml', 'up', '-d'], check=True, text=True)
        to_write("Docker executado com sucesso!")
    except FileNotFoundError as fnf_error:
        to_write(f"Diretório não encontrado: {fnf_error}")
    except subprocess.CalledProcessError as e:
        to_write(f"Ocorreu um erro ao executar o comando: {e}")

def ibanez():
    try:
        directory = os.getenv('IBANEZ_DIRECTORY') + '/.docker'
        os.chdir(directory)
                
        subprocess.run(['docker-compose', '-f', 'docker-compose-arm.yaml', 'up', '-d'], check=True, text=True)
        to_write("Docker executado com sucesso!")
    except FileNotFoundError as fnf_error:
        to_write(f"Diretório não encontrado: {fnf_error}")
    except subprocess.CalledProcessError as e:
        to_write(f"Ocorreu um erro ao executar o comando: {e}")

def ibanez_open():
    directory = os.getenv('IBANEZ_DIRECTORY')
    os.chdir(directory)
            
    subprocess.run(['code', '.'], check=True, text=True)

def fender_open():
    directory = os.getenv('FENDER_DIRECTORY')
    os.chdir(directory)
            
    subprocess.run(['code', '.'], check=True, text=True)

def pandabk_open():
    directory = os.getenv('PANDABK_DIRECTORY')
    os.chdir(directory)
            
    subprocess.run(['code', '.'], check=True, text=True)

def save():
    to_write(excalidraw.save())

def start():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "personal":
            personal()
        if command == "generic":
            question = input("Digite algo (generic): ")
            question = question
            response = gemini.question(question)
            return to_write(response)
        if command == "open":
            pandabk_open()
            return
        if command == "fender:up":
            fender()
            return
        if command == "fender:open":
            fender_open()
            return
        if command == "ibanez:up":
            ibanez()
            return
        if command == "ibanez:open":
            ibanez_open()
            return
        if command == "save":
            save()
            return
        else:
            to_write("precisa de ajuda?")
    else:
        tech()