import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.title("análise dos Deputados 2022")

params = st.query_params

if "partido" in params:
    partido = params["partido"]

    st.subheader(f"deputados do {partido}")

    deputados = df[df["partido"] == partido]["nome"].sort_values()

    for deputado in deputados:
        st.write(f"- {deputado}")

    st.markdown("[← voltar para partidos](./)")

else:
    pergunta = st.selectbox(
        "escolha uma pergunta:",
        [
            "selecione uma opção",
            "partidos com mais candidatos",
            "estados com mais candidatos"
        ]
    )

    if pergunta == "partidos com mais candidatos":
        st.subheader("partidos com mais candidatos")

        resultado = df["partido"].value_counts().reset_index()
        resultado.columns = ["partido", "quantidade de candidatos"]
        resultado.index = resultado.index + 1

        for _, linha in resultado.iterrows():
            partido = linha["partido"]
            qtd = linha["quantidade de candidatos"]

            st.markdown(f"[{partido}](?partido={partido}) — {qtd} candidatos")

    elif pergunta == "estados com mais candidatos":
        st.subheader("estados com mais candidatos")

        resultado = df["uf"].value_counts().reset_index()
        resultado.columns = ["estado", "quantidade de candidatos"]
        resultado.index = resultado.index + 1

        st.dataframe(resultado)
