# Atualize o código de aluguel de carros feito anteriormente. 
# Crie um programa em Python que simule o cálculo do valor total a ser pago pelo aluguel de um carro. O programa deve:
# 1- Perguntar ao usuário qual foi o modelo do carro alugado.
# 2- Perguntar por quantos dias o carro foi alugado.
# 3- Perguntar quantos quilômetros foram percorridos com o carro.
# 4- Usar uma tabela de preços (pré-definida pelo próprio aluno) para determinar o valor diário de aluguel de acordo com o modelo do carro.
# 5- Calcular o custo total com base:
# 6- No número de dias alugados × valor por dia
# 7- No total de quilômetros rodados × R$0,15 por km
# 8- Exibir o valor total a ser pago, com duas casas decimais.

# Os alunos são livres para definir quais modelos de carro o programa aceitará e o valor por dia de cada um.

# Se o modelo inserido pelo usuário não estiver na lista, o programa deve aplicar um valor padrão por dia.

# OUTPUT ESPERADO: 

# ----------------------------------------------------- EXEMPLO 1

# Qual foi o modelo do carro alugado? uno
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100
# Você andou 100.0km por 10 dias, então o preço a pagar é R$415.00.

# ----------------------------------------------------- EXEMPLO 2

# Qual foi o modelo do carro alugado? bmw
# Por quantos dias o carro foi alugado: 10 
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$10015.00.

# ----------------------------------------------------- EXEMPLO 3(PREÇO PADRÃO)

# Qual foi o modelo do carro alugado? fox
# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 100 
# Você andou 100.0km por 10 dias, então o preço a pagar é R$615.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

tabela_precos = {
    "gol": 80,
    "hb20": 100,
    "corolla": 180,
    "civic": 200
}


valor_padrao = 120

modelo = input("Digite o modelo do carro alugado: ").lower()
dias = int(input("Digite a quantidade de dias alugados: "))
km = float(input("Digite a quantidade de quilômetros percorridos: "))

if modelo in tabela_precos:
    valor_dia = tabela_precos[modelo]
else:
    print("Modelo não encontrado. Será aplicado o valor padrão.")
    valor_dia = valor_padrao

custo_dias = dias * valor_dia
custo_km = km * 0.15
valor_total = custo_dias + custo_km

print("\n===== RESUMO DO ALUGUEL =====")
print(f"Modelo do carro: {modelo}")
print(f"Valor da diária: R$ {valor_dia:.2f}")
print(f"Custo pelos dias alugados: R$ {custo_dias:.2f}")
print(f"Custo pelos quilômetros rodados: R$ {custo_km:.2f}")
print(f"Valor total a pagar: R$ {valor_total:.2f}")