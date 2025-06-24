import os
import json
import hashlib
import interface

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONTAS_PATH = os.path.join(BASE_DIR, "contas_gravadas", "contas.json")
os.makedirs(os.path.dirname(CONTAS_PATH), exist_ok=True)

# Carregar ou inicializar banco de contas
try:
    with open(CONTAS_PATH, "r") as f:
        banco_de_contas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    banco_de_contas = []

def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def criar_conta_obj(usuario, senha):
    return {"usuario": usuario, "senha": criptografar_senha(senha)}

def validar_usuario(usuario):
    if len(usuario) < 4:
        return "Nome de usuário curto (mín. 4)."
    if len(usuario) > 10:
        return "Nome de usuário longo (máx. 10)."
    return "válido!"

def validar_senha(senha):
    if len(senha) < 4:
        return "Senha curta (mín. 4)."
    if len(senha) > 16:
        return "Senha longa (máx. 16)."
    if not any(char.isdigit() for char in senha):
        return "A senha deve conter ao menos um número."
    if senha.isalnum():
        return "A senha deve conter ao menos um caractere especial."
    return "válido!"

def analisar_conta(usuario, senha):
    msg_usuario = validar_usuario(usuario)
    msg_senha = validar_senha(senha)

    if msg_usuario == msg_senha == "válido!":
        return {"status": "sucesso", "conta": criar_conta_obj(usuario, senha)}

    erros = []
    if msg_usuario != "válido!":
        erros.append(f"Usuário: {msg_usuario}")
    if msg_senha != "válido!":
        erros.append(f"Senha: {msg_senha}")

    return {"status": "erro", "mensagem": "\n".join(erros)}

def adicionar_conta(usuario, senha):
    banco_de_contas.append(criar_conta_obj(usuario, senha))
    salvar_contas()

def verificar_login(usuario, senha):
    senha_hash = criptografar_senha(senha)
    for conta in banco_de_contas:
        if conta["usuario"] == usuario and conta["senha"] == senha_hash:
            return {"status": "sucesso", "mensagem": "Login realizado com sucesso!"}
    return {"status": "erro", "mensagem": "Usuário ou senha incorretos."}

def salvar_contas():
    with open(CONTAS_PATH, "w") as f:
        json.dump(banco_de_contas, f, indent=4)

if __name__ == "__main__":
    interface.mainloop()