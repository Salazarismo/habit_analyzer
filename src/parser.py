def ler_arquivo(caminho):
    with open(caminho, 'r') as arquivo:
        linhas = arquivo.readlines()
        dados = []

        for linha in linhas:
            linha = linha.strip()
            partes = linha.split(", ")

            if len(partes) == 3:
                data, tipo, valor = partes
                dados.append({
                    "data": data,
                    "tipo": tipo,
                    "valor": float(valor)
                })

        return dados


if __name__ == "__main__":
    caminho_do_arquivo = "data/logs.txt"
    registros = ler_arquivo(caminho_do_arquivo)

    for r in registros:
        print(f"{r['data']} - {r['tipo']}: {r['valor']}")
