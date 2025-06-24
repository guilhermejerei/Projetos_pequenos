import random


switch = {
    1: "pedra",
    2: "papel",
    3: "tesoura"
}

qtde_jogos = 0
pontos_jogador = 0
pontos_computador = 0

print("\nBem-vindo ao jogo Pedra, Papel, Tesoura!")
print("\nQual é o seu nome?")
nome = str(input("Digite seu nome: "))

while True:
    try:
        print(f"\n{nome}, quantos jogos você deseja jogar?")
        qtde_jogos = int(input("Digite um número inteiro positivo: "))
        if qtde_jogos > 0:
            break
        else:
            print("\nOpção inválida! Tente novamente.")
    except ValueError:
        print("\nEntrada inválida!")


def verificar_vencedor(jogador_usuario, jogador_computador):
    regras = {
        1: 3,  # pedra vence tesoura
        2: 1,  # papel vence pedra
        3: 2   # tesoura vence papel
    }
    if jogador_usuario == jogador_computador:
        return "Empate"
    elif regras[jogador_usuario] == jogador_computador:
        return "Jogador"
    else:
        return "Computador"

for i in range(qtde_jogos):
    print(f"\nJogo {i + 1} de {qtde_jogos}")
    print("\nEscolha sua jogada:")
    for key in switch:
        print(f"{key} - {switch[key]}")
    while True:
        try:
            jogador_usuario = int(input(f"{nome}, escolha:"))
            if jogador_usuario in switch:
                break
            else:
                print("\nOpção inválida! Tente novamente.")
        except ValueError:
            print("\nEntrada inválida!")

    jogador_computador = random.randint(1, 3)

    print(f"{nome} escolheu: {switch[jogador_usuario]}")
    print(f"Computador escolheu: {switch[jogador_computador]}")

    vencedor = verificar_vencedor(jogador_usuario, jogador_computador)
    if vencedor == "Empate":
        print("Empate!")
    elif vencedor == "Jogador":
        print(f"{nome} venceu!")
        pontos_jogador += 1
    else:
        print("Computador venceu!")
        pontos_computador += 1

    print(f"Pontos - {nome}: {pontos_jogador}, Computador: {pontos_computador}")

print("\nFim de jogo!")
print(f"Placar final - {nome}: {pontos_jogador}, Computador: {pontos_computador}")
if pontos_jogador > pontos_computador:
    print(f"{nome} é o grande vencedor!")
elif pontos_jogador < pontos_computador:
    print("Computador é o grande vencedor!")
else:
    print("O jogo terminou empatado!")
    while pontos_jogador == pontos_computador:
        print("\nEmpate! Vamos jogar mais uma rodada para desempatar.")
        while True:
            try:
                for key in switch:
                    print(f"{key} - {switch[key]}")
                jogador_usuario = int(input(f"{nome}, escolha:"))
                if jogador_usuario in switch:
                    break
                else:
                    print("\nOpção inválida! Tente novamente.")
            except ValueError:
                print("\nEntrada inválida!")
        jogador_computador = random.randint(1, 3)
        print(f"{nome} escolheu: {switch[jogador_usuario]}")
        print(f"Computador escolheu: {switch[jogador_computador]}")
        vencedor = verificar_vencedor(jogador_usuario, jogador_computador)
        if vencedor == "Empate":
            print("\nEmpate novamente! Continuando o desempate...")
        elif vencedor == "Jogador":
            print(f"{nome} venceu o desempate!")
            pontos_jogador += 1
        else:
            print("\nComputador venceu o desempate!")
            pontos_computador += 1

    if pontos_jogador > pontos_computador:
        print(f"\n{nome} é o grande vencedor!")
    else:
        print("\nComputador é o grande vencedor!")