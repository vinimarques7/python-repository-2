file = open("arq2.txt", "r")

for line in file:
    lista = line.strip().split()
    nome = lista[0]
    notas = lista[1:]

    if len(notas) > 6:
        print(nome)

file.close()