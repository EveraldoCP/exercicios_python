print("--MULTIPLICAÇÃO ATÉ 10--")

tabuada = int(input("Digite um número para calcular sua multiplicação até 10: "))

print(f"Tabuada do {tabuada}:\n")

for i in range(1 , 11):
    resultado = tabuada * i
    
    print(f"{tabuada} x {i} = {resultado}\n")    