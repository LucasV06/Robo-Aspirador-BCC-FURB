# 🤖 Robô Aspirador — BCC FURB

Projeto acadêmico desenvolvido para a **FURB (Universidade Regional de Blumenau)**, com o objetivo de desenvolver um sistema de **robô aspirador autônomo** capaz de identificar se uma sala está limpa ou suja e, a partir dessa informação, realizar a limpeza e se movimentar para a próxima sala.

## 👥 Integrantes

* **Lucas Visconti**
* **Luiz Carlos Martendal**
* **Fabian Formento**
* **Cauã Bertolini**
* **Eduarda Dagnoni Mazureck**

## 🎯 Objetivo

Desenvolver um sistema capaz de:

* Identificar o estado de limpeza de uma sala;
* Realizar a limpeza quando necessário;
* Movimentar-se de forma autônoma entre as salas;
* Determinar a próxima sala a ser visitada.

## 🏫 Instituição

**Universidade Regional de Blumenau — FURB**
**Curso:** Ciência da Computação

## 📁 Versões

* `version-001/`: versão original (geração do ambiente 6x6 com paredes e sujeira).
* `version-002/`: expande a `version-001` para atender à atividade avaliativa
  "Aspirador de Pó Automático":
  * `ambiente.py` — geração da sala, agora com funções auxiliares
    (`eh_parede`, `tem_sujeira`, `limpar`, `sala_esta_limpa`) e sem o bug de
    sorteio de sujeira repetida.
  * `agente_reflexo_simples.py` — **Questão 1**: `agenteReativoSimples(percepcao)`
    e `funcaoMapear(percepcao)`, construídas a partir de um ciclo hamiltoniano
    que garante limpar a sala 4x4 inteira a partir de qualquer posição inicial.
  * `agente_objetivo.py` — **Questão 2**: `agenteObjetivo(percepcao, objObtido)`,
    `checkObj(sala)` e o contador `pontos`.
  * `main.py` — roda as duas simulações e imprime o resultado.
  * `RESPOSTAS.md` — respostas às perguntas conceituais do enunciado
    (extensibilidade para 3x3/6x6 e garantia de limpeza total).
