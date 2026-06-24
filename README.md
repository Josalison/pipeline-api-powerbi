# 📊 E-Commerce Data Pipeline: ETL de API para Power BI

Este repositório contém um projeto completo de **Pipeline de Dados (End-to-End)** que simula um cenário real de engenharia e análise de dados. O fluxo automatiza a extração de dados brutos de uma API de e-commerce, realiza o tratamento e a limpeza utilizando Python e disponibiliza uma base otimizada para um dashboard executivo no Power BI.

---

## 🛠️ Tecnologias e Ferramentas

* **Python 3.13** (Linguagem principal do pipeline)
* **Requests** (Consumo da API Rest e requisições HTTP)
* **Pandas** (Engenharia de dados, filtragem e manipulação de DataFrames)
* **Jupyter Notebook** (Ambiente de rascunho, testes de requisições e validação lógica)
* **Git & GitHub** (Controle de versão e boas práticas de repositório)
* **Power BI** (Visualização de dados e Data Storytelling)

---

## ⚙️ Arquitetura do Projeto (Processo ETL)

1. **Extraction (Extração):** O script `pipeline.py` faz uma requisição para a API pública da `FakeStoreAPI`, buscando o catálogo completo de produtos em formato JSON de forma dinâmica.
2. **Transformation (Transformação):** Utilizando a biblioteca **Pandas**, os dados brutos são convertidos em um DataFrame onde:
   * Isolamos apenas as colunas estratégicas para o negócio (`id`, `title`, `price`, `category`).
   * Aplicamos uma padronização de texto, convertendo todos os títulos dos produtos para letras maiúsculas.
3. **Load (Carga):** O dataset tratado é exportado automaticamente para um arquivo estruturado `dados_produtos.csv`.
4. **Business Intelligence (BI):** O Power BI consome o arquivo `.csv` de forma conectada. Sempre que o pipeline roda e atualiza a base, o dashboard reflete os novos dados com apenas um clique de atualização.

---

## 📊 Visualização dos Dados (Data Storytelling)

Para a construção do relatório no Power BI, foi aplicado o conceito de **design clean (menos é mais)**, removendo ruídos visuais, linhas de grade desnecessárias e poluções de eixos para focar puramente no que gera valor para a tomada de decisão (Faturamento acumulado por Categoria).

<img width="877" height="647" alt="image" src="https://github.com/user-attachments/assets/3138ff3c-24a1-4f2f-9e05-097d7294fe0c" />


---

## 🚀 Como Executar este Projeto Localmente

### 1. Clonar o Repositório
```bash
git clone [https://github.com/SEU_USUARIO/pipeline-api-powerbi.git](https://github.com/SEU_USUARIO/pipeline-api-powerbi.git)
cd pipeline-api-powerbi
