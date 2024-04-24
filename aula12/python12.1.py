frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra contida na frase: ')
palavra_2 = input('Digite a palavra que substituirá a palavra informada anteriormente: ')


frase_nova = frase.replace(palavra, palavra_2)

print(frase_nova)