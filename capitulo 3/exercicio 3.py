
def diametro(raio):
    return 2 * raio

def circunferencia(raio, pi):
    return 2 * pi * raio

def area(raio, pi):
    return pi * raio**2


raio = float(input("digite o raio do circulo"))
pi = 3.14159

resultadoDiametro = diametro(raio)
resultadoCircunferencia = circunferencia(raio, pi)
resultadoarea = area(raio, pi)

print("O resultado da função Diametro", resultadoDiametro)
print("O resultado da função Circunferencia",resultadoCircunferencia)
print("O resultado da função area",resultadoarea)