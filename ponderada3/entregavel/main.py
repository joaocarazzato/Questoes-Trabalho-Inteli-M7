# Importando bibliotecas necessárias
import pandas as pd
import pickle
from fastapi import FastAPI
import uvicorn
import json

# Criando o app com o framework do fastapi
app = FastAPI()

# Carregando/lendo o modelo criado usando o pickle
pickled_model = pickle.load(open('model.pkl', 'rb'))


# Criando a rota de post do modelo e passando seus parâmetros necessários
@app.post("/predict")
def predict(age: int, sex: int, 
            cp: int, trtbps: int, 
            chol: int, fbs: int, 
            restecg: int, thalachh: int, 
            exng: int, oldpeak: float, 
            slp: int, caa: int, thall: int):
    # Atribuindo os dados a um dicionário
    data = {'age': age, 'sex': sex, 
            'cp': cp, 'trtbps': trtbps, 
            'chol': chol, 'fbs': fbs, 
            'restecg': restecg, 'thalachh': thalachh, 
            'exng': exng, 'oldpeak': oldpeak,
            'slp': slp, 'caa': caa, 'thall': thall
            }
    # Transformando em dataframe usando o pandas
    data_df = pd.DataFrame([data])
    # Predizendo os dados a partir do modelo
    predictions = pickled_model.predict(data_df)
    # Retornando o primeiro dado retornado do modelo, no caso, a resposta de 0 ou 1.
    return json.dumps(predictions[0], default=str)

# Executando a aplicação
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
