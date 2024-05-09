vetor = []
maior = 0
menor = 0
igual = 0

while len(vetor) < 5:
    try:
        numero = vetor.append(int(input(f"Digite um número: ")))
    except ValueError:
        print("Somente números são aceitos")

primeiro = vetor[0]

for i in range(1, len(vetor)):
    if vetor[i] < primeiro:
        menor += 1
    if vetor[i] > primeiro:
        maior += 1
    if vetor[i] == primeiro:
        igual += 1

print(f'''Resultado da lista:
      {menor} números menores que o primeiro número
      {maior} números maiores que o primeiro número
       {igual} númeors iguais ao primeiro número ''')
    