import os
from datetime import datetime

def proximo_nome_arquivo():
    i = 1
    while True:
        nome = f"dados_gravados_{i:03}.txt"
        if not os.path.exists(nome):
            return nome
        i += 1

arquivo_destino = proximo_nome_arquivo()

def obter_valor():
    return input("\nDigite qualquer coisa, para saber de qual tipo é: ")

def verificar_tipos(valor):
    partes = valor.split()
    tipos_verificados = []

    for parte in partes:
        if parte.isdigit():
            tipo = "int"
        elif parte.replace('.', '', 1).isdigit() and parte.count('.') == 1:
            tipo = "float"
        else:
            tipo = "string"
        
        tipos_verificados.append((parte, tipo))  # CORRETO

    return tipos_verificados

def salvar_entrada(numero, valor, tipos):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open(arquivo_destino, 'a') as myFile:
        myFile.write(f"Entrada {numero} - {data_hora}: {valor}\n")
        for parte, tipo in tipos:
            myFile.write(f"    -> {parte} ({tipo})\n")

def perguntar_continuar():
    resposta = input("\nVocê deseja continuar? (S/N) ")
    return resposta.lower() == "s"

def verificar():
    numero_de_entrada = 1

    while True:
        valor = obter_valor()
        tipos = verificar_tipos(valor)

        print("\nTipos identificados:")
        for parte, tipo in tipos:
            print(f"{parte} -> {tipo}")

        salvar_entrada(numero_de_entrada, valor, tipos)

        if not perguntar_continuar():
            print("\nBye Bye")
            break

        numero_de_entrada += 1

if __name__ == '__main__':
    verificar()