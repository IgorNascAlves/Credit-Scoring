import streamlit as st
import pandas as pd
from joblib import load
from utils import OneHotEncoder_Colunas

#Carregando dados
modelo = load('objetos/modelo.joblib')
lista_campos = load('objetos/lista_campos.joblib')
colunas_continuas_1 = load('objetos/colunas_continuas.joblib')
colunas_categoricas_nao_binarias = load('objetos/colunas_categoricas_nao_binarias.joblib')
colunas_categoricas_binarias = load('objetos/colunas_categoricas_binarias.joblib')

#Header
st.image('img/bytebank_logo.png', width=None)
st.write('# Simulador de Avaliação de crédito')

#Paginação
if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

col1, col2, col3, _ = st.beta_columns([0.1, 0.17, 0.1, 0.63])

if st.session_state.page < 2:
    col3.button(">", on_click=next_page)
else:
    col3.write("")  # this makes the empty column show up on mobile

if st.session_state.page > 0:
    col1.button("<", on_click=prev_page)
else:
    col1.write("")  # this makes the empty column show up on mobile

col2.write(f"Page {1+st.session_state.page} of {3}")


#Questionario

if st.session_state.page == 0:

    col1_form, col2_form = st.beta_columns(2)

    categoria_de_renda = col1_form.selectbox('Categoria', lista_campos['Categoria_de_renda'])

    ocupacao = col1_form.selectbox('Ocupação', lista_campos['Ocupacao'])

    tem_telefone_trabalho = col1_form.selectbox('Tem telefone do trabalho', ['Sim', 'Não'])

    resp_rendimento = col2_form.slider('Salario mensal', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=35000, step=500) * 12

    anos_empregado = col2_form.slider('Anos empregado', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=50, step=1)

    anos_empregado = col2_form.slider('Anos desempregado', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=50, step=1) * -1

if st.session_state.page == 1:

    col3_form, col4_form = st.beta_columns(2)

    grau_escolaridade = col3_form.selectbox('Grau_Escolaridade', lista_campos['Grau_Escolaridade'])

    estado_civil = col3_form.selectbox('Estado_Civil', lista_campos['Estado_Civil'])

    tem_carro = col3_form.selectbox('Tem_Carro', ['Sim', 'Não'])

    tem_telefone_fixo = col4_form.selectbox('Tem_telefone_fixo', ['Sim', 'Não'])

    tem_email = col4_form.selectbox('Tem_email', ['Sim', 'Não'])

    idade = col4_form.slider('Idade', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=100, step=1)

    lista_familia = ['Tem_Casa_Propria', 'Moradia', 'Tamanho_Familia', 'Qtd_Filhos']

if st.session_state.page == 2:

    col4_form, col5_form = st.beta_columns(2)

    moradia = col4_form.selectbox('Moradia', lista_campos['Moradia'])

    tem_casa_propria = col4_form.selectbox('Tem Casa Propria', ['Sim', 'Não'])

    tamanho_familia = col5_form.slider('Tamanho da familia', help='Podemos mover a barra usando as setas do teclado', min_value=1, max_value=20, step=1)

    qtd_filhos = col5_form.slider('Quantidade de filhos', help='Podemos mover a barra usando as setas do teclado', min_value=0, max_value=20, step=1)

    # Simulador
    if st.button('Simular'):
        st.success(f"Crédito Aprovado ! 🎈")

#     respostas = [resp_colunas_continuas_1+resp_colunas_categoricas_binarias+resp_lista_campos]
#     features = colunas_continuas_1+colunas_categoricas_binarias+colunas_categoricas_nao_binarias
#     df_novo_cliente = pd.DataFrame(data=respostas,columns=features)
#     resultado = modelo.predict(df_novo_cliente)

#     if resultado[0]: # Mau igual a verdadeiro
#         st.write('## Crédito não aprovado')
#     else:
#         st.write('## Crédito aprovado')

#     resp_colunas_continuas_1 = []
#     resp_colunas_categoricas_binarias = []
#     resp_lista_campos = []


# resp_colunas_continuas_1 = []
# for campo in colunas_continuas_1:
#     resp_colunas_continuas_1.append(col1.number_input(campo))

# resp_colunas_categoricas_binarias = []
# for campo in colunas_categoricas_binarias:
#     resp_colunas_categoricas_binarias.append(col2.selectbox(campo, ['Sim', 'Não']))

# resp_colunas_categoricas_binarias = pd.Series(resp_colunas_categoricas_binarias).replace({'Sim': 1, 'Não': 0}).to_list()

# resp_lista_campos = []
# for chave, valor in lista_campos.items():
#     resp_lista_campos.append(st.selectbox(chave, valor))

# print(colunas_continuas_1+colunas_categoricas_binarias+colunas_categoricas_nao_binarias)

# if st.button('Simular'):
#     respostas = [resp_colunas_continuas_1+resp_colunas_categoricas_binarias+resp_lista_campos]
#     features = colunas_continuas_1+colunas_categoricas_binarias+colunas_categoricas_nao_binarias
#     df_novo_cliente = pd.DataFrame(data=respostas,columns=features)
#     resultado = modelo.predict(df_novo_cliente)

#     if resultado[0]: # Mau igual a verdadeiro
#         st.write('## Crédito não aprovado')
#     else:
#         st.write('## Crédito aprovado')

#     resp_colunas_continuas_1 = []
#     resp_colunas_categoricas_binarias = []
#     resp_lista_campos = []
