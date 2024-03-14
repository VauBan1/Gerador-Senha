import tkinter as tk
from tkinter import ttk
import random
import string

class GeradorSenha:
    def __init__(self, master):
        # Inicialização da aplicação
        self.master = master
        master.title("Gerador de Senhas")  # Define o título da janela
        master.geometry("600x550")  # Define o tamanho da janela
        master.configure(background="#f0f0f0")  # Define a cor de fundo da janela

        # Rótulo e caixa de entrada para o comprimento da senha
        self.label_length = ttk.Label(master, text="Comprimento da senha (até 35):", font=("Arial", 30), background="#f0f0f0")
        self.label_length.pack(pady=(10, 0))  # Espaçamento do rótulo
        self.length_var = tk.StringVar(value="12")  # Variável para armazenar o comprimento da senha
        self.length_entry = ttk.Entry(master, textvariable=self.length_var, font=("Arial", 30), width=10)
        self.length_entry.pack()  # Exibição da caixa de entrada

        # Rótulo para exibir a senha gerada
        self.label_generated = ttk.Label(master, text="Senha Gerada:", font=("Arial", 30), background="#f0f0f0")
        self.label_generated.pack(pady=5)  # Espaçamento do rótulo

        # Variável para armazenar e exibir a senha gerada
        self.password_var = tk.StringVar()
        self.password_label = ttk.Label(master, textvariable=self.password_var, font=("Arial", 30, "bold"), wraplength=250, background="#ffffff")
        self.password_label.pack()  # Exibição da senha gerada

        # Botão para gerar senha
        self.generate_button = ttk.Button(master, text="Gerar Senha", command=self.generate_password, style="Generate.TButton")
        self.generate_button.pack(pady=20)  # Espaçamento do botão

        # Botão para copiar senha para a área de transferência
        self.copy_button = ttk.Button(master, text="Copiar", command=self.copy_password, style="Copy.TButton")
        self.copy_button.pack()  # Exibição do botão

    def generate_password(self):
        # Função para gerar uma senha aleatória
        length = int(self.length_var.get())  # Obtém o comprimento da senha da entrada de texto
        length = min(length, 35)  # Limita o comprimento máximo da senha a 500 caracteres
        if length <= 0:  # Verifica se o comprimento é válido
            return
        characters = string.ascii_letters + string.digits + string.punctuation  # Define os caracteres possíveis para a senha
        password = ''.join(random.choice(characters) for i in range(length))  # Gera a senha aleatória
        self.password_var.set(password)  # Exibe a senha gerada na interface

    def copy_password(self):
        # Função para copiar a senha gerada para a área de transferência
        self.master.clipboard_clear()  # Limpa a área de transferência
        self.master.clipboard_append(self.password_var.get())  # Copia a senha gerada
        self.master.update()  # Atualiza a interface

root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")

# Configuração dos estilos para os botões
style.configure("Generate.TButton", background="#007bff", foreground="#ffffff", font=("Arial", 10, "bold"))
style.map("Generate.TButton", background=[("active", "#0056b3")])
style.configure("Copy.TButton", background="#28a745", foreground="#ffffff", font=("Arial", 10, "bold"))
style.map("Copy.TButton", background=[("active", "#218838")])

# Cria a aplicação e inicia o loop principal da interface gráfica
app = GeradorSenha(root)
root.mainloop()