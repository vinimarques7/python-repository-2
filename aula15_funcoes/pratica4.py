def media(n1, n2):
    n_soma = n1 + n2
    return n_soma/2

def status(media):
    if media > 6:
        print("Aprovado")
    elif media >= 4 and media <= 6:
        print("Verificação Suplementar")
    elif media < 4:
        print("Reprovado!")
    



n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota:  "))

print(media(n1,n2))
status(media(n1,n2))