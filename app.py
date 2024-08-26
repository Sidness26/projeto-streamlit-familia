import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meu sistema streamlit",
    page_icon="💫",
    layout="centered"
)

lateral=st.sidebar
data=lateral.date_input("Selecione a data")
cidade=lateral.selectbox("Selecione a cidade",["Belo Horizonte","Rio de janeiro","Amapá"])


@st.cache_data
def carregar_dados():
    dados=pd.read_csv("acidentes.csv")
    return dados

dados=carregar_dados()
st.session_state["dados"]=dados
st.session_state["data"]=data
st.session_state["cidade"]=cidade



st.title("dados")
col1,col2,col3=st.columns([0.50,0.25,0.25])

tabela=col1.dataframe(dados)

municipios=dados["municipio"].value_counts()
col2.bar_chart(municipios)


st.subheader("cidade")
st.write(f"A cidade selecionada foi {cidade}")

lateral.video("sid.mp4")
col3.image("imagem.jpg")