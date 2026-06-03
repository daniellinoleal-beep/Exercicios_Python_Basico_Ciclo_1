# Escreva um programa que pede ao usuario que pede o nome de um aluno e as notas de 3 provasuno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
nome = ("Digite um nome")

nota1 = float(input("Digite uma nota: "))
nota2 = float(input("Digite uma segunda nota: "))
nota3 = float(input("Digite uma terceira nota: "))

media = (nota1 + nota2 + nota3) /3

print("Aluno:", nome)
print("Média das 3 provas:", media)
if media >=5:
    print("aprovado")
else:
    print("reprovado")
