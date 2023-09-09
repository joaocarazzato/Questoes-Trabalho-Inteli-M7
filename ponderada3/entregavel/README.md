## Criação de um modelo de machine learning com predições feitas através de uma API

O objetivo desse repositório, é criar uma API capaz de realizar predições em um modelo pré-treinado utilizando FastAPI.

O modelo foi criado utilizando como base o dataset ["Heart Attack Analysis & Prediction Dataset"](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset), e utilizando o algoritmo de regressão logísitca(utilizada para criar modelos categóricos) após uma análise de diversos modelos utilizando o pycaret como base, onde o único pré-processamento foi a normalização das colunas numéricas. 

## API - Como funciona?

A API funciona utilizando os frameworks FastAPI e Uvicorn em junção a fim de criar um servidor web. A rota utilizada para prever uma nova linha de dados utilizando um modelo pré-treinado, pede para que o usuário passe os parâmetros necessários de uma nova linha para que então, seja possível utilizar o modelo pré-treinado carregando-o com a biblioteca do pickle. Então, o modelo retorna 1 ou 0 a partir da sua percepção do que está correto.

## Como executar?
A aplicação está dockerizada, então, é possível baixar diretamente do Docker Hub [disponibilizada aqui](https://hub.docker.com/r/joaocarazzato/modulo7/tags), usando o seguinte comando:
```
docker pull joaocarazzato/modulo7:ponderada3
```

Ou, caso queira utilizar o dockerfile, se direcione ao diretório que o Dockerfile foi baixado e execute o seguinte comando:
```
docker build . -t [NOME DA IMAGEM]
```

Após isso, é preciso executá-la mapeando suas portas, utilizando o seguinte comando:
```
docker run -p 8000:8000 joaocarazzato/modulo7:ponderada3
```

Ou caso tenha usado o dockerfile:

```
docker run -p 8000:8000 [NOME DA IMAGEM]
```

A partir disso, a aplicação já estará funcionando, e você deverá se direcionar a [http://localhost:8000/docs](http://localhost:8000/docs), e então, com o docs criado pelo Swagger, você poderá realizar predições diretamente da rota da API preenchendo os campos necessários. Caso queira testar, recomendo utilizar os dados disponibilizados pelo dataset a fim de facilitar seu uso. Novamente, o dataset pode ser encontrado [aqui](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset).