def idade(atual, data_nascimento):
    return atual - data_nascimento

def maioridade(nome, idade):
    if idade >= 18:
        print(f"{nome} é maior de idade.")
    elif idade < 18:
        print(f"{nome} é menor de idade.")

nome = input("Diga o seu nome: ")
atual = 2024
data_nascimento = int(input("Insira sua data de nascimento: "))
maioridade(nome, idade(atual, data_nascimento))



