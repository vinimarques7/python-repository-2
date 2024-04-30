def numeros_selecionados(lista, inferior, superior):
    numeros = []
    for numero in lista:
        if inferior <= numero <= superior:
            numero.append(numero)
        return numeros
    
    numeros2 = []
    for i in range(10):
        numeros2.append(int(input()))

    inferior = int(input("O inferior é: "))
    superior = int(input("O superior é: "))

numeros_selecionados()
