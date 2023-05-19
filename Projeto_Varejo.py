##importa bibliotecas 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

#le o arquivo csv
df_dsa = pd.read_csv('dados/dataset.csv')


# print(df_dsa.dtypes) #ve o tipo de dados do dataset
# print(df_dsa['Valor_Venda'].describe()) #descreve alguns KPIs do valor venda
# print(df_dsa.isnull().sum()) #verifica se tem NULL no dataset
print(df_dsa.head())

### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
df1 = df_dsa[df_dsa['Categoria'] == 'Office Supplies']
df1_total = df1.groupby('Cidade')['Valor_Venda'].sum() #agrupa a coluna cidade e venda
cidade_maior_venda = df1_total.idxmax()
# print("Cidade com maior valor de venda para 'Office Supplies':", cidade_maior_venda)

### Qual o Total de Vendas Por Data do Pedido? Demonstre o resultado através de um gráfico de barras.
df2 = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()

##plota o grafico de total de vendas por data de pedido
# plt.figure(figsize=(20,5))
# df2.plot(x= 'Data_Pedido', y = 'Valor_Venda', color= 'b')
# plt.xlabel('Data pedido')
# plt.ylabel('Valor Venda')
# plt.title("Total de vendas por data do pedido.")
# plt.show()

### Qual o Total de Vendas por Estado? Demonstre o resultado através de um gráfico de barras.
df3 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()
# plt.figure(figsize=(20,6))
# sns.barplot(data = df3, x = 'Estado', y ='Valor_Venda').set(title = 'Total de vendas por Estado.')
# plt.xticks(rotation= 70)
# plt.show()

### Quais São as 10 Cidades com Maior Total de Vendas? Demonstre o resultado através de um gráfico de barras.
df4 = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().nlargest(10,['Valor_Venda'])
# plt.figure(figsize=(20,6))
# sns.set_palette('colorblind')
# sns.barplot(data = df4, x = 'Cidade', y ='Valor_Venda').set(title = 'Total de vendas por cidade.')
# plt.xticks(rotation= 70)
# plt.show()

### Qual Segmento Teve o Maior Total de Vendas? Demonstre o resultado através de um gráfico de pizza.
def formatacao_dados(values):
    def formatar(pct):
        total = sum(values)
        val = int(round(pct*total/100))
        return '${v:d}'.format(v= val)
    return formatar
df5 = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index()
# fig, ax = plt.subplots()
# ax.pie(df5['Valor_Venda'], labels =df5['Segmento'], autopct=formatacao_dados(df5['Valor_Venda']), shadow=True)
# ax.set_title('Total de vendas por segmento.')
# plt.show()

### Qual o Total de Vendas Por Segmento e Por Ano?
# df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst= True)
# df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
## OU
df_dsa['Ano'] = df_dsa['Data_Pedido'].str.split('/').str[2]
df6 = df_dsa.groupby(['Ano','Segmento'])['Valor_Venda'].sum()

# Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
### Quantas Vendas Receberiam 15% de Desconto?


# df_maior = df_dsa[df_dsa['Valor_Venda'] > 1000]
# df_menor = df_dsa[df_dsa['Valor_Venda'] < 1000]
# print(f"A quantidade de vendas que receberiam 15% de desconto seriam {df_maior['Valor_Venda'].count()} vendas.")
# print(f"A quantidade de vendas que receberiam 10% de desconto seriam {df_menor['Valor_Venda'].count()} vendas.")
#OU
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.85,0.9)
df_dsa['Desconto'].value_counts()
desc_maior = df_dsa[df_dsa['Desconto'] == 0.85]
desc_menor = df_dsa[df_dsa['Desconto'] == 0.9]

# print(f"A quantidade de vendas que receberiam 15% de desconto seriam {desc_maior['Desconto'].count()} vendas.")
# print(f"A quantidade de vendas que receberiam 10% de desconto seriam {desc_menor['Desconto'].count()} vendas.")

### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

media_antes = df_dsa[df_dsa['Valor_Venda'] > 1000]
media_depois = media_antes['Valor_Venda']*0.85
# print(f"A média de vendas antes do desconto foi de R${media_antes['Valor_Venda'].mean():.2f} e depois do desconto foi de R${media_depois.mean():.2f}.")

### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês? Demonstre o resultado através de gráfico de linha.
df_dsa['Mes'] = df_dsa['Data_Pedido'].str.split('/').str[1]
df7 =df_dsa.groupby(['Segmento', 'Mes', 'Ano'])['Valor_Venda'].agg([np.mean])

segmentos = df7.index.get_level_values(0)
meses = df7.index.get_level_values(1)
anos = df7.index.get_level_values(2)

##realizando grafico com a biblioteca seaborn
# plt.figure(figsize=(20,6))
# sns.set()
# fig1 = sns.relplot(kind= 'line',
#                    data= df7,
#                    y= 'mean',
#                    x=meses,
#                    hue=segmentos,
#                    col=anos,
#                    col_wrap= 4)
# plt.show()

### Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias? Demonstre tudo através de um único gráfico.
df8 = df_dsa.groupby(['Categoria', 'SubCategoria']).sum(numeric_only= True).sort_values('Valor_Venda', ascending= False).head(12)
df8 = df8[['Valor_Venda']].astype(int).sort_values(by = 'Categoria').reset_index()

topdoze = df8.groupby('Categoria').sum(numeric_only = True).reset_index()

##cores em hexadecimal
cores_categorias = ['#5d00de',
                    '#0ee84f',
                    '#e80e27']

cores_subcategorias = ['#aa8cd4',
                       '#aa8cd5',
                       '#aa8cd6',
                       '#aa8cd7',
                       '#26c957',
                       '#26c958',
                       '#26c959',
                       '#26c960',
                       '#e65e65',
                       '#e65e66',
                       '#e65e67',
                       '#e65e68']

fig,ax = plt.subplots(figsize = (18,12))
p1 = ax.pie(topdoze['Valor_Venda'],
       radius = 1,
       labels = topdoze['Categoria'], 
       wedgeprops= dict(edgecolor = 'white'),
       colors= cores_categorias,
       )
p2 = ax.pie(df8['Valor_Venda'],
            radius= 0.9,
            labels= df8['SubCategoria'],
            autopct= formatacao_dados(df8['Valor_Venda']),
            colors= cores_subcategorias,
            labeldistance=0.7,
            wedgeprops= dict(edgecolor = 'white'),
            pctdistance= 0.53,
            rotatelabels= True)
centre_circle = plt.Circle((0,0), 0.6, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Total de vendas por categoria e top 12 subcategorias.')
plt.show()
