import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles.csv")

st.header("Análise de Anúncio de Veículos")

hist_button = st.button("Criar Histograma de Preços")

if hist_button:
    st.write("Criando um histograma mostrando a distribuição dos preços dos veículos")
    
    fig = px.histogram(
        car_data,
        x='price',
        title='Distribuição de Quilometragem dos Veículos',
        nbins=50
    )
    
    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
scatter_button = st.button("Criar Gráfico de Dispersão")

if scatter_button:
    st.write("Criando gráfico de dispersão entre quilometragem e preço")
    
    fig = px.scatter(
        car_data, 
        x='odometer',
        y='price',
        title="Preço x Quilometragem dos veículos",
        opacity=0.5
    )
    
    st.plotly_chart(
        fig,
        use_container_width=True
    )