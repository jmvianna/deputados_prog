import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.title("Análise dos Deputados 2022")

pergunta = st.selectbox(
    "escolha uma pergunta:",
    [
        "estados com mais candidatos",
        "partidos com mais candidatos"
    ]
)

if pergunta == "estados com mais candidatos":
    st.subheader("estados com mais candidatos")

    resultado = df["uf"].value_counts().reset_index()
    resultado.columns = ["estado", "quantidade de candidatos"]

    st.dataframe(resultado)

elif pergunta == "partidos com mais candidatos":
    st.subheader("partidos com mais candidatos")

    resultado = df["partido"].value_counts().reset_index()
    resultado.columns = ["partido", "quantidade de candidatos"]

    st.dataframe(resultado)
