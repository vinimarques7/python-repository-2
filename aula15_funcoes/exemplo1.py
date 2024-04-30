def media (n1, n2):
    resultado_media = (n1 + n2)/2
    return resultado_media

nota1 = int(input("Informe a primeira nota:"))
nota2 = int(input("Informe a segunda nota: "))

media_aluno = media(nota1, nota2)

print(f"A média desse aluno é de {media_aluno}")
print(f"Média entre 16 e 45: {media(16, 45)}")