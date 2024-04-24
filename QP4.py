saida = []
n = int(input())
for i in range(n):
    numero1, numero2 = input().split()
    if(len(numero1) <1000 and len(numero2)<1000):
        if(numero1.endswith(numero2)):
            saida.append("encaixa")
        else:
            saida.append("nao encaixa")
for i in range(len(saida)):
    print(saida[i])