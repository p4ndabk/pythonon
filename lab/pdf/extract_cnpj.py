from PyPDF2 import PdfReader
import time
import re
import csv
import sys


def extrair_cnpjs(text):
    cnpj_pattern = r'\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b|\b\d{14}\b'
    
    cnpjs = re.findall(cnpj_pattern, text)
    
    return cnpjs

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
def remove_format_cnpj(data):
    for cnpj in range(len(data)):
        data[cnpj] = data[cnpj].replace('.', '').replace('-', '').replace('/', '')
    return data

def start(export_csv=False):
    for param in sys.argv:
        if param == '--export_csv':
            export_csv = True

    cnpjs_merged = []
    path = "cadastro_de_empregadores.pdf"
    with open(path, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        for page_number in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_number]

            text = page.extract_text()
            cnpjs = extrair_cnpjs(text)

            cnpjs_merged += remove_format_cnpj(cnpjs)
    if export_csv:
        print("export csv file: cnpj.csv")
        save_csv(cnpjs_merged, 'cnpjs.csv')

    return cnpjs_merged