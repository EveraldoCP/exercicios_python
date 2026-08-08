print('VOTAÇÃO PARA NOVO GERENTE--')
print("Para escolher seu candidato digite de 1 a 4. Para anular digite 5 e para voto em branco digite 6")

contador = 0

candidato_A = 0
candidato_B = 0
candidato_C = 0
candidato_D = 0 
nulo = 0
branco = 0

while contador <= 20:
   contador+=1
   voto_candidato = int(input("Vote agora: "))
   if voto_candidato == 1:
      candidato_A += 1
      print("Voto para o candidato 1 computado")
   elif voto_candidato == 2:
      candidato_B += 1
      print("Voto para o candidato 2 computado") 
   elif voto_candidato == 3:
         candidato_C += 1
         print("Voto para o candidato 3 computado")
   elif voto_candidato == 4:
         candidato_D += 1
         print("Voto para o candidato 4 computado")
   elif voto_candidato == 5:
        nulo += 1
        print("Voto anulado")
   elif voto_candidato == 6:
         branco += 1
         print("Voto em branco computado")

votos_totais =  contador
porcento_1 = (candidato_A / contador) * 100
porcento_2 = (candidato_B / contador) * 100
porcento_3 = (candidato_C / contador) * 100
porcento_4 = (candidato_D / contador) * 100
porcento_5 = (nulo / contador) * 100
porcento_6 = (branco / contador) * 100   

print("--RESULTADO DA VOTAÇÃO--")
print(f"O candidato 1: {candidato_A} votos {porcento_1:.1f}% dos votos")
print(f"O candidato 2: {candidato_B} votos {porcento_2:.1f}% dos votos")
print(f"O candidato 3: {candidato_C} votos {porcento_3:.1f}% dos votos")
print(f"O candidato 4: {candidato_D} votos {porcento_4:.1f}% dos votos")
print(f"Votos nulos totais: {nulo} - {porcento_1:.1f}% dos votos")
print(f"Votos em branco totais: {branco} - {porcento_1:.1f}% dos votos")

print ("Obrigado por contribuir - VIVA A DEMOCRACIA!!")

                            
