
def validalogin(nome ,senha):
    if(nome == "isabella" and senha == "123456"):
     return print("seja bem vindo")
    else:
     return print("senha ou nome invalidos")

print("=== digite seu nome ===")
nome = input()
print("=== digite sua senha ===")
senha = input()

validalogin(nome , senha)