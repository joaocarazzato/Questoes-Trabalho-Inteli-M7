## Criação de um dashboard para visualização de dados de um modelo pré-treinado e realizar sua predição

O objetivo desse repositório é criar um dashboard cujo seja possível ver todos os dados a partir dos dados previstos pelo modelo diretamente do banco de dados.


https://github.com/joaocarazzato/Questoes-Trabalho-Inteli-M7/assets/99187756/a4b3fb99-2a97-49e1-b867-274f273b341f



### Descrição
A aplicação é utiliazda para prever chances altas/baixas de uma pessoa ter um ataque cardiaco a partir de dados de exames. O dataset base foi retirado do [Kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset), e o algoritmo utilizado foi o de regressão linear.

A aplicação é desenvolvida utilizando Flask, Streamlit e Pickle onde utilizamos o Flask para o servidor web, o Streamlit para os gráficos e o Pickle para salar e carregar o modelo pré-treinado.
Seu deploy é feito na núvem utilizando, no nosso caso, a AWS(vídeo a cima) utilizando o serviço da EC2 e todas as imagens podem ser encontradas em nosso Docker Hub [clicando aqui](https://hub.docker.com/repository/docker/joaocarazzato/modulo7/tags).


### Como executar a aplicação?
Primeiro, é necessário criar uma EC2 na AWS, após isso, precisamos clonar o repositório do github:
```
git clone https://github.com/joaocarazzato/Questoes-Trabalho-Inteli-M7.git
```
(Após isso, como você terá sua própria máquina, é necessário mudar o IP que direciona o streamlit para nossa máquina(EC2) localizado no arquivo dashboard.html, para isso, você pode usar o seguinte comando: ```sudo nano dashboard.html```)

Após isso, precisamos nos direcionar ao diretório de src e executar o docker-compose:
```
docker-compose up
```

E então, é só acessar o IP da sua EC2 com a porta 5000:
http://ipdamaquina:5000

Após isso, você deve ter a aplicação completa e funcionando.