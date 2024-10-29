# rss_parser.py

import feedparser
import pandas as pd
import os

# URL do feed RSS
url = 'https://scon.stj.jus.br/SCON/PesquisaProntaFeed'

# Faz o parsing do feed
feed = feedparser.parse(url)

# Lista para armazenar os dados dos itens do feed
data = []

# Itera pelos itens do feed e armazena as informações em 'data'
for entry in feed.entries:
    item = {
        'Título': entry.title,
        'Data': entry.published if 'published' in entry else 'Sem data',
        'Link': entry.link,
        'Descrição': entry.summary if 'summary' in entry else 'Sem descrição'
    }
    data.append(item)

# Cria um DataFrame a partir dos dados coletados
df = pd.DataFrame(data)

# Cria o diretório data se ele não existir
os.makedirs('data', exist_ok=True)

# Salva o DataFrame como CSV
df.to_csv('data/output.csv', index=False)

print("Arquivo CSV gerado com sucesso em data/output.csv")