import streamlit as st

cidade=st.session_state["cidade"]

st.title("Dados do Sistema")
st.text(st.session_state["data"])
st.text(cidade)