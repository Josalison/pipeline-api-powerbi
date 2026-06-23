import requests
import pandas as pd
def buscar_todos_produtos():
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    return response.json()

def criar_tabela():
    tabela_de_produto = buscar_todos_produtos()
    df = pd.DataFrame(tabela_de_produto)
    df_tratado = df[["id", "title", "price", "category"]].copy()
    df_tratado["title"] = df_tratado["title"].str.upper()
    return df_tratado

def criando_arq_csv(df_final):
    df_final.to_csv("dados_produtos.csv", index=False)

print("🚀 Automação concluída com sucesso! O arquivo 'dados_produtos.csv' foi atualizado.")

criando_minha_tabela = criar_tabela()
criando_arq_csv(criando_minha_tabela)