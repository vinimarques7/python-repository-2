frase = input("Digite uma frase qualquer: ")


contagem_vogal_a = frase.count("a")
contagem_vogal_e = frase.count("e")
contagem_vogal_i = frase.count("i")
contagem_vogal_o = frase.count("o")
contagem_vogal_u = frase.count("u")

contagem_espaco = frase.count(" ")


print(f'Quantidade de A: {contagem_vogal_a}')
print(f'Quantidade de E: {contagem_vogal_e}')
print(f'Quantidade de I: {contagem_vogal_i}')
print(f'Quantidade de O: {contagem_vogal_o}')
print(f'Quantidade de U: {contagem_vogal_u}')
print(f"\nQuantidade de espaços: {contagem_espaco}")