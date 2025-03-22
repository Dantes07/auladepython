import pandas as pd
from plyer import notification

dados = pd.read_csv('vendas.csv')

dados['TvP'] = dados['quantidade'] * dados['preco']

total_por_produto = dados.groupby('produto')['TvP'].sum()

produto_mais_vendido = total_por_produto.idxmax()
total_vendido_produto_mais_vendido = total_por_produto.max()
total_geral_vendas = total_por_produto.sum()

relatorio_resumo = f"Produto mais vendido: {produto_mais_vendido}\nTotal geral de vendas: R$ {total_geral_vendas:.2f}"

notification.notify(
    title='Resumo de Vendas',
    message=relatorio_resumo,
    timeout=10  
)

print(f"Relatório:\nProduto Mais Vendido: {produto_mais_vendido}\nTotal Geral de Vendas: R$ {total_geral_vendas:.2f}")