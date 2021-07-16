import streamlit as st
import pandas as pd
from joblib import load
from utils import OneHotEncoder_Colunas

import streamlit.components.v1 as components

#Cor de fundo do listbox
st.markdown('<style>div[role="listbox"] ul{background-color: #eee1f79e};</style>', unsafe_allow_html=True)


def carregar_dados():    
    #Carregando dados
    modelo = load('objetos/modelo.joblib')
    colunas_continuas_1 = load('objetos/colunas_continuas.joblib')
    colunas_categoricas_nao_binarias = load('objetos/colunas_categoricas_nao_binarias.joblib')
    colunas_categoricas_binarias = load('objetos/colunas_categoricas_binarias.joblib')

    return modelo, colunas_continuas_1, colunas_categoricas_binarias, colunas_categoricas_nao_binarias

def avaliar(dict_respostas):
    modelo, colunas_continuas_1, colunas_categoricas_binarias, colunas_categoricas_nao_binarias = carregar_dados()
    features = colunas_continuas_1+colunas_categoricas_binarias+colunas_categoricas_nao_binarias
    respostas = []

    for coluna in features:
        respostas.append(dict_respostas[coluna])

    df_novo_cliente = pd.DataFrame(data=respostas,columns=features)
    resultado = modelo.predict(df_novo_cliente)

#Header
st.image('img/bytebank_logo.png', width=None)
st.write('# Simulador de Avaliação de crédito')

my_expander_1 = st.beta_expander("Trabalho")

my_expander_2 = st.beta_expander("Pessoal")

my_expander_3 = st.beta_expander("Familia")

#Questionario
dict_respostas = {}
lista_campos = load('objetos/lista_campos.joblib')


with my_expander_1:

    col1_form, col2_form = st.beta_columns(2)

    dict_respostas['Categoria'] = col1_form.selectbox('Categoria', lista_campos['Categoria_de_renda'])

    dict_respostas['Ocupacao'] = col1_form.selectbox('Ocupação', lista_campos['Ocupacao'])

    dict_respostas['Tem_telefone_trabalho'] = 1 if col1_form.selectbox('Tem telefone do trabalho', ['Sim', 'Não']) == 'Sim' else 0

    dict_respostas['Rendimento_Anual'] = col2_form.slider('Salario mensal', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=35000, step=500) * 12

    dict_respostas['Anos_empregado'] = col2_form.slider('Anos empregado', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=50, step=1)

    dict_respostas['Anos_desempregado'] = col2_form.slider('Anos desempregado', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=50, step=1) * -1

with my_expander_2:

    col3_form, col4_form = st.beta_columns(2)

    dict_respostas['Grau_Escolaridade'] = col3_form.selectbox('Grau Escolaridade', lista_campos['Grau_Escolaridade'])

    dict_respostas['Estado_Civil'] = col3_form.selectbox('Estado Civil', lista_campos['Estado_Civil'])

    dict_respostas['Tem_Carro'] = 1 if col3_form.selectbox('Tem Carro', ['Sim', 'Não']) == 'Sim' else 0

    dict_respostas['Tem_telefone_fixo'] = 1 if col4_form.selectbox('Tem telefone fixo', ['Sim', 'Não']) == 'Sim' else 0

    dict_respostas['Tem_email'] = 1 if col4_form.selectbox('Tem email', ['Sim', 'Não']) == 'Sim' else 0

    dict_respostas['Idade'] = col4_form.slider('Idade', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=100, step=1)

with my_expander_3:

    col4_form, col5_form = st.beta_columns(2)

    dict_respostas['Moradia'] = col4_form.selectbox('Moradia', lista_campos['Moradia'])

    dict_respostas['Tem_Casa_Propria'] = 1 if col4_form.selectbox('Tem Casa Propria', ['Sim', 'Não']) == 'Sim' else 0

    dict_respostas['Tamanho_Familia'] = col5_form.slider('Tamanho da familia', help='Podemos mover a barra usando as setas do teclado', min_value=1, max_value=20, step=1)

    dict_respostas['Qtd_Filhos'] = col5_form.slider('Quantidade de filhos', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=20, step=1)

# Simulador
# if st.button('Crédito Recusado'):        
#     st.error('Crédito Recusado :no_entry:')

if st.button('Avaliar crédito'):
    st.success("Crédito Aprovado :confetti_ball:")
    st.balloons()