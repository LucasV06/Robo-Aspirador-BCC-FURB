import random


def gerar_ambiente(largura_sala: int, comprimento_sala: int, quantidade_sujeira: int) -> list[list[int]]:
    sala = []

    for x in range(largura_sala):
        larg = []
        for y in range(comprimento_sala):
            if x == 0 or x == largura_sala - 1 or y == 0 or y == comprimento_sala - 1:
                larg.append(1)  
            else:
                larg.append(0)  
        sala.append(larg)

    for _ in range(quantidade_sujeira):
        x = random.randint(1, largura_sala - 2)
        y = random.randint(1, comprimento_sala - 2)
        sala[y][x] = 2 

    return sala

def eh_parede(sala: list[list[int]], x: int, y: int) -> bool:
    return sala[x][y] == 1


def tem_sujeira(sala: list[list[int]], x: int, y: int) -> bool:
    return sala[x][y] == 2


def limpar(sala: list[list[int]], x: int, y: int) -> None:
    sala[x][y] = 0


def sala_esta_limpa(sala: list[list[int]]) -> bool:
    return not any(2 in linha for linha in sala)


def imprimir_sala(sala: list[list[int]]) -> None:
    for linha in sala:
        print(" ".join(str(celula) for celula in linha))
