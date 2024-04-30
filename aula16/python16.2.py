def armazenar_idades():
    nomes = []
    idades = []
    while True:
        entrada_nome = input("Digite um nome: ")
        if (entrada_nome == "Maria"):
            continue
        nomes.append(entrada_nome)
        entrada_idade = int(input("Digite sua idade: "))
        if(entrada_nome == -1):
            nomes.pop()
            print(f"Os nomes cadastrados são: {nomes}")
            print(f"Suas respectivas idades são: {idades}")
            break
        idades.append(entrada_idade)
armazenar_idades()


