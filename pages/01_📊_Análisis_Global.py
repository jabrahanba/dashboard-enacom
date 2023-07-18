import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
pd.set_option('display.max_columns', 200) #Mostrar todas las columnas
pd.set_option('display.float_format', '{:.2f}'.format) #No mostrar notación científica
import plotly.io as pio

# Setup web page
st.set_page_config(
     page_title="📊Análisis Global",
     page_icon= "src\internet.png",
     layout="wide")


#importar dataframe:
dataGlobal = pd.read_csv('..\data\dataGlobal.csv')

#1era prueba mostrar el df:
if st.checkbox('Mostrar el dataframe Global'):
    st.dataframe(dataGlobal)

if st.checkbox('Vista de datos Head o Tail'):
    if st.button('Mostrar Head'):
        st.write(dataGlobal.head())
    if st.button('Mostrar Tail'):
        st.write(dataGlobal.tail())

dim = st.radio('Dimensión a mostrar:',('Filas','Columnas'), horizontal=True)
if dim == 'Filas':
    st.write(f'Cantidad de filas: {dataGlobal.shape[0]}')
else:
    st.write(f'Cantidad de columnas: {dataGlobal.shape[1]}')

#1er gráfico:
st.markdown('***')
#Seleccionar el tema:
dim = st.radio('Seleccionar tema:',('plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 'seaborn', 'simple_white', 'none'), horizontal=True)
st.markdown('### Ingreso global por años 📶')
data = dataGlobal.groupby('anio')['ingresos'].sum().reset_index()
fig = px.bar(data, x='anio', y='ingresos', template=dim)
fig.update_layout(
    xaxis_title='Año',
    yaxis_title='Ingresos'
)
st.plotly_chart(fig)

#2do gráfico:
st.markdown('***')
st.markdown('### Velocidad media de descarga por año y trimestre 📈')
anio_trimestre = dataGlobal['anio'].astype(str) + '-' + dataGlobal['trimestre'].astype(str)
velocidad = dataGlobal['velocidadMediaDesc']
data = pd.DataFrame({'anio_trimestre': anio_trimestre, 'velocidad': velocidad})
fig = px.line(data, x='anio_trimestre', y='velocidad', template=dim)
fig.update_layout(
    xaxis_title='Año - trimestre',
    yaxis_title='Velocidad media de descarga'
)
st.plotly_chart(fig)

#3er gráfico:
st.markdown('***')
st.markdown('### Velocidad media de descarga por año Boxplot 📊')
data_by_year = []
for year in sorted(set(dataGlobal['anio'])):
    data_year = dataGlobal[dataGlobal['anio'] == year]['velocidadMediaDesc']
    data_by_year.append(data_year)
fig = px.box(pd.DataFrame(data_by_year), x=dataGlobal['anio'], y=dataGlobal['velocidadMediaDesc'], template=dim)
fig.update_xaxes(title='Año', type='category')
fig.update_yaxes(title='Velocidad Media')
fig.update_xaxes(autorange="reversed")
st.plotly_chart(fig)


#ejemplo
if st.checkbox('Mostrar texto'):
    st.write('Hola')