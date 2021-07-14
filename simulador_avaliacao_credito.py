import streamlit as st
import pandas as pd
from joblib import load
from utils import OneHotEncoder_Colunas

modelo = load('objetos/modelo.joblib')
lista_campos = load('objetos/lista_campos.joblib')
colunas_continuas_1 = load('objetos/colunas_continuas_1.joblib')
colunas_categoricas_nao_binarias = load('objetos/colunas_categoricas_nao_binarias.joblib')
colunas_categoricas_binarias = load('objetos/colunas_categoricas_binarias.joblib')

st.write('# Simulador de Avaliação de crédito')

col1, col2 = st.beta_columns(2)

resp_colunas_continuas_1 = []
for campo in colunas_continuas_1:
    resp_colunas_continuas_1.append(col1.number_input(campo))

resp_colunas_categoricas_binarias = []
for campo in colunas_categoricas_binarias:
    resp_colunas_categoricas_binarias.append(col2.selectbox(campo, ['Sim', 'Não']))

resp_colunas_categoricas_binarias = pd.Series(resp_colunas_categoricas_binarias).replace({'Sim': 1, 'Não': 0}).to_list()

resp_lista_campos = []
for chave, valor in lista_campos.items():
    resp_lista_campos.append(st.selectbox(chave, valor))

if st.button('Simular'):
    respostas = [resp_colunas_continuas_1+resp_colunas_categoricas_binarias+resp_lista_campos]
    features = colunas_continuas_1+colunas_categoricas_binarias+colunas_categoricas_nao_binarias
    df_novo_cliente = pd.DataFrame(data=respostas,columns=features)
    resultado = modelo.predict(df_novo_cliente)

    if resultado[0]:
        st.write('## Crédito aprovado')
    else:
        st.write('## Crédito não aprovado')

    resp_colunas_continuas_1 = []
    resp_colunas_categoricas_binarias = []
    resp_lista_campos = []