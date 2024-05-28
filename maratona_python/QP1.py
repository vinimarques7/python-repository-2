# Para fazer isso eu preciso que o usuário me dê números ímpares para desenhar 
# o caule



def copa(base):
    for i in range(1, base + 1, 2):
        espacos = ' ' * ((base - 1) // 2)
        astericos = '*' * i
        print(espacos + astericos)

base_tam = int(input("Informe o tamanho da base da copa: "))
copa(base_tam)