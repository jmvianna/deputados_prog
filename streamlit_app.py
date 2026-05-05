import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
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

        max_qtd = resultado["quantidade"].max()

        html = ""

        for _, linha in resultado.iterrows():
            partido = linha["partido"]
            qtd = linha["quantidade"]
            largura = (qtd / max_qtd) * 100
            link = quote(str(partido))

            html += f"""
            <div style="margin-bottom: 20px; font-family: sans-serif;">
                <a href="?partido={link}" target="_parent" style="font-weight: bold; font-size: 18px;">
                    {partido}
                </a>
                <span style="margin-left: 8px; font-size: 16px;">{qtd} candidatos</span>

                <div style="background-color: #eeeeee; border-radius: 8px; height: 24px; margin-top: 6px;">
                    <div style="background-color: #4a90e2; width: {largura}%; height: 24px; border-radius: 8px;"></div>
                </div>
            </div>
            """

        components.html(html, height=900, scrolling=True)

    elif pergunta == "estados com mais candidatos":
        st.subheader("estados com mais candidatos")

        resultado = df["uf"].value_counts().reset_index()
        resultado.columns = ["estado", "quantidade"]

        max_qtd = resultado["quantidade"].max()

        html = ""

        for _, linha in resultado.iterrows():
            estado = linha["estado"]
            qtd = linha["quantidade"]
            largura = (qtd / max_qtd) * 100
            link = quote(str(estado))

            html += f"""
            <div style="margin-bottom: 20px; font-family: sans-serif;">
                <a href="?estado={link}" target="_parent" style="font-weight: bold; font-size: 18px;">
                    {estado}
                </a>
                <span style="margin-left: 8px; font-size: 16px;">{qtd} candidatos</span>

                <div style="background-color: #eeeeee; border-radius: 8px; height: 24px; margin-top: 6px;">
                    <div style="background-color: #2ecc71; width: {largura}%; height: 24px; border-radius: 8px;"></div>
                </div>
            </div>
            """

        components.html(html, height=900, scrolling=True)
