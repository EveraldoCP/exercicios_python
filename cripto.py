print("--Verificação de números primos--")

numero = int(input("Digite um número para a vereficação:\n"))

if numero <= 1:
    print(f"O {numero} digitado não é primo")

else:
    for i in range(2 , numero):
        if numero % i == 0:
            print(f"O {numero} não é primo")
            break

    else:
        print(f"O {numero} é primo")    


