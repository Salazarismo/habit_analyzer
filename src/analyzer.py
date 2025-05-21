from parser import ler_arquivo
from reporter import gerar_relatorio


def analisar_dados(registros):
    contagem = {}

    for registro in registros:
        tipo = registro['tipo']
        if tipo in contagem:
            contagem[tipo] += 1
        else:
            contagem[tipo] = 1

    return contagem


if __name__ == "__main__":
    caminho = "data/logs.txt"
    registros = ler_arquivo(caminho)

    resultados = analisar_dados(registros)
    print("Resumo das atividades:")
    for tipo, qtd in resultados.items():
        print(f"{tipo}: {qtd} vezes")

    gerar_relatorio(registros)
