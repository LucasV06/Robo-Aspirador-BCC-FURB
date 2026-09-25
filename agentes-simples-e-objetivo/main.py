import random

import ambiente
import agente_simples as ars
import agente_objetivo as ao

MOVIMENTOS = {
    "acima": (-1, 0),
    "abaixo": (1, 0),
    "esquerda": (0, -1),
    "direita": (0, 1),
}


def aplicar_acao(sala, posicao, acao):
    linha, coluna = posicao

    if acao == "aspirar":
        ambiente.limpar(sala, linha, coluna)
        return posicao

    if acao == "NoOp":
        return posicao

    delta_linha, delta_coluna = MOVIMENTOS[acao]
    nova_posicao = (linha + delta_linha, coluna + delta_coluna)

    if ambiente.eh_parede(sala, *nova_posicao):
        return posicao

    return nova_posicao


def rodar_agente_reativo_simples(sala, posicao_inicial, passos_max=30):
    posicao = posicao_inicial
    passo_da_limpeza_total = None

    print("=== Agente Reativo Simples (questão 1) ===")
    print(f"Posição inicial sorteada: {posicao_inicial}")
    ambiente.imprimir_sala(sala)

    for passo in range(1, passos_max + 1):
        sujeira = ambiente.tem_sujeira(sala, *posicao)
        percepcao = {"posicao": posicao, "sujeira": sujeira}
        acao = ars.agenteReativoSimples(percepcao)
        posicao = aplicar_acao(sala, posicao, acao)

        if passo_da_limpeza_total is None and ambiente.sala_esta_limpa(sala):
            passo_da_limpeza_total = passo

    if passo_da_limpeza_total is not None:
        print(
            f"A sala ficou totalmente limpa no passo de número {passo_da_limpeza_total}, "
            f"mas o agente continuou andando até "
            f"completar os {passos_max} passos"
        )
    else:
        print(f"Após {passos_max} passos a sala ainda não ficou totalmente limpa.")

    print()


def rodar_agente_objetivo(sala, passos_max=64):
    ao.reiniciar_pontos()
    posicao = (1, 1)
    print("=== Agente Baseado em Objetivos (questão 2) ===")
    ambiente.imprimir_sala(sala)

    for _ in range(passos_max):
        objObtido = ao.checkObj(sala)
        sujeira = ambiente.tem_sujeira(sala, *posicao)
        percepcao = {"posicao": posicao, "sujeira": sujeira}
        acao = ao.agenteObjetivo(percepcao, objObtido)

        if acao == "NoOp":
            break

        posicao = aplicar_acao(sala, posicao, acao)

    print(f"Sala limpa! Total de passos até atingir o objetivo (pontos): {ao.pontos}\n")


if __name__ == "__main__":
    sala_1 = ambiente.gerar_ambiente(6, 6, 4)
    posicao_aleatoria = (
        random.randint(1, ars.LINHAS),
        random.randint(1, ars.COLUNAS),
    )
    rodar_agente_reativo_simples(sala_1, posicao_aleatoria)

    sala_2 = ambiente.gerar_ambiente(6, 6, 4)
    rodar_agente_objetivo(sala_2)
