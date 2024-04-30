def reverso_num(numero):
    numero = str(numero)
    invertido = numero[::-1]
    return invertido

numero = int(input("Digite o número que será invertido: "))
print(reverso_num(numero))
