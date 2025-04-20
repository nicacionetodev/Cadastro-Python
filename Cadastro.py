import random
import os
print(os.path.abspath("usuario.txt"))

def menu():
    while True:
        print("\nSeja bem-vindo ao sistema de usuários")
        print("1 - Cadastrar usuário")
        print("2 - Fazer Login")
        print("3 - Mudar de Senha")
        print("4 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar()
        elif escolha == "2":
            login()
        elif escolha == "3":
            mudarsenha()
        elif escolha == "4":
            print("Saindo... até mais!")
            break
        else:
            print("Opção inválida, tente novamente!")

def cadastrar():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    email = input("Digite seu e-mail: ")

    try:
        with open("usuario.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome_arquivo, _, _ = linha.strip().split(":")
                if usuario == nome_arquivo:
                    print("Esse usuário já existe! Tente outro nome.")
                    return
    except FileNotFoundError:
        pass  # Arquivo ainda não existe, então tudo bem

    with open("usuario.txt", "a") as arquivo:
        arquivo.write(f"{usuario}:{senha}:{email}\n")
        print("Usuário cadastrado com sucesso!")

def login():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    try:
        with open("usuario.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                nome_arquivo, senha_arquivo, _ = linha.strip().split(":")
                if usuario == nome_arquivo and senha == senha_arquivo:
                    print(f"Login bem-sucedido! Bem-vindo, {usuario}!")
                    return
            print("Usuário ou senha incorretos!")
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda. Cadastre-se primeiro.")

def mudarsenha():
    usuario = input("Digite seu nome de usuário: ")
    try:
        with open("usuario.txt", "r") as arquivo:
            linhas = arquivo.readlines()

        usuario_encontrado = False
        novas_linhas = []

        for linha in linhas:
            nome, senha_antiga, email = linha.strip().split(":")
            if nome == usuario:
                usuario_encontrado = True
                codigo = str(random.randint(0, 9999)).zfill(4)
                print(f"(Simulado) Código enviado para o e-mail {email}: {codigo}")

                tentativa = input("Digite o código que foi enviado: ")
                if tentativa == codigo:
                    nova_senha = input("Digite sua nova senha: ")
                    novas_linhas.append(f"{nome}:{nova_senha}:{email}\n")
                    print("Senha alterada com sucesso!")
                else:
                    print("Código incorreto. Operação cancelada.")
                    return
            else:
                novas_linhas.append(linha)

        if not usuario_encontrado:
            print("Usuário não encontrado.")
            return

        with open("usuario.txt", "w") as arquivo:
            arquivo.writelines(novas_linhas)

    except FileNotFoundError:
        print("Arquivo de usuários não encontrado.")

# Inicia o menu
menu()