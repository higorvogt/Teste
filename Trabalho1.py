nomeA = input("Digite o nome do primeiro jogador: ")
while True:
    try:
        resultadoNomeA = int(input("Quantos gols o primeiro jogador fez? "))
        if resultadoNomeA < 0:
            print("*** SOMENTE NÚMEROS INTEIROS ENTRE 0 E +∞ SÃO ACEITOS ***")
        else:
            break
    except ValueError:
        print("*** SOMENTE NÚMEROS INTEIROS ENTRE 0 E +∞ SÃO ACEITOS ***")
print("\n")
 
#Jogador 1
nomeB = input("Digite o nome do segundo jogador: ")
while True:
    try:
        resultadoNomeB = int(input("Quantos gols o segundo jogador fez? "))
        if resultadoNomeB < 0:
            print("*** SOMENTE NÚMEROS INTEIROS ENTRE 0 E +∞ SÃO ACEITOS ***")
        else:
            break
    except ValueError:
        print("*** SOMENTE NÚMEROS INTEIROS ENTRE 0 E +∞ SÃO ACEITOS ***")
print("\n")
 
#Comparação de gols entre os dois jogadores
if resultadoNomeA > resultadoNomeB:
    print("Vitória de ", nomeA)
elif resultadoNomeB > resultadoNomeA:
    print("Vitória de ", nomeB)
else:
    print("O jogo deu empate de: ", resultadoNomeA, " a ", resultadoNomeB )