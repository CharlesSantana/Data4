import streamlit
import streamlit as st
import pandas as pd
import plotly.express as px
import csv

# Configurar o layout da página
st.set_page_config(layout="wide")

#https://github.com/jkanner/streamlit-dataview/blob/master/app.py


# Carregar os dados do arquivo "/home/charles/dados/datasets/dataset_olist.csv"
df = pd.read_csv("https://raw.githubusercontent.com/CharlesSantana/datasets/main/olist.csv")
# Exibir o DataFrame
3st.write(df)

#=================combodata

# Converter a coluna "Date" para o formato de data
df["Date"] = pd.to_datetime(df["order_approved_at"])
df = df.sort_values("Date")
# Criar uma nova coluna "Month" que contém o ano e o mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
# Criar uma seleção de meses na barra lateral do dashboard
month = st.sidebar.selectbox("Selecione o Mês", df["Month"].unique(), index=None, placeholder="Select contact method...")



#combo categoria - product_category_name
df["Catg"] =(df["product_category_name"])
df = df.sort_values("Catg")
df["Categoria"] = df["Catg"]
categoria = st.sidebar.selectbox("Selecione o Categoria", df["Categoria"].unique(), index=None, placeholder="Select contact method...")




# Filtrar os dados com base no mês selecionado
df_filtered = df[df["Month"] == month]
df_filtered1 = df[df["Categoria"] == categoria]
df_fil=(df_filtered, df_filtered1)
#==================botao para chamar resultado
botao01= st.sidebar.button ('Total Vendas Mes')
cabe=sum(df_filtered.payment_value)
if botao01:
    st.info(cabe)
   


# Exibir o DataFrame filtrado
#st.write(df_filtered)

st.title("DashBoard Olist")



#st.write(df)
col1, col2, col3 = st.columns(3) # Primeira linha com duas colunas
col4,col5 = st.columns(2) # Primeira linha com duas colunas
col6 = st.columns(1) # Segunda linha com três colunas


#https://emojipedia.org/pt/black-friday
# Exibir o gráfico na primeira coluna


col1.subheader(':blue[Vendas]:moneybag:')
col1.info(cabe)

col2.subheader(':red[Saidas]:money_with_wings:')
col2.info(cabe)

col3.subheader('Lucro :truck:')
col3.info(cabe)


# Criar o gráfico de faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="payment_value", color="customer_state", title="Faturamento por dia")

# Exibir o gráfico na primeira coluna
col4.plotly_chart(fig_date, use_container_width=True)

# Criar o gráfico de faturamento por tipo de produto
fig_prod = px.line(df_filtered, x="Date", y="Categoria", 
                  color="customer_state", title="Faturamento por tipo de produto",
                  orientation="v")

# Exibir o gráfico na segunda coluna
col5.plotly_chart(fig_prod, use_container_width=True)

# Calcular o faturamento total por cidade
city_total = df_filtered.groupby("customer_city")[["payment_value"]].sum().reset_index()

# Criar o gráfico de barras para exibir o faturamento por cidade
fig_city = px.bar(city_total, x="payment_value", y="customer_city",
title="Faturamento por cidade")

st.plotly_chart(fig_city, use_container_width=True)

# Exibir o gráfico na terceira coluna








