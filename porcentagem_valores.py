valores = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

contador  = 0
total = len(valores)
for valor in valores:
    
    if valor >= 3000:
        contador += 1

porcentagem = (contador / total) * 100

print(porcentagem)
