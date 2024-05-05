n = int(input())
for i in range(n):
    numero1, numero2 = input().split()
    if(len(numero1) <= 1000 and len(numero2) <= 1000):
        if(numero1.endswith(numero2)):
            print("encaixa")
        else:
            print("nao encaixa")
