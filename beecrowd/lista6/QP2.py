def cal_imposto(salario):
    imposto = 0.0

    if salario <= 2000.00:
        return "Isento"
    elif salario <= 3000.00:
        imposto = (salario - 2000.00) * 0.08
    elif salario <= 4500.00:
        imposto = (salario - 3000.00) * 0.18 + (1000.00 * 0.08)
    else:
        imposto = (salario - 4500.00) * 0.28 + (1500.00 * 0.18) + (1000.00 * 0.08)

    return round(imposto, 2)


salario = float(input())
imposto = cal_imposto(salario)
if imposto == "Isento":
    print(imposto)
else:
    print(f"R$ {imposto:.2f}")
