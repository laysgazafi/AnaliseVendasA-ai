import pandas as pd
import plotly_express as px

dados = pd.read_excel("vendas.xlsx")

# grafico = px.histogram(dados, x="loja", y="preco", color="forma_pagamento", text_auto=True) #criando a variável
# grafico.show() #mostrando o gráfico
# grafico.write_html("grafico.html")

lista_colunas = ["loja", "cidade", "estado", "regiao", "tamanho", "local_consumo"]
for coluna in lista_colunas:
    grafico = px.histogram(dados, x=coluna, y="preco", color="forma_pagamento", text_auto=True)
    grafico.show()
    grafico.write_html(f"grafico-{coluna}.html")

agrupado = dados.groupby(["loja", "ano_mes"]).sum()
agrupado.reset_index(inplace=True)
agrupado["acumulado"] = agrupado.groupby("loja").cumsum()

fig = px.bar(agrupado,
            x = "acumulado",
            y = "loja",
            color = "loja",
            text_auto = True,
            range_x = [0,160000],
            animation_frame = "ano_mes")

fig.show()
fig.write_html("grafico-tempo.html")