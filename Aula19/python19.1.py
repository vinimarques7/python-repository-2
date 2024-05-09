import math

while True:
    try:
        numero = int(input("Digite um número: "))
        raiz = math.sqrt(numero)
        print(f"A raiz de {numero} é {raiz :.2f}")

    except ValueError:
        print("Formato do número não condiz com o esperado.")
        break


