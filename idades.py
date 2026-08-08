idade_pensao = int(input("Digite a idade do pensionista: "))

contador = 0

while idade_pensao >=0:
    contador += 1
    if idade_pensao >= 0 and idade_pensao <= 25:
        print( "Pertence ao grupo A (entre 0 e 25 anos)")
        
    elif idade_pensao >= 26 and idade_pensao <= 50:
        print("Pertence ao grupo B (entre 26 a 50 anos)")
        
    elif idade_pensao >= 51 and idade_pensao <= 75:
        print("Pertence ao grupo C (entre 51 a 75 anos)")
        
    elif idade_pensao >= 76 and idade_pensao <= 100:
        print("Pertence ao grupo D (entre 76 a 100 anos)")
        
    idade_pensao = int(input("Digite a idade do pensionista: "))

print(f"Total de idades verificadas = {contador}")
                    