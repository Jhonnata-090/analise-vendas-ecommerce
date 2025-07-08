import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Visualizacao do grafico
sns.set(style='whitegrid')

#visualizacao pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

# carregando os dados
df= pd.read_csv('vendas_ecommerce.csv')
print(df.head())

#Tratando valores nulos
df= df.dropna()
print('Valores nulos:\n', df.isnull().sum())

# Tratamento data
df['data_pedido']= pd.to_datetime(df['data_pedido'])
print('Data corrigida: \n', df.head())

# Criando colunas auxiliares
df['valor_total']= df['preco_unitario']* df['quantidade']
df['mes_ano']= df['data_pedido'].dt.to_period('M')
print('Visualizando coluna auxiliar:\n', df.head(10))

print('Produtos mais vendidos:\n', df['produto'].value_counts().head(10))
print('Ticket medio por categoria:\n', df.groupby('categoria')['valor_total'].mean().sort_values(ascending=False))
print('Vendas por estado:\n', df.groupby('estado')['valor_total'].sum().sort_values(ascending=False))
print('Vendas por mes:\n', df.groupby('mes_ano')['valor_total'].sum())

# Produtos mais vendidos
plt.figure(figsize=(10, 5))
df['produto'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Produtos Mais Vendidos')
plt.ylabel('Quantidade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Ticket médio por categoria
plt.figure(figsize=(8, 4))
df.groupby('categoria')['valor_total'].mean().sort_values().plot(kind='barh')
plt.title('Ticket Médio por Categoria')
plt.xlabel('Valor Médio')
plt.show()

# Evolução das vendas por mês
plt.figure(figsize=(12, 6))
df.groupby('mes_ano')['valor_total'].sum().plot(marker='o')
plt.title('Evolução das Vendas por Mês')
plt.ylabel('R$')
plt.xlabel('Mês/Ano')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


