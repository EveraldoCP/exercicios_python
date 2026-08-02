for produtos in range (1,16):
    nota = int(input("Avalie com uma note de 0 a 5 para o produto:\n"))
    while nota <0 or nota >5:
        print("Nota inválida")
        nota = int(input("Avalie com uma note de 0 a 5 para o produto:\n"))
        


