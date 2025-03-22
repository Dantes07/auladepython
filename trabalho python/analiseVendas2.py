import pandas as pd #importando a biblioteca pandas para ler um arquivo csv

dados  = pd.read_csv('vendas.csv') #declarando a varivel dados para puxar o arquivo csv (vendas)

dados ['total_vendido'] = dados ['quantidade'] * dados ['preco'] #criando as varives para fazer a leitura do total de vendas

total_por_produto = dados.groupby('produto')['total_vendido'].sum() #puxando os dados para fazer a operacao

produto_mais_vendido = total_por_produto.idxmax() #filtrando o produto de maior quantidade
total_vendido_produto_mais_vendido = total_por_produto.max()

#declarando a variavel relatorio para fazer uma lista
relatorio = {
    'Produto Mais Vendido': produto_mais_vendido,
    'Total Vendido do Produto Mais Vendido': total_vendido_produto_mais_vendido
}

print(f"Relatório:\nProduto Mais Vendido: {relatorio['Produto Mais Vendido']}\nTotal Vendido: {relatorio['Total Vendido do Produto Mais Vendido']}")
#imprimindo as informacoes da lista