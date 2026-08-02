bac_A = 4
bac_B = 10

dia = 1

while bac_A <= bac_B:
    bac_A = bac_A + (bac_A * 0.03)
    bac_B = bac_B + (bac_B * 0.015)

    dia += 1

print(f"A bactéria A levou {dia} dias para alcaçar a B")   