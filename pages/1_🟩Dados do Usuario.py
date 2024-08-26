import streamlit as st

st.title("Dados do Usuário")
st.dataframe(st.session_state["dados"])