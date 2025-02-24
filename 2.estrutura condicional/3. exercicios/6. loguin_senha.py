import os
os.system("clear")

login_cadastrado = "neymar"
senha_cadastrada = "goat"

login = input("Digite o login: ")
senha = input("digite a senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem-vindo")
else:
    print(" login ou senha invalidos!")