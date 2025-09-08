import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar o CSV, ignorando linhas malformadas
df = pd.read_csv('books.csv', sep=",", on_bad_lines="skip")

# 2. Limpar nomes de colunas (remove espaços extras)
df.columns = df.columns.str.strip()

# 3. Remover colunas irrelevantes
df.drop(['isbn', 'isbn13', 'bookID'], axis=1, inplace=True)

# 4. Remover livros sem avaliações ou com menos de 30 páginas
df.drop(df[(df['ratings_count'] == 0) | (df['num_pages'] < 30)].index, inplace=True)

# 5. Resetar índice após remoções
df.reset_index(drop=True, inplace=True)

# 6. Remover datas inválidas
invalid_dates = []
for idx, date_str in enumerate(df['publication_date']):
    try:
        pd.to_datetime(date_str, format='%m/%d/%Y')
    except ValueError:
        invalid_dates.append(idx)

df.drop(index=invalid_dates, inplace=True)

# 7. Converter coluna de data para datetime
df['publication_date'] = pd.to_datetime(df['publication_date'], format='%m/%d/%Y')

# 8. Agrupar dados por título e idioma
aggregated_df = df.groupby(['title', 'language_code']).agg({
    'authors': lambda x: '/'.join(set(x)),
    'average_rating': 'mean',
    'num_pages': 'max',
    'ratings_count': 'sum',
    'text_reviews_count': 'sum',
    'publication_date': 'min',
    'publisher': lambda x: '/'.join(set(x))
}).reset_index()

# 9. Atualizar o DataFrame final
df = aggregated_df

# 10. Visualização: Top 10 livros mais avaliados
sns.set(style="whitegrid")

# Seleciona os 10 livros com mais avaliações
most_rated = df.sort_values('ratings_count', ascending=False).head(10).set_index('title')

# Tamanho da figura
plt.figure(figsize=(10, 6))

# Gráfico de barras com paleta suave
ax = sns.barplot(x=most_rated['ratings_count'], y=most_rated.index, palette="viridis")

# Título e rótulos
plt.title("Top 10 livros mais avaliados", fontsize=16)
plt.xlabel("Número de avaliações", fontsize=12)
plt.ylabel("Título do livro", fontsize=12)

# Adiciona os valores diretamente nas barras
for i, value in enumerate(most_rated['ratings_count']):
    ax.text(value + 5000, i, f"{value:,}", va='center', fontsize=10)

# Remove bordas desnecessárias
sns.despine(left=True, bottom=True)

# Ajusta layout e exibe
plt.tight_layout()
plt.show()