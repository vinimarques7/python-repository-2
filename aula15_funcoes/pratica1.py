def contador_palavras(entrada):
    entrada = entrada.split()
    return len(entrada)

entrada = input("Digite uma frase: ")
print(contador_palavras(entrada))
