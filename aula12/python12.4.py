frase = input("Digite uma frase: ").lower().replace(" ", "")

if frase == frase[::-1]:
    print('É palindromo')
else:
    print('Não é palindromo')
