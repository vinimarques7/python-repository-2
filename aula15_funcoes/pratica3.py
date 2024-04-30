def adicao(a,b):
    plus = a+b
    return plus
def subtracao(a,b):
    minus = a-b
    return minus
def multiplicacao(a,b):
    times = a*b
    return times
def divisao(a,b):
    divided = a/b
    return divided

while True:

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    operacao = int(input("Agora selecione o operador entre +(1), -(2), *(3) ou /(4): "))

    if operacao == 1:
        print(adicao(a,b))
    elif operacao == 2:
        print(subtracao(a,b))
    elif operacao == 3:
        print(multiplicacao(a,b))
    elif operacao == 4:
        print(divisao(a,b))
    
    repete = input("Informe se deseja repetir o processo: ")

    if repete == 's':
        True
    else:
        break


    
