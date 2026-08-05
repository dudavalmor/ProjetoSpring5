# ProjetoSpring5 🚗📊

Aplicativo web desenvolvido durante o curso de **Análise de Dados da TripleTen** utilizando **Python e Streamlit** para realizar uma análise exploratória de anúncios de veículos.

O objetivo do projeto é explorar um conjunto de dados reais de veículos, identificar padrões e tendências e apresentar os resultados através de visualizações interativas, facilitando a interpretação das informações.

A aplicação permite analisar características dos veículos anunciados, como preço, quilometragem e categorias, utilizando gráficos desenvolvidos com Plotly Express.

---

## Aplicação Online

Acesse o dashboard:

🔗 https://projetospring5.onrender.com

---

## Funcionalidades

O aplicativo web oferece:

- Visualização da distribuição dos preços dos veículos;
- Análise da distribuição da quilometragem (`odometer`);
- Gráfico de dispersão entre preço e quilometragem;
- Visualização da quantidade de anúncios por tipo de veículo;
- Análise do preço médio dos veículos de acordo com sua condição;
- Gráficos interativos desenvolvidos com Plotly Express;
- Interface criada utilizando Streamlit.

---

## Análise Exploratória de Dados (EDA)

O projeto também possui um notebook de análise exploratória:

📓 `notebooks/EDA.ipynb`

Durante a análise foram realizados:

- Inspeção inicial do conjunto de dados;
- Análise da estrutura e tipos das variáveis;
- Investigação de valores ausentes;
- Estudo da distribuição dos preços;
- Análise da quilometragem dos veículos;
- Avaliação da relação entre preço e odômetro;
- Identificação de padrões e possíveis valores extremos.

---

## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit
- Jupyter Notebook
- Git/GitHub
- Render

---

## Estrutura do projeto

```
ProjetoSpring5/
│
├── app.py                    # Aplicação web desenvolvida com Streamlit
│
├── vehicles.csv              # Conjunto de dados utilizado no projeto
│
├── notebooks/
│   └── EDA.ipynb             # Notebook com análise exploratória dos dados
│
├── requirements.txt          # Dependências do projeto
│
└── streamlit/
    └── config.toml           # Configuração do Streamlit para deploy
```

---

## Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/dudavalmor/ProjetoSpring5
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o aplicativo Streamlit

```bash
streamlit run app.py
```

Após executar o comando, o aplicativo estará disponível no navegador.

---

## Dataset

O projeto utiliza um conjunto de dados de anúncios de veículos contendo informações como:

- Preço;
- Ano do modelo;
- Quilometragem;
- Tipo de veículo;
- Condição;
- Características do veículo.

---

## Objetivo do projeto

Este projeto teve como objetivo aplicar na prática conceitos de **Análise de Dados**, passando pelas etapas de:

- Exploração e entendimento dos dados;
- Criação de visualizações;
- Desenvolvimento de uma aplicação interativa;
- Publicação de um dashboard online.

---

Projeto desenvolvido como parte da formação em **Análise de Dados da TripleTen**. 🚀
