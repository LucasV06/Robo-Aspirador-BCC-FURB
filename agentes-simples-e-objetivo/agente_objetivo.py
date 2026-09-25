
from agente_simples import proxima_direcao

pontos = 0


def checkObj(sala: list[list[int]]) -> int:

    SUJEIRA = 2
    return 1 if any(SUJEIRA in linha for linha in sala) else 0


def agenteObjetivo(percepcao: dict, objObtido: int) -> str:

    global pontos

    if objObtido == 0:
        return "NoOp"

    linha, coluna = percepcao["posicao"]
    sujeira = percepcao["sujeira"]

    if sujeira:
        acao = "aspirar"
    else:
        acao = proxima_direcao(linha, coluna)

    pontos += 1
    return acao


def reiniciar_pontos() -> None:
    global pontos
    pontos = 0
