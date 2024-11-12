def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


def verificar_vencedor(tabuleiro, jogador):
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] == jogador:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False


def verificar_empate(tabuleiro):
    for linha in tabuleiro:	
        if " " in linha:
            return False
    return True

def jogar():
    tabuleiro = [
        [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
    ]
    jogador_atual = "X"
    
    while True:
        exibir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}. Escolha uma linha e uma coluna (0, 1 ou 2):")
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Posição inválida, tente novamente.")
            continue
        
        if verificar_vencedor(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {jogador_atual} venceu!")
            break
        
        if verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("O jogo terminou em empate!")
            break
        
        jogador_atual = "O" if jogador_atual == "X" else "X"

jogar()
