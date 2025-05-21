from collections import defaultdict

def gerar_relatorio(registros):
    agrupado_por_data = defaultdict(list)

    for registro in registros:
        data = registro['data']
        agrupado_por_data[data].append(registro)

    for data in sorted(agrupado_por_data.keys()):
        print(f"\n📅 {data}:")
        tipos = defaultdict(list)
        for r in agrupado_por_data[data]:
            tipos[r['tipo']].append(float(r['valor']))  # assumindo que valor foi convertido no parser
        
        for tipo, valores in tipos.items():
            soma = sum(valores)
            media = soma / len(valores)
            print(f"  {tipo}: soma = {soma}, média = {media}")
