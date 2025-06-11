def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2
numero1 = int(input("Digite um numero inteiro"))
numero2 = int(input("Digite outro numero inteiro"))

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 / numero2


resultadoSoma= soma(numero1, numero2)
resultadoSubtracao = subtracao(numero1, numero2) #chamada da funcao
resultadoMultiplicaco = multiplicacao(numero1, numero2)
resultadodivisao = divisao(numero1, numero2)



print("O resultado da função soma", resultadoSoma)
print("O resultado da função subtracao",resultadoSubtracao)
print("O resultado da função multiplicação",resultadoMultiplicaco)
print("O resultado da função divisao",resultadodivisao)