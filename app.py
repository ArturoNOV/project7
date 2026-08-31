import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Muestra un enccabezado para la aplicación
st.header('Análisis exploratorio de datos')

# crear una casilla de verificación
build_od_dispersion = st.checkbox('Incluir un gráfico de la relación precio y kilometraje')

if build_od_dispersion: # si la casilla de verificación está seleccionada
    st.write('Se incluirá además la relación entre Odómetro y Precio')

# Crear un botón en la aplicación Streamlit
hist_button = st.button('Construir')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    st.write('Histograma distribución del odómetro')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Se añade un título al gráfico
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'width='stretch'' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, width='stretch')
    
    if build_od_dispersion:
        # Crear un scatter plot utilizando plotly.graph_objects
        # Se crea una figura vacía y luego se añade un rastro de scatter
        fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

        # Se añade un título al gráfico
        fig.update_layout(title_text='Relación entre Odómetro y Precio')
        
        # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
        # 'width='stretch'' ajusta el ancho del gráfico al contenedor
        st.plotly_chart(fig, width='stretch')

