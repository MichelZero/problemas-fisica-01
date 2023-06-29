#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# Exercício 1: Lançamento Oblíquo
# Escreva um programa que calcule a trajetória de um objeto lançado 
# obliquamente, considerando o ângulo de lançamento, a velocidade 
# inicial e a aceleração da gravidade. O programa deve solicitar 
# o tempo total de simulação e imprimir as coordenadas x e y a cada segundo.

# Exemplo de saída:
# Digite o tempo total de simulação: 5
# Digite o ângulo de lançamento (em graus): 45
# Digite a velocidade inicial: 1
# Tempo: 0 s - Posição (x, y): 0.0, 0.0
# Tempo: 1 s - Posição (x, y): 0.7071067811865476, -4.1928932188134524
# Tempo: 2 s - Posição (x, y): 1.4142135623730951, -18.185786437626906
# Tempo: 3 s - Posição (x, y): 2.121320343559643, -41.978679656440356
# Tempo: 4 s - Posição (x, y): 2.8284271247461903, -75.57157287525382
# Tempo: 5 s - Posição (x, y): 3.5355339059327378, -118.96446609406728

# import math
import math
# entrada de dados
tempoTotal = int(input("Digite o tempo total de simulação: "))
tempo = 0
anguloLancamento = float(input("Digite o ângulo de lançamento (em graus): "))
velocidadeInicial = float(input("Digite a velocidade inicial: "))
aceleracaoGravidade = 9.8

anguloRad = math.radians(anguloLancamento)
velocidadeInicial_x = velocidadeInicial * math.cos(anguloRad)
velocidadeInicial_y = velocidadeInicial * math.sin(anguloRad)

while tempo <= tempoTotal:
    posicao_x = velocidadeInicial_x * tempo
    posicao_y = velocidadeInicial_y * tempo - 0.5 * aceleracaoGravidade * tempo**2
    #print("Tempo:", tempo, "s - Posição (x, y):", posicao_x, ",", posicao_y)
    print(f"Tempo: {tempo} s - Posição (x, y): {posicao_x}, {posicao_y}")
    tempo += 1
