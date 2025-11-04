import streamlit as st 
import pandas as pd 
from sklearn.linear_model import LinearRegression
import joblib

# Título e descrição do aplicativo
st.title("Predição de Salário com Base na Experiência")
st.write("Este aplicativo prevê o salário com base nos anos de experiência usando um modelo de regressão linear simples.")

# Carregando o modelo

@st.cache_resource
def carregar_modelo():
    modelo = joblib.load('modelo.pkl')
    return modelo

modelo = carregar_modelo()

st.divider()

#Entrada do usuário
anos_experiencia = st.number_input("Insira os anos de experiência:", min_value=0.0, step=0.1)

# Previsão do salário
if anos_experiencia: 
    salario_previsto = modelo.predict([[anos_experiencia]])[0]
    st.write(f"O salário previsto para {anos_experiencia} anos de experiência é: R$ {salario_previsto:,.2f}")  
    st.balloons() 

