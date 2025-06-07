import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV (asegúrate que vehicles_us.csv esté en la misma carpeta que app.py)
car_data = pd.read_csv('vehicles_us.csv')

# Título y encabezado
st.title("Dashboard de Anuncios de Venta de Coches")
st.header("Análisis Exploratorio de Datos")

# Botones para construir gráficos
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer", nbins=50, title="Histograma del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    fig_scatter = px.scatter(car_data, x="model_year", y="price", 
                             title="Dispersión Precio vs Año por Fabricante")
    st.plotly_chart(fig_scatter, use_container_width=True)