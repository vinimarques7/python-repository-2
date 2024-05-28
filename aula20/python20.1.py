def verificar_primo(numero):
    lista = []
    contador = 0

    while (contador <= numero):
            contador+=1
            if numero % contador == 0:
                lista.append(contador)
            
    if lista[0] == 1 and lista[1] == numero:
        print("Este número é primo.")

    else:
        print("Este número não é primo.")
        
try:
    numero = int(input("Digite um número: "))

except ValueError:
    print("Digite um número inteiro.")

else:
    verificar_primo(numero)
    

    


