def vitamina():
    lista = {
        "suco de laranja": 120,
        "morango fresco": 85,
        "mamao": 85,
        "goiaba vermelha": 70,
        "manga": 56,
        "laranja": 50,
        "brocolis": 34
    }

    ideal = (110, 130)

    while True:
        numero = int(input())
        if numero == 0:
            break 

        vitamina_c = 0
        for _ in range(numero):
            input_str = input()
            quantidade, _, alimento = input_str.partition(' ')
            quantidade = int(quantidade)
            if alimento in lista:
                vitamina_c += quantidade * lista[alimento]
            else:
                print(f"Comida invalida: {alimento}")

        
        if vitamina_c > ideal[1]:
            print(f"Menos {vitamina_c - ideal[1]} mg")
        elif vitamina_c < ideal[0]:
            print(f"Mais {ideal[0] - vitamina_c} mg")
        else:
            print(f"{vitamina_c} mg")

vitamina()