soma = 0
quantidade = 0

temperatura = float(input("Digite uma temperatura em °C: "))

while temperatura != -273:   
    quantidade += 1
    soma += temperatura
    media = soma / quantidade

    temperatura = float(input("Digite mais uma temperatura em °C (ou -273 para sair): "))

    print(f"A média final das temperaturas é: {media}")
    








