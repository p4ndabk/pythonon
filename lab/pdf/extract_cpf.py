from PyPDF2 import PdfReader # type: ignore
import time
import re
import csv
import sys

def extrair_cpfs(text):
    cpf_pattern = r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b'
    cpfs = re.findall(cpf_pattern, text)
    
    return cpfs

def save_csv(cpf_list, file_name):
    try :
        path = 'output_csv/' + file_name

        with open(path, mode='w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
        
            for cpf in cpf_list:
                escritor_csv.writerow([cpf])
        print (f'Arquivo {file_name} salvo com sucesso')
    except Exception as e:
        print(f'Erro ao salvar o arquivo {file_name}')
        print(e)

def remove_format_cpf(data):
    for cpf in range(len(data)):
        data[cpf] = data[cpf].replace('.', '').replace('-', '')
    return data

def start(export_csv=False):
    cpfs_merged = []
    path = "cadastro_de_empregadores.pdf"
    with open(path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]

            text = page.extract_text()
            cpfs = extrair_cpfs(text)

            cpfs_merged += remove_format_cpf(cpfs)
    if export_csv:
        save_csv(cpfs_merged, 'cpfs.csv')
        print("save csv")

    print(cpfs_merged)

    return cpfs_merged