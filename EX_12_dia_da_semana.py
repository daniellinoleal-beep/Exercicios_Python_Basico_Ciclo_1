# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

numero = float(input("digite um numero"))

if numero == 1:
    print("domingo")
elif numero ==2:
    print("segunda")
elif numero ==3:
    print("terça")
elif numero ==4:
    print("quarta")
elif numero ==5:
    print("quinta")
elif numero ==6:
    print("sexta")
elif numero ==7:
    print("sabado")
else:
    ("numero errado")