import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.title("análise dos Deputados 2022")

params = st.query_params

if "partido" in params:
    partido = params["partido"]

    st.subheader(f"deputados do {partido}")

    deputados = df[df["partido"] == partido].copy()

    deputados = deputados[["nome", "nome_civil", "partido", "uf", "sexo"]]
    deputados.columns = ["nome", "nome civil", "partido", "estado", "sexo"]

    deputados = deputados.sort_values("nome").reset_index(drop=True)
    deputados.index = deputados.index + 1

    st.dataframe(deputados, use_container_width=True)

    st.markdown("[← voltar](./)")

else:
    pergunta = st.selectbox(
        "escolha uma opção:",
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

        tabela_html = resultado.to_html(escape=False)

        for partido in resultado["partido"]:
            tabela_html = tabela_html.replace(
                f"<td>{partido}</td>",
                f'<td><a href="?partido={partido}">{partido}</a></td>'
            )

        st.markdown(tabela_html, unsafe_allow_html=True)

    elif pergunta == "estados com mais candidatos":
        st.subheader("estados com mais candidatos")

        resultado = df["uf"].value_counts().reset_index()
        resultado.columns = ["estado", "quantidade de candidatos"]
        resultado.index = resultado.index + 1

        st.dataframe(resultado, use_container_width=True)
