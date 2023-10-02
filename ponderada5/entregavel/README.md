# Resenha do Artigo:
## "Machine learning for internet of things data analysis: a survey"

O artigo "Machine learning for internet of things data analysis: a survey" explora o uso de técnicas de aprendizado de máquina na análise de dados gerados pela Internet das Coisas (IoT). Com o rápido crescimento de dispositivos conectados à internet, espera-se que até 2020 haja entre 25 e 50 bilhões de dispositivos IoT em uso. Esses dispositivos geram grandes volumes de dados, caracterizados por sua velocidade, dependência de tempo e localização, várias modalidades e variação na qualidade dos dados.

Em resposta aos desafios apresentados pelos grandes volumes de dados, surge o conceito de "smart data", que se refere à transformação de dados brutos em dados inteligentes por meio do uso de semântica. Smart data visa aumentar a produtividade, eficiência e eficácia ao lidar com os desafios de volume, velocidade, variedade e veracidade dos grandes dados, fornecendo informações acionáveis e melhorando a tomada de decisões.

O artigo se concentra principalmente no contexto das "cidades inteligentes" (smart cities) como um caso de uso da IoT. Ele apresenta uma taxonomia de algoritmos de aprendizado de máquina que explicam como diferentes técnicas são aplicadas aos dados para extrair informações de nível superior. Além disso, o artigo discute o potencial e os desafios do uso de aprendizado de máquina na análise de dados da IoT.

### Autor: 
#### João Pedro Gonçalves Carazzato | Inteli - Instituto de Tecnologia e Liderança

## Resenha Literaria
### Smart Cities

As cidades inteligentes têm como objetivo melhorar serviços como gerenciamento de tráfego, gestão de água e consumo de energia, bem como a qualidade de vida dos cidadãos. Elas buscam reduzir despesas em áreas como saúde pública, segurança, transporte e gestão de recursos, contribuindo para o desenvolvimento econômico.

O artigo descreve quatro casos de uso específicos para cidades inteligentes:

* Smart Energy: Envolve a redução do consumo de energia por meio de medidas operacionais e energéticas, como o uso de energias renováveis e a implementação de redes elétricas inteligentes (smart grids).

* Smart Mobility: Lida com a melhoria da mobilidade urbana, incluindo a utilização de veículos autônomos, controle de tráfego e sistemas de transporte público inteligentes.

* Smart Citizens: Aborda áreas como monitoramento ambiental, segurança pública e saúde social, visando melhorar a qualidade de vida dos cidadãos.

* Urban Planning: Envolve a tomada de decisões de longo prazo relacionadas à infraestrutura e ao planejamento urbano, usando dados coletados de diversas fontes para prever e resolver problemas futuros.

### Taxonomia e algoritmos de ML

Além do citado anteriormente, O artigo também aborda a taxonomia de algoritmos de aprendizado de máquina, discutindo os principais conceitos e algoritmos frequentemente aplicados na análise de dados inteligentes (smart data). São mencionadas três categorias principais de aprendizado: supervisionado, não supervisionado e por reforço, com foco nas duas primeiras, que são amplamente aplicadas na análise de dados da IoT.

Diante disso, relacionando com nosso projeto realizado nesse módulo, de um modelo de manutenção preditiva, utilizamos e testamos alguns algoritmos citados no artigo:

* **Naive Bayes**: Escolhemos esse modelo, pelo mesmo motivo pelo qual foi dito no artigo: "necessita de um pequeno número de data points para ser treinado e é facilmente escalável e rápido"

* **Support Vector Machine(SVM)**: Por estarmos trabalhando de uma forma supervisionada, e termos dados enormes, também testamos o SVM. O SVM costuma trabalhar com grandes quantidades de dados para difíceis propósitos, sendo muito utilizado em casos reais, onde optamos por testá-lo também.

* **Linear Regression**: Esse é um dos modelos mais simples de se testar, mas também um dos mais rápidos, e funcionou de forma significativa em nosso projeto.

## Conclusão

Diante do artigo lido, podemos concluir que seu principal objetivo é explorar o papel essencial do aprendizado de máquina na análise de dados gerados pelo Internet of Things (IoT). Onde podemos ressaltar pontos principais como o Crescimento do IoT em torno de todo o mundo, os desafios da análise de dados, as aplicações em cidades inteligentes e até mesmo os desafios e as oportunidades.

#### Pontos positivos:
**1. Visão Abrangente**: O artigo abordou os conceitos essenciais e forneceu uma taxonomia de algoritmos relevantes.

**2. Aplicações Práticas**: O artigo apresenta exemplos e casos de uso do que é utilizado nas áreas citadas.


#### Pontos negativos:

**1. Data de publicação**: Apesar de apresentar uma visão sólida, o artigo foi públicado em 2018, e muitas técnologias novas surgiram e evoluiram desde a época.

**3. Complexidade Técnica**: O artigo utiliza muitos termos técnicos, onde uma pessoa com um conhecimento menor da área pode ter dificuldade em entender seu propósito, funcionalidade ou até mesmo o assunto do artigo como um todo.
