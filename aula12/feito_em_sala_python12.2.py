vogais = []

frase = input("Digite uma frase: ").lower()

for i in frase:
    if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
        vogais.append(i)
print('\nExistem ', frase.count(' '), ' espaços na frase.')
print('A: ', vogais.count('a'), '\nE: ', vogais.count('e'), '\nI: ', 
      vogais.count('i'), '\nO: ', vogais.count('o'), '\nU: ', vogais.count('u'))
