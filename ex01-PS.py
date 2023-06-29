#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# Exercício 1: Pêndulo Simples
# Escreva um programa que calcule o período de um pêndulo simples, 
# dado o comprimento e a aceleração da gravidade. O programa deve 
# imprimir o período de oscilação.

# Exemplo de saída:
# Digite o comprimento do pêndulo: 5
# O período de oscilação é: 4.487989505128276 s

# importação de bibliotecas
import math

# entrada de dados
comprimento = float(input("Digite o comprimento do pêndulo: "))
aceleracaoGravidade = 9.8

periodo = 2 * math.pi * math.sqrt(comprimento / aceleracaoGravidade)

print(f"O período de oscilação é: {periodo} s")
