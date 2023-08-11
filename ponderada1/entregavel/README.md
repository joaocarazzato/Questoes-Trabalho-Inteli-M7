# Currículo Dockerizado
Nesse repositório é ensinado a como baixar e executar uma imagem de Docker baseada em Python, criando uma aplicação em Flask em conjunto da utilização de HTML e CSS.

## Construção e execução
Temos duas formas de iniciar a execução do nosso Container, sendo ela baixando diretamente a imagem ou criando-a a partir do nosso Dockerfile em junção com os conteúdos obtidos diante desse repositório do GitHub.

Baixando a imagem já pronta a fim de economizar tempo, podemos localizá-la em nosso [Docker Hub](https://hub.docker.com/repository/docker/joaocarazzato/modulo7/tags?page=1&ordering=last_updated), e baixá-la executando o seguinte comando:
```
docker pull joaocarazzato/modulo7:1.0
```

A partir disso, já teremos nossa imagem com os requisitos necessários baixados, então, precisamos criar um container a partir da nossa imagem:
```
docker run -p 80:3000 joaocarazzato/modulo7:1.0
```
Com esse comando, criamos um container docker a partir da nossa imagem, mapeando a porta 80 de nosso computador com a porta 3000 do container Docker.

Após o fim da sua criação, você deve receber uma mensagem parecida a esta:

```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:3000
 * Running on http://xxx.xx.x.x:3000
Press CTRL+C to quit
```

Caso isso apareça, você poderá acessar o currículo a partir do seu [localhost](http://localhost:80), na url do seu navegador utilizando a porta 80 que mapeamos!
```
http://localhost:80
```