# syntax=docker/dockerfile:1

FROM python:3.9

# Dir de trabalho
WORKDIR /code

# Copiando os requerimentos que passamos
COPY ./requirements.txt /code/requirements.txt

# Rodando uma linha de CMD para instalar os requerimentos
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copiar o nosso app para o work dir
COPY . .

# Passando os comandos para o CMD e rodando
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0",  "--port=3000"]
