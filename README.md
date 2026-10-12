# Segmentação de Clientes com Machine Learning Não Supervisionado

## Sobre o projeto

Este projeto utiliza técnicas de Machine Learning não supervisionado para segmentar clientes de uma loja com base em suas características e comportamento de compra.

O algoritmo K-Means identifica grupos de clientes com padrões semelhantes, permitindo explorar perfis de consumo e apoiar a análise de dados para tomada de decisões.

## Objetivos

- Aplicar o algoritmo K-Means para agrupar clientes.
- Preparar e padronizar variáveis numéricas.
- Analisar os perfis identificados pelo modelo.
- Criar visualizações para interpretar os agrupamentos.
- Exportar os resultados para análise posterior.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Scikit-learn
- CSV

## Estrutura do projeto

```text
machine_learning_nao_supervisionado/
├── clientes.csv
├── segmentacao.py
├── clientes_segmentados.csv
├── segmentacao_clientes.png
└── README.md
```

## Metodologia

### 1. Carregamento dos dados

Os dados fictícios dos clientes são importados de um arquivo CSV.

### 2. Seleção das variáveis

São utilizadas as seguintes características:

- Idade do cliente.
- Renda mensal.
- Quantidade de compras mensais.

### 3. Padronização

A classe `StandardScaler`, do Scikit-learn, padroniza as variáveis numéricas para que diferenças de escala não distorçam excessivamente o cálculo das distâncias.

### 4. Aplicação do K-Means

O modelo K-Means é configurado inicialmente para identificar três grupos de clientes.

### 5. Análise dos resultados

Os agrupamentos são analisados por meio das médias das variáveis selecionadas e de um gráfico que relaciona renda mensal e quantidade de compras.

### 6. Exportação

O projeto gera um arquivo CSV com os grupos atribuídos aos clientes e uma imagem com a visualização dos resultados.

## Como executar

### Pré-requisitos

- Python 3 instalado.
- Bibliotecas Pandas, Matplotlib e Scikit-learn.

### Instalação das dependências

```bash
python3 -m pip install pandas matplotlib scikit-learn
```

### Execução

No terminal, acesse a pasta do projeto e execute:

```bash
python3 segmentacao.py
```

## Resultados esperados

Após a execução, serão gerados:

- `clientes_segmentados.csv`: dados dos clientes com o grupo atribuído pelo modelo.
- `segmentacao_clientes.png`: gráfico de dispersão dos grupos identificados.

Os grupos representam padrões encontrados pelo algoritmo nos dados utilizados. Sua interpretação depende das características médias de cada agrupamento.

## Aprendizados

Este projeto permite praticar conceitos fundamentais de Ciência de Dados e Machine Learning:

- Preparação e exploração de dados.
- Padronização de variáveis.
- Aprendizado não supervisionado.
- Clusterização com K-Means.
- Visualização e interpretação de resultados.
- Exportação de dados para análise.

## Limitações

A base utilizada é pequena e fictícia, criada exclusivamente para fins educacionais. O número de grupos foi definido inicialmente como três e não representa necessariamente a melhor segmentação possível.

Em aplicações reais, seria importante avaliar diferentes quantidades de grupos, utilizar métricas como o *Silhouette Score* e validar se os agrupamentos fazem sentido para o negócio.

## Autor

Projeto desenvolvido para fins de estudo e construção de portfólio em Ciência de Dados e Machine Learning.
