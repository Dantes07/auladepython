def calcular_ticket_o_medio(total_vendas, numero_transacoes):
    return total_vendas / numero_transacoes

def calcular_margem_lucro(preco_venda, custo_produto):
    margem = (preco_venda - custo_produto) / preco_venda * 100
    return margem

def calcular_lucro(preco_venda, custo_produto):
    return preco_venda - custo_produto

total_vendas = 1000
numero_transacoes = 50

produtos = [
    {"nomes produtos": "Camisa", "preco_venda": 80, "custo_produto": 50},
    {"nomes produtos": "calca", "preco_venda": 60, "custo_produto": 40},
    {"nomes produtos": "bone", "preco_venda": 100, "custo_produto": 70},
    {"nomes produtos": "sapato", "preco_venda": 50, "custo_produto": 30},
    {"nomes produtos": "meia", "preco_venda": 120, "custo_produto": 90},
]

ticket_medio = calcular_ticket_o_medio(total_vendas, numero_transacoes)
print(f"Ticket Médio: R$ {ticket_medio:.2f}")

for produto in produtos:
    produto["margem_lucro"] = calcular_margem_lucro(produto["preco_venda"], produto["custo_produto"])
    print(f"Produto: {produto['nomes produtos']} - Margem de Lucro: {produto['margem_lucro']:.2f}%")

produtos_com_margem_baixa = sorted(produtos, key=lambda x: x["margem_lucro"])

print("\nProdutos com menor margem de lucro:")
for produto in produtos_com_margem_baixa[:3]:
    print(f"{produto['nomes produtos']} - Margem de Lucro: {produto['margem_lucro']:.2f}%")

for produto in produtos:
    produto["lucro"] = calcular_lucro(produto["preco_venda"], produto["custo_produto"])

produtos_mais_lucrativos = sorted(produtos, key=lambda x: x["lucro"], reverse=True)

print("\nTop 3 Produtos Mais Lucrativos:")
for produto in produtos_mais_lucrativos[:3]:
    print(f"{produto['nomes produtos']} - Lucro: R$ {produto['lucro']:.2f}")