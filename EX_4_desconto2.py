# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto (%): "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print("Resultado")
print(f"Produto: {nome}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final do produto: R$ {preco_final:.2f}")