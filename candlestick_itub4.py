# Na primeira vez que for rodar o programa, abra o terminal e copie a linha abaixo
# pip install plotly pandas-datareader yfinance ou se for no Jupter Notebook -> !pip install plotly pandas-datareader yfinance

import plotly.graph_objects as go
import pandas_datareader.data as pdr
import yfinance

yfinance.pdr_override()

ativo = "ITUB4.SA"

tabela_cotacoes = pdr.get_data_yahoo(ativo, "2016-08-01","2024-09-15")

display(tabela_cotacoes)

grafico = go.Figure(
	data=[go.Candlestick(x=tabela_cotacoes.index, open=tabela_cotacoes["Open"], close=tabela_cotacoes["Close"], high=tabela_cotacoes["High"], low=tabela_cotacoes["Low"])]
)
# Esta tabela retira um mini-gráfico que fica abaixo do gráfico normal
grafico.update_layout(xaxis_rangeslider_visible=False)

grafico.show()