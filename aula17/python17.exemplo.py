file = open ("notas.txt", "r")

soma_notas = 0.0
quant = 0
for line in file:
    soma_notas += float(line)
    quant += 1

file.close()

media = soma_notas / quant
print(f"A média de notas foi {media}")