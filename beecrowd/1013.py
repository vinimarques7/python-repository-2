numeros = input().split()

a = int(numeros[0])
b = int(numeros[1])
c = int(numeros[2])


maiorAB = (a + b + abs(a - b))/2


maiorABC = (maiorAB+c+abs(maiorAB-c))/2

print(f"{maiorABC:.0f} eh o maior")