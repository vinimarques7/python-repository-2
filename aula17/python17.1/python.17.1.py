file = open("arq.txt", "r")
print(file.read())
medicoes = []
quantidade = 0

for line in file:
    medicoes.append(line)

file.close()

for i in range(1, len(medicoes)):
    if (medicoes[i] > medicoes[i -1]):
        quantidade += 1

print(quantidade)