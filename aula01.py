# calcular o valor do bonus de um funcionario, baseando-se no seu nome, salario e porcentagem de bonus
# o calculo deve ser feito de acordo com as seguintes regras: 1000 + salario * bonus
# o nome do funcionario e um string, o salario um float, e o bonus um float e todos os campos devem ser informados pelo usuario
def calcular_bonus(nome, salario, bonus):
    return 1000 + salario * bonus

nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
bonus = float(input("Digite a porcentagem de bônus (em decimal): "))

valor_bonus = calcular_bonus(nome, salario, bonus)
print(f"O valor do bônus para {nome} é: {valor_bonus}")
