import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Gestão da venda de veículos')
hist_button = st.button('Criar histograma')
disp_button = st.button('Criar gráfico de dispersão')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    # mensagem descritiva:
    st.write(
        'Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

    # Criação do gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibição do gráfico
    fig.show()
