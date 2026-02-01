import PyPDF2
import os

merger = PyPDF2.PdfMerger() # Cria um mesclador de PDFs

lista_arquivos = os.listdir("arquivos") # Lista todos os arquivos na pasta "arquivos"
lista_arquivos.sort() # Ordena os arquivos em ordem alfabética
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo: # Verifica se o arquivo é um PDF
        merger.append(f"arquivos/{arquivo}") # Usando o append para adicionar o PDF ao mesclador

merger.write("documento_final.pdf") # Escreve o PDF mesclado em um novo arquivo, salvando o pdf final