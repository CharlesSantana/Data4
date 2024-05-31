import streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
import csv

# Configurar o layout da página
st.set_page_config(layout="wide")


url = 'https://drive.google.com/file/d/1dpMSmpARIxtH-LX5u8UI_qqDV8bpMlSG/view?usp=sharing'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv(path)

# Exibir o DataFrame
#st.write(df)

# Converter a coluna "Date" para o formato de data
df["Date"] = pd.to_datetime(df["order_approved_at"])
df = df.sort_values("Date")

# Criar uma nova coluna "Month" que contém o ano e o mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Criar uma seleção de meses na barra lateral do dashboard
month = st.sidebar.selectbox("Selecione o Mês", df["Month"].unique())

# Filtrar os dados com base no mês selecionado
df_filtered = df[df["Month"] == month]


# Exibir o DataFrame filtrado
#st.write(df_filtered)

cabe=sum(df_filtered.payment_value)

st.write(cabe)
col1, col2 = st.columns(2) # Primeira linha com duas colunas
col3, col4, col5 = st.columns(3) # Segunda linha com três colunas

# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="payment_value", color="customer_state", title="Faturamento por dia")

# Exibir o gráfico na primeira coluna
col1.plotly_chart(fig_date, use_container_width=True)

# Criar o gráfico de faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Date", y="product_category_name", 
                  color="customer_state", title="Faturamento por tipo de produto",
                  orientation="h")

# Exibir o gráfico na segunda coluna
col2.plotly_chart(fig_prod, use_container_width=True)

# Calcular o faturamento total por cidade
city_total = df_filtered.groupby("customer_city")[["payment_value"]].sum().reset_index()

# Criar o gráfico de barras para exibir o faturamento por cidade
fig_city = px.bar(city_total, x="payment_value", y="customer_city",
title="Faturamento por cidade")

# Exibir o gráfico na terceira coluna
col3.plotly_chart(fig_city, use_container_width=True)







