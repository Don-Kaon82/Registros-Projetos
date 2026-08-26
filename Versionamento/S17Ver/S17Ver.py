# Função calcular total

def calcular_total(valor, taxa):
    if valor < 0:
        return 0

    total = valor + (valor * taxa)
    print("Total calculado:", total)

    return total


# Valores das variáveis

valor = 100
taxa = 0.10

# Cálculo do total

resultado = calcular_total(valor, taxa)

print("Resultado final:", resultado)