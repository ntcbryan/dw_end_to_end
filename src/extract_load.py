#import 
import yfinance as yf
import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv #para pegar as variaveis de ambiente
import os 

load_dotenv()



commodities = ['CL=F','GC=F','SI=F ']

#trazendo as variaveis de ambientes

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')


#url de requisicao (uma string que vai utilizar todas as variaveis)
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'


engine = create_engine(DATABASE_URL)

def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval = intervalo)[['Close']] #ele transforma em um df
    dados['simbolo'] = simbolo
    return dados

def buscar_todos_dados_commodities(commodities):
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados)

def salvar_no_postgres(df):
    #função para salvar uma tabela no banco (e vamos usar o sqlachemy para fazer a requisicao)
    #geralmente no lugar de utilizar funções, construimos o schema em um DF, porem aqui vamos pegar só o dado bruno
    #e fazer o tratamento no DBT
    df.to_sql('commodities', engine, if_exists ='append', index=True, index_label='Date')


if __name__ == "__main__":
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    print(dados_concatenados)
    salvar_no_postgres(dados_concatenados)
    


# agora precisa salvar no bd (vou salvar no postgres no render)

