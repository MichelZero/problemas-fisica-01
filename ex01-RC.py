#
# autores: Michel e Cristiano

# data: 29/06/2023

# fazer o programa usando o while.

# Exercício 1: Resistência em Circuitos
# Escreva um programa que calcule a resistência equivalente em um circuito elétrico 
# composto por resistores em série ou em paralelo. O programa deve solicitar ao 
# usuário que escolha o tipo de circuito (série ou paralelo) e, em seguida, 
# solicitar os valores das resistências até que o usuário decida parar. O programa 
# deve imprimir a resistência equivalente final.

# Exemplo de saída:
# Escolha o tipo de circuito (série(S) ou paralelo(P)): s
# Digite o valor da resistência (ou digite 0 para sair): 5
# Digite o valor da resistência (ou digite 0 para sair): 2
# Digite o valor da resistência (ou digite 0 para sair): 3
# Digite o valor da resistência (ou digite 0 para sair): 0
# A resistência equivalente é: 10.0 ohms

# Escolha o tipo de circuito (série(S) ou paralelo(P)): p
# Digite o valor da resistência (ou digite 0 para sair): 5
# Digite o valor da resistência (ou digite 0 para sair): 2
# Digite o valor da resistência (ou digite 0 para sair): 3
# Digite o valor da resistência (ou digite 0 para sair): 0
# A resistência equivalente é: 0.9677419354838711 ohms


# entrada de dados
resistenciaEquivalente = 0
tipoCircuito = input("Escolha o tipo de circuito (série(S) ou paralelo(P)): ")

while True:
    resistencia = float(input("Digite o valor da resistência (ou digite 0 para sair): "))
    if resistencia == 0:
        break
    if tipoCircuito.upper() == "S":
        resistenciaEquivalente += resistencia
    elif tipoCircuito.upper() == "P":
        resistenciaEquivalente += 1 / resistencia

if tipoCircuito.upper() == "P":
    resistenciaEquivalente = 1 / resistenciaEquivalente

print(f"A resistência equivalente é: {resistenciaEquivalente} ohms")
