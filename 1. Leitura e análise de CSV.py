import pandas as pd
# Ler o arquivo CSV
arquivo_csv = 'vendas.csv'
df = pd.read_csv(arquivo_csv)

# Calcular o total vendido por produto
df['Total'] = df['Quantidade'] * df['Preço']
total_vendido = df.groupby('Produto')['Total'].sum().reset_index()

# Identificar o produto mais vendido
produto_mais_vendido = total_vendido.loc[total_vendido['Total'].idxmax()]

# Gerar relatório
relatorio = f"Produto mais vendido: {produto_mais_vendido['Produto']}\nTotal vendido: R$ {produto_mais_vendido['Total']:.2f}"

print(relatorio)

# Salvar relatório em um arquivo
with open('relatorio_vendas.txt', 'w') as f:
    f.write(relatorio)
