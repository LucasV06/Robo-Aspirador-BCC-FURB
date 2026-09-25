LINHAS = 4
COLUNAS = 4


def proxima_direcao(linha: int, coluna: int) -> str:
    
    if coluna == 1:
        if linha > 1:
            return "acima"
        return "direita" 

    if linha % 2 == 1:
        if coluna < COLUNAS:
            return "direita"
        return "abaixo" 

    if coluna > 2:
        return "esquerda"
    if linha < LINHAS:
        return "abaixo" 
    return "esquerda" 


def funcaoMapear(percepcao: dict) -> str:
    linha, coluna = percepcao["posicao"]
    sujeira = percepcao["sujeira"]

    if sujeira:
        return "aspirar"

    return proxima_direcao(linha, coluna)


def agenteReativoSimples(percepcao: dict) -> str:
    return funcaoMapear(percepcao)
