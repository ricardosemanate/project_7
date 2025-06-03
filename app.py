import pandas as pd 
import plotly.express as px
import streamlit as st 

st.header('venta de carros en Estados Unidos')

car_data = pd.read_csv('vehicles_us.csv')
car_data['cylinders'] = car_data['cylinders'].fillna(car_data['cylinders'].median())
car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].median())
car_data['model_year'] = car_data['model_year'].fillna(car_data['model_year'].mode()[0])
car_data['is_4wd'] = car_data['is_4wd'].fillna(0).astype(bool)

categorical_cols = ['paint_color', 'model', 'fuel', 'transmission', 'type']
for col in categorical_cols:
    car_data[col] = car_data[col].fillna('unknown')

st.subheader('dataset')
if st.checkbox('mostrar datos procesados'):
    st.write(car_data.head())

st.subheader('Datos')
hist_button = st.button('Historigrama de kilometraje')

if hist_button: 
    st.write('Historigrama de la columna kilometraje')
    fig = px.histogram(car_data, x= 'odometer', title= 'Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir Gráfico de Dispersión de Precio vs. Kilometraje')

if scatter_button:
    st.write('Creando un gráfico de dispersión de precio vs. kilometraje')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='precio vs kilometraje')
    st.plotly_chart(fig_scatter, use_container_widh=True)