#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# Exercício 1: Movimento Uniforme
# Escreva um programa que calcule a posição de um objeto em movimento 
# uniforme a cada segundo, dado o tempo inicial, a velocidade e a 
# aceleração constantes. O programa deve solicitar o tempo total 
# de simulação e imprimir a posição a cada segundo.

# Exemplo de saída: 
# Digite o tempo total de simulação: 5
# Digite a posição inicial: 1
# Digite a velocidade: 2
# Tempo: 0 s - Posição: 1.0 m
# Tempo: 1 s - Posição: 3.0 m
# Tempo: 2 s - Posição: 5.0 m
# Tempo: 3 s - Posição: 7.0 m
# Tempo: 4 s - Posição: 9.0 m
# Tempo: 5 s - Posição: 11.0 m

# entrada de dados
tempoTotal = int(input("Digite o tempo total de simulação: "))
tempo = 0
posicaoInicial = float(input("Digite a posição inicial: "))
velocidade = float(input("Digite a velocidade: "))

# processamento
while tempo <= tempoTotal:
    posicao = posicaoInicial + velocidade * tempo
    print("Tempo:", tempo, "s - Posição:", posicao, "m")
    tempo += 1
