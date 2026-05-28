import streamlit as st
import pandas as pd
import plotly.express as px
from urllib.parse import quote

df = pd.read_csv("deputados_2022.csv")
st.title("análise dos deputados 2022")

params = st.query_params

if "partido" in params:
    partido = params["partido"]
    st.subheader(f"deputados do {partido}")
    deputados = df[df["partido"] == partido].copy()
    deputados = deputados.sort_values("nome").reset_index(drop=True)
    deputados.index = deputados.index + 1
    deputados["id"] = deputados["id"].apply(
        lambda x: f'<a href="https://www.camara.leg.br/deputados/{x}" target="_blank">{x}</a>'
    )
    st.markdown(deputados.to_html(escape=False), unsafe_allow_html=True)
    st.markdown("[← voltar](./)")

elif "estado" in params:
    estado = params["estado"]
    st.subheader(f"deputados de {estado}")
    deputados = df[df["uf"] == estado].copy()
    deputados = deputados.sort_values("nome").reset_index(drop=True)
    deputados.index = deputados.index + 1
    deputados["id"] = deputados["id"].apply(
        lambda x: f'<a href="https://www.camara.leg.br/deputados/{x}" target="_blank">{x}</a>'
    )
    st.markdown(deputados.to_html(escape=False), unsafe_allow_html=True)
    st.markdown("[← voltar](./)")

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
        resultado.columns = ["partido", "quantidade"]

        fig = px.bar(
            resultado,
            x="quantidade",
            y="partido",
            orientation="h",
            text="quantidade",
            color="quantidade",
            color_continuous_scale="Blues",
            labels={"quantidade": "nº de candidatos", "partido": "partido"},
        )
        fig.update_layout(
            yaxis={"categoryorder": "total ascending"},
            coloraxis_showscale=False,
            height=600,
        )
        st.plotly_chart(fig, use_container_width=True)

    elif pergunta == "estados com mais candidatos":
        st.subheader("estados com mais candidatos")
        resultado = df["uf"].value_counts().reset_index()
        resultado.columns = ["estado", "quantidade"]

        fig = px.bar(
            resultado,
            x="quantidade",
            y="estado",
            orientation="h",
            text="quantidade",
            color="quantidade",
            color_continuous_scale="Greens",
            labels={"quantidade": "nº de candidatos", "estado": "estado"},
        )
        fig.update_layout(
            yaxis={"categoryorder": "total ascending"},
            coloraxis_showscale=False,
            height=600,
        )
        st.plotly_chart(fig, use_container_width=True)
