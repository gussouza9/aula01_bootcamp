def calcular_bonus(nome, salario, bonus):
    return 1000 + salario * bonus

nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
bonus = float(input("Digite a porcentagem de bônus (em decimal): "))

valor_bonus = calcular_bonus(nome, salario, bonus)
print(f"O valor do bônus para {nome} é: {valor_bonus}")
