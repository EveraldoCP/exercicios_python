fator = int(input("Digite um número inteiro ('sem vírgulas') para o calculo do seu fatoria: \n"))

fatorial = 1

for i in range(fator , 0 , -1 ):
    
    fatorial = fatorial * i

print (fatorial)    
