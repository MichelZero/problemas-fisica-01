#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# Exercício 1: Queda Livre
# Escreva um programa que calcule a altura de um objeto em queda livre a
# cada segundo, dado o tempo inicial e a aceleração da gravidade. O 
# programa deve solicitar o tempo total de queda e imprimir a altura 
# a cada segundo.

# Exemplo de saída:
# Digite o tempo total de queda: 5
# Digite a altura inicial: 200
# Tempo: 0 s - Altura: 200.0 m
# Tempo: 1 s - Altura: 195.1 m
# Tempo: 2 s - Altura: 180.4 m
# Tempo: 3 s - Altura: 155.9 m
# Tempo: 4 s - Altura: 121.6 m
# Tempo: 5 s - Altura: 77.49999999999999 m

# entrada de dados
tempoTotal = int(input("Digite o tempo total de queda: "))
tempo = 0
alturaInicial = float(input("Digite a altura inicial: "))
aceleracaoGravidade = 9.8

while tempo <= tempoTotal:
    altura = alturaInicial - 0.5 * aceleracaoGravidade * tempo**2
    print(f"Tempo: {tempo} s - Altura: {altura} m")
    tempo += 1
