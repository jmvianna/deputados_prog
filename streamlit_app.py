import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")

st.title("análise dos deputados 2022")

params = st.query_params

# página de partido
if "partido" in params:
    partido = params["partido"]

    st.subheader(f"deputados do {partido}")

    deputados = df[df["partido"] == partido].copy()
    deputados = deputados[["nome", "nome_civil", "partido", "uf", "sexo"]]

    deputados = deputados.sort_values("nome").reset_index(drop=True)

    deputados.columns = ["nome", "nome civil", "partido", "estado", "sexo"]
    deputados.index = deputados.index + 1

    st.dataframe(deputados, use_container_width=True)

    st.markdown("[← voltar](./)")

# página de estado
elif "estado" in params:
    estado = params["estado"]

    st.subheader(f"deputados de {estado}")

    deputados = df[df["uf"] == estado].copy()
    deputados = deputados[["nome", "nome_civil", "partido", "uf", "sexo"]]

    deputados = deputados.sort_values("nome").reset_index(drop=True)

    deputados.columns = ["nome", "nome civil", "partido", "estado", "sexo"]
    deputados.index = deputados.index + 1

    st.dataframe(deputados, use_container_width=True)

    st.markdown("[← voltar](./)")

# página principal
else:
    pergunta = st.selectbox(
        "escolha uma pergunta:",
        [
            "selecione uma opção",
            "partidos com mais candidatos",
            "estados com mais candidatos"
        ]
    )

    # gráfico de partidos
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

            html += f"""
<div style="margin-bottom: 18px;">
    <a href="?partido={partido}" style="font-weight: bold; font-size: 18px;">
        {partido}
    </a>
    <span style="margin-left: 8px;">{qtd} candidatos</span>

    <div style="background-color: #eeeeee; border-radius: 8px; height: 24px; margin-top: 6px;">
        <div style="
            background-color: #4a90e2;
            width: {largura}%;
            height: 24px;
            border-radius: 8px;">
        </div>
    </div>
</div>
"""

        st.markdown(html, unsafe_allow_html=True)

    # gráfico de estados
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

            html += f"""
<div style="margin-bottom: 18px;">
    <a href="?estado={estado}" style="font-weight: bold; font-size: 18px;">
        {estado}
    </a>
    <span style="margin-left: 8px;">{qtd} candidatos</span>

    <div style="background-color: #eeeeee; border-radius: 8px; height: 24px; margin-top: 6px;">
        <div style="
            background-color: #2ecc71;
            width: {largura}%;
            height: 24px;
            border-radius: 8px;">
        </div>
    </div>
</div>
"""

        st.markdown(html, unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)
