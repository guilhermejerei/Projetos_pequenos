from tkinter import *
import main
import os

cor_fundo = "#0F2027"
cor_degrade = "#203A43"
cor_borda_caixa = "#2C5364"
cor_botao = "#00FFAE"
cor_texto = "#FFFFFF"
cor_destaque = "#00FFC6"
fonte_padrao = ("Poppins", 10)

def criar_conta():
    usuario = nome_usuario.get()
    senha = senha_usuario.get()
    resultado = main.analisar_conta(usuario, senha)
    if resultado["status"] == "sucesso":
        mensagem.config(text="Conta criada com sucesso!", fg="#00ffae")
        nome_usuario.delete(0, END)
        senha_usuario.delete(0, END)
        main.adicionar_conta(usuario, senha)
    else:
        mensagem.config(text=resultado["mensagem"], fg="#ff4c4c")

def fazer_login():
    usuario = nome_usuario.get()
    senha = senha_usuario.get()
    resultado = main.verificar_login(usuario, senha)
    if resultado["status"] == "sucesso":
        abrir_plataforma()
        nome_usuario.delete(0, END)
        senha_usuario.delete(0, END)
    else:
        mensagem.config(text=resultado["mensagem"], fg="#ff4c4c")

def abrir_plataforma():
    plataforma = Toplevel(index)
    plataforma.title("Plataforma")
    plataforma.geometry("800x600")
    plataforma.configure(bg="white")
    Label(plataforma, text="teste", font=("Poppins", 24), bg="white", fg="black").pack(pady=20)

def criar_degrade(canvas, width, height, cor1, cor2):
    canvas.delete("all")
    r1, g1, b1 = canvas.winfo_rgb(cor1)
    r2, g2, b2 = canvas.winfo_rgb(cor2)
    r_ratio = (r2 - r1) / height
    g_ratio = (g2 - g1) / height
    b_ratio = (b2 - b1) / height
    for i in range(height):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        cor = f"#{nr>>8:02x}{ng>>8:02x}{nb>>8:02x}"
        canvas.create_line(0, i, width, i, fill=cor)

def on_resize(event):
    largura = event.width
    altura = event.height
    criar_degrade(canvas_degrade, largura, altura, cor_fundo, cor_degrade)

def toggle_senha():
    if mostrar_senha.get():
        senha_usuario.config(show="")
    else:
        senha_usuario.config(show="*")

index = Tk()
index.title("Login")
index.geometry("700x500")
index.minsize(700, 500)
index.configure(bg=cor_fundo)
index.grid_propagate(False)

canvas_degrade = Canvas(index, highlightthickness=0)
canvas_degrade.pack(fill=BOTH, expand=True)
canvas_degrade.bind("<Configure>", on_resize)

form_frame = Frame(index, bg=cor_degrade, bd=2, relief=RIDGE, padx=20, pady=20)
form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

titulo = Label(form_frame, text="Login", font=("Poppins", 36, "bold"), bg=cor_degrade, fg=cor_texto)
titulo.grid(row=0, column=0, columnspan=2, pady=(0, 20))

Label(form_frame, text="Usuário", font=("Poppins", 12), bg=cor_degrade, fg=cor_texto).grid(row=1, column=0, padx=(0, 5))
nome_usuario = Entry(form_frame, width=30, font=fonte_padrao, fg=cor_texto, bg=cor_borda_caixa,
                     insertbackground=cor_texto, relief=FLAT, highlightthickness=1, highlightcolor=cor_destaque)
nome_usuario.grid(row=1, column=1, pady=5, ipady=6, ipadx=4)
nome_usuario.configure(highlightbackground=cor_borda_caixa, borderwidth=1)

Label(form_frame, text="Senha", font=("Poppins", 12), bg=cor_degrade, fg=cor_texto).grid(row=2, column=0, padx=(0, 5))
senha_usuario = Entry(form_frame, width=30, font=fonte_padrao, show="*", fg=cor_texto, bg=cor_borda_caixa,
                      insertbackground=cor_texto, relief=FLAT, highlightthickness=1, highlightcolor=cor_destaque)
senha_usuario.grid(row=2, column=1, pady=5, ipady=6, ipadx=4)
senha_usuario.configure(highlightbackground=cor_borda_caixa, borderwidth=1)

mostrar_senha = BooleanVar(value=False)
mostrar_senha_check = Checkbutton(form_frame, text="Mostrar senha", variable=mostrar_senha, command=toggle_senha,
                                 bg=cor_degrade, fg=cor_texto, font=("Poppins", 8), activebackground=cor_degrade,
                                 highlightthickness=0, relief=FLAT, indicatoron=False,
                                 selectcolor=cor_degrade, activeforeground=cor_texto)
mostrar_senha_check.grid(row=3, column=1, sticky="e", pady=(0, 5))

botao_login = Button(form_frame, text="Login", command=fazer_login, font=("Poppins", 10, "bold"),
                     bg=cor_botao, fg="black", activebackground="#00cc90", relief=FLAT, bd=0, padx=20, pady=8)
botao_login.grid(row=4, column=0, columnspan=2, pady=10)
botao_login.configure(borderwidth=0, highlightthickness=0)

mensagem = Label(form_frame, text="", bg=cor_degrade, fg="white", font=("Poppins", 9), wraplength=300, justify=LEFT)
mensagem.grid(row=5, column=0, columnspan=2, sticky="w")

rodape = Label(form_frame, text="Não possui conta? ", bg=cor_degrade, fg=cor_texto, font=("Poppins", 9))
rodape.grid(row=6, column=0, sticky="e", pady=(10, 0))

criar_conta_link = Label(form_frame, text="Criar conta", bg=cor_degrade, fg=cor_destaque,
                         font=("Poppins", 9, "underline"), cursor="hand2")
criar_conta_link.grid(row=6, column=1, sticky="w", pady=(10, 0))
criar_conta_link.bind("<Button-1>", lambda e: criar_conta())