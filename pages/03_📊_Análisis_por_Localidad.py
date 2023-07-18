import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import json
from plotly.subplots import make_subplots
pd.set_option('display.max_columns', 200) #Mostrar todas las columnas
pd.set_option('display.float_format', '{:.2f}'.format) #No mostrar notación científica

# Setup web page
st.set_page_config(
     page_title="📊Análisis por Localidad",
     page_icon= "src\internet.png",
     layout="wide")


#importar dataframe:

dataLocalidad = pd.read_csv('data\dataLocalidad.csv')

#1er gráfico:
st.markdown('***')
st.markdown('### Cantidad de Accesos por Rango de Velocidad por Tecnología')
dim = st.radio('Seleccionar tecnología a visualizar:',('adsl', 'cableModem', 'dialUp','fibraOptica', 'satelital', 'wimax', 'wireless', 'otros_tec'), horizontal=True)
df1 = dataLocalidad[['provincia','localidad','adsl','cableModem','dialUp','fibraOptica', 'satelital', 'wimax', 'wireless', 'otros_tec','latitud','longitud']]

if st.checkbox('Quitar CABA para visualizar mejor las localidades en Provincias en este gráfico'):
    df1 = dataLocalidad[['provincia','localidad','adsl','cableModem','dialUp','fibraOptica', 'satelital', 'wimax', 'wireless', 'otros_tec','latitud','longitud']]

    df1 = df1[df1['localidad'] != 'Palermo'].reset_index()
else:
    df1 = dataLocalidad[['provincia','localidad','adsl','cableModem','dialUp','fibraOptica', 'satelital', 'wimax', 'wireless', 'otros_tec','latitud','longitud']]

with open('data/ProvinciasArgentina.geojson') as f:
    data_provincias = json.load(f)
fig = go.Figure()
# Agregar capa de las divisiones de provincias
fig.add_trace(go.Choroplethmapbox(geojson=data_provincias, featureidkey='properties.nombre'))
# Agregar capa de los marcadores de las localidades
fig.add_trace(go.Scattermapbox(
    lat=df1['latitud'],
    lon=df1['longitud'],
    mode='markers',
    marker=dict(
        size=5,
        color=df1[dim],
        colorscale="Rainbow",
        cmin=df1[dim].min(),
        cmax=df1[dim].max(),
        opacity=0.8,
        colorbar=dict(title=dim)
    ),
    hovertemplate='<b>%{text}</b><br>Cantidad: %{marker.color:.2f}<extra></extra>',
    text=df1['localidad']
))
# Configurar diseño del mapa
fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=-38.40, lon=-63.60),
        zoom=3
    ),
    margin=dict(r=0, t=0, l=0, b=0)
)
st.plotly_chart(fig)
if st.checkbox('Mostrar Dataframe'):
    st.dataframe(df1)

#2do gráfico:
st.markdown('***')
st.markdown('### Cantidad de Accesos por Rango de Velocidad por Localidad')
dim2 = st.radio('Seleccionar el rango de velocidad a visualizar:',('de0a9Mbps','de10a20Mbps','de21a49Mbps','de50a99Mbps','de100a199Mbps','de200a499Mbps','de500a1024Mbps','otros'), horizontal=True)

if st.checkbox('Quitar CABA para visualizar mejor las localidades en Provincias'):
    df2 = dataLocalidad[['provincia','localidad','de0a9Mbps','de10a20Mbps','de21a49Mbps','de50a99Mbps','de100a199Mbps','de200a499Mbps','de500a1024Mbps','otros','latitud','longitud']]
    df2 = df2[df2['localidad'] != 'Palermo'].reset_index()
else:
    df2 = dataLocalidad[['provincia','localidad','de0a9Mbps','de10a20Mbps','de21a49Mbps','de50a99Mbps','de100a199Mbps','de200a499Mbps','de500a1024Mbps','otros','latitud','longitud']]
with open('data/ProvinciasArgentina.geojson') as f:
    data_provincias = json.load(f)
fig = go.Figure()
# Agregar capa de las divisiones de provincias
fig.add_trace(go.Choroplethmapbox(geojson=data_provincias, featureidkey='properties.nombre'))
# Agregar capa de los marcadores de las localidades
fig.add_trace(go.Scattermapbox(
    lat=df2['latitud'],
    lon=df2['longitud'],
    mode='markers',
    marker=dict(
        size=5,
        color=df2[dim2],
        colorscale="Rainbow",
        cmin=df2[dim2].min(),
        cmax=df2[dim2].max(),
        opacity=0.8,
        colorbar=dict(title=dim2)
    ),
    hovertemplate='<b>%{text}</b><br>Cantidad: %{marker.color:.2f}<extra></extra>',
    text=df2['localidad']
))
# Configurar diseño del mapa
fig.update_layout(
    mapbox=dict(
        style="open-street-map",
        center=dict(lat=-38.40, lon=-63.60),
        zoom=3
    ),
    margin=dict(r=0, t=0, l=0, b=0)
)
st.plotly_chart(fig)
if st.checkbox('Mostrar Dataframe:'):
    st.dataframe(df2)