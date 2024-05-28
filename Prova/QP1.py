usuarios = {}

nomes = []
curtidas = []


for i in range(2):
    # uma lista para curtidas de cada usuário
    curtidas_do_usuario = []
    try:

        # variável nome como string em vazia pra manipulação
        nome = ''
        # Este serve para tornar a primeira letra do nome em uma letra maiúscula
        while len(nome) < 1:
            nome = input("Informe o nome do usuário: ").capitalize()
        # Desta vez verifica se o nome possui ao menos um caractere
            if len(nome) < 1:
                print("Informe um nome com pelo menos um caractere")
        nomes.append(nome)
        
    # Exceção de valores para vericação de nome
    except ValueError:
        print("digite dados válidos no nome")
    except Exception:
        print(f"Exceção não considerada: {Exception}")

    #  else para a continuação caso não haja erros
    else:
        # range de 3 curtidas em um inteiro i
        for i in range(0, 3):
            try:
                # solicitação do número de curtidas por foto
                curtidas_do_usuario.append(int(input(f"Informe a quantdade de curtidas da {i + 1}ª foto: ")))

            except ValueError:
                print("Digite apenas números inteiros")
            except Exception:
                print(f"Exceção não considerada: {Exception}")
            
    # inserção das listas de curtidas de cada usuário na lista de curtidas de todos
    curtidas.append(curtidas_do_usuario)


            # leitura do comprimento dentro da lista de nomes 
for i in range(len(nomes)):
    # atribuindo cada nome como key e também a lista de curtidas como valor para cada chave 
    usuarios[nomes[i]] = curtidas[i]

# para cada nome em usuarios um incremento foi criado
for key in usuarios:
    num = 0
    # esse incremento verificar as curtidas dentro da lista de curtidas e usá-los
    #  usuario é uma lista de listas e like é cada valor  desta lista 
    for like in usuarios[key]:
        num += like
    print(f"Média: {num/3:.0f}")

print(usuarios)