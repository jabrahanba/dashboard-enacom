import streamlit as st
import pandas as pd
import numpy as np
import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
pd.set_option('display.max_columns', 200) #Mostrar todas las columnas
pd.set_option('display.float_format', '{:.2f}'.format) #No mostrar notación científica
import plotly.io as pio

# Setup web page
st.set_page_config(
     page_title="📊Análisis por Provincia",
     page_icon= "internet.png",
     layout="wide")


#importar dataframe:
dataProvincia = pd.read_csv('dataProvincia.csv')

#Seleccionar tema
dim = st.radio('Seleccionar tema:',('plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 'seaborn', 'simple_white', 'none'), horizontal=True)
#Seleccionar trimestre
trim = st.radio('Seleccionar el trimestre:',(1, 2, 3, 4), horizontal=True)
st.write('Se recomienda utilizar el 3er trimestre para poder comparar propiamente cada año, pues los datos para el 2022 solo están hasta el 3er trimestre')


#1er gráfico:
st.markdown('***')
st.markdown('### Cantidad de accesos Banda Ancha Fija y Dial-Up 📶')
df1 = dataProvincia[['anio','trimestre','provincia','region','bandaAnchaFija','dialUp','total_ba_du']]
lista_regiones = ['Provincia de Buenos Aires', 'Norte Grande Argentino', 'Patagonia', 'Centro', 'Nuevo Cuyo']
fig = make_subplots(rows=1, cols=2, column_widths=[0.8, 0.2])
traces = []
for r in lista_regiones:
    df_region = df1[df1['trimestre'] == trim].reset_index()
    df_region = df_region.groupby(['region', 'anio'])[['bandaAnchaFija', 'dialUp']].sum().reset_index()
    df_region = df_region[df_region['region'] == r]
    df_region.sort_values(by='anio', inplace=True)
    anio = df_region['anio']
    bandaAnchaFija = df_region['bandaAnchaFija']
    dialUp = df_region['dialUp']
    trace_bandaAnchaFija = go.Scatter(x=anio, y=bandaAnchaFija, name='Banda Ancha Fija', legendgroup=r, showlegend=False)
    traces.append(trace_bandaAnchaFija)
    trace_dialUp = go.Scatter(x=anio, y=dialUp, name='Dial-Up', legendgroup=r, showlegend=False)
    traces.append(trace_dialUp)
    fig.add_trace(trace_bandaAnchaFija, row=1, col=1)
    fig.add_trace(trace_dialUp, row=1, col=1)
fig.update_traces(showlegend=True)  # Mostrar la leyenda
fig.update_layout(
    xaxis=dict(title='Año'),
    yaxis=dict(title='Cantidad de Accesos'),
    legend=dict(orientation='h', x=0, y=-0.2),
    showlegend=True,
    template=dim)
buttons = []
for r in lista_regiones:
    visible_indices = [i for i in range(len(traces)) if traces[i]['legendgroup'] == r]
    visible = [False] * len(traces)
    for i in visible_indices:
        visible[i] = True
    button = dict(
        label=r,
        method='update',
        args=[{'visible': visible}, {'title': f'Cantidad de accesos Banda Ancha Fija y Dial-Up en {r}'}]
    )
    buttons.append(button)
fig.update_layout(
    updatemenus=[dict(
        type='buttons',
        buttons=buttons,
        active=0,
        direction='down',
        x=0.99,
        y=0.5
    )]
)
st.plotly_chart(fig)


#2do gráfico:
st.markdown('***')
st.markdown('### Cantidad de acceso por cada 100 hogares y 100 habitantes 🏠👥')
df2 = dataProvincia[['anio','trimestre','provincia','region','accesx100hab','accesx100hog']]
lista_regiones = ['Provincia de Buenos Aires', 'Norte Grande Argentino', 'Patagonia', 'Centro', 'Nuevo Cuyo']
fig = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3])
traces = []
for r in lista_regiones:
    df_region = df2[df2['trimestre'] == trim].reset_index()
    df_region = df_region.groupby(['region', 'anio'])[['accesx100hab', 'accesx100hog']].sum().reset_index()
    df_region = df_region[df_region['region'] == r]
    df_region.sort_values(by='anio', inplace=True)
    anio = df_region['anio']
    accesx100hab = df_region['accesx100hab']
    accesx100hog = df_region['accesx100hog']
    trace_accesx100hab = go.Scatter(x=anio, y=accesx100hab, name='Acceso por cada 100 habitantes', legendgroup=r, showlegend=False)
    traces.append(trace_accesx100hab)
    trace_accesx100hog = go.Scatter(x=anio, y=accesx100hog, name='Acceso por cada 100 hogares', legendgroup=r, showlegend=False)
    traces.append(trace_accesx100hog)
    fig.add_trace(trace_accesx100hab, row=1, col=1)
    fig.add_trace(trace_accesx100hog, row=1, col=1)
fig.update_traces(showlegend=True)  # Mostrar la leyenda
fig.update_layout(
    xaxis=dict(title='Año'),
    yaxis=dict(title='Cantidad de Accesos'),
    legend=dict(orientation='h', x=0, y=-0.2),
    showlegend=True
)
buttons = []
for r in lista_regiones:
    visible_indices = [i for i in range(len(traces)) if traces[i]['legendgroup'] == r]
    visible = [False] * len(traces)
    for i in visible_indices:
        visible[i] = True
    button = dict(
        label=r,
        method='update',
        args=[{'visible': visible}, {'title': f'Región: {r}'}]
    )
    buttons.append(button)
fig.update_layout(
    updatemenus=[dict(
        type='buttons',
        buttons=buttons,
        active=0,
        direction='down',
        x=0.99,
        y=0.5
    )]
)
st.plotly_chart(fig)


#3er gráfico:
st.markdown('***')
st.markdown('### Cantidad de Accesos por Tecnología📡📶🖧')
df3 = dataProvincia[['anio','trimestre','provincia','region','adsl','cableModem','fibraOptica','wireless','otras_tecno','total_tec']]
lista_regiones = ['Provincia de Buenos Aires', 'Norte Grande Argentino', 'Patagonia', 'Centro', 'Nuevo Cuyo']
fig = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3])
traces = []
for r in lista_regiones:
    df_region = df3[df3['trimestre'] == trim].reset_index()
    df_region = df_region.groupby(['region', 'anio'])[['adsl', 'cableModem', 'fibraOptica', 'wireless', 'otras_tecno']].sum().reset_index()
    df_region = df_region[df_region['region'] == r]
    df_region.sort_values(by='anio', inplace=True)
    anio = df_region['anio']
    adsl = df_region['adsl']
    cableModem = df_region['cableModem']
    fibraOptica = df_region['fibraOptica']
    wireless = df_region['wireless']
    otras_tecno = df_region['otras_tecno']
    trace_adsl = go.Scatter(x=anio, y=adsl, name='adsl', legendgroup=r, visible=False)
    traces.append(trace_adsl)
    trace_cableModem = go.Scatter(x=anio, y=cableModem, name='cableModem', legendgroup=r, visible=False)
    traces.append(trace_cableModem)
    trace_fibraOptica = go.Scatter(x=anio, y=fibraOptica, name='fibraOptica', legendgroup=r, visible=False)
    traces.append(trace_fibraOptica)
    trace_wireless = go.Scatter(x=anio, y=wireless, name='wireless', legendgroup=r, visible=False)
    traces.append(trace_wireless)
    trace_otras_tecno = go.Scatter(x=anio, y=otras_tecno, name='otras_tecno', legendgroup=r, visible=False)
    traces.append(trace_otras_tecno)
    fig.add_trace(trace_adsl, row=1, col=1)
    fig.add_trace(trace_cableModem, row=1, col=1)
    fig.add_trace(trace_fibraOptica, row=1, col=1)
    fig.add_trace(trace_wireless, row=1, col=1)
    fig.add_trace(trace_otras_tecno, row=1, col=1)
fig.update_layout(
    xaxis=dict(title='Año', tickangle=90),
    yaxis=dict(title='Cantidad de Accesos'),
    legend=dict(orientation='h', x=0, y=-0.2),
    showlegend=True
)
buttons = []
for r in lista_regiones:
    visible_indices = [i for i in range(len(traces)) if traces[i]['legendgroup'] == r]
    visible = [False] * len(traces)
    for i in visible_indices:
        visible[i] = True
    button = dict(
        label=r,
        method='update',
        args=[{'visible': visible}, {'title': f'Región: {r}'}]
    )
    buttons.append(button)
fig.update_layout(
    updatemenus=[dict(
        type='buttons',
        buttons=buttons,
        active=0,
        direction='down',
        x=0.99,
        y=0.5
    )]
)
st.plotly_chart(fig)

#4to grafico:
st.markdown('***')
st.markdown('### Velocidad Media de Descarga por Región 📶🗺️')
df4 = dataProvincia[['anio','trimestre','provincia','region','velocidadMediaDesc']]
#lista_regiones = ['Provincia de Buenos Aires', 'Norte Grande Argentino', 'Patagonia', 'Centro', 'Nuevo Cuyo']
lista_regiones = st.multiselect('Selecciona la región o regiones a visualizar:', ('Provincia de Buenos Aires', 'Norte Grande Argentino', 'Patagonia', 'Centro', 'Nuevo Cuyo'))
fig = make_subplots(rows=1, cols=1)
traces = []
for r in lista_regiones:
    df_region = df4[df4['trimestre'] == trim].reset_index()
    df_region = df_region.groupby(['region', 'anio'])[['velocidadMediaDesc']].mean().reset_index()
    df_region = df_region[df_region['region'] == r]
    df_region.sort_values(by='anio', inplace=True)
    anio = df_region['anio']
    velocidadMediaDesc = df_region['velocidadMediaDesc']
    trace = go.Scatter(x=anio, y=velocidadMediaDesc, name=r)
    traces.append(trace)
for trace in traces:
    fig.add_trace(trace)
fig.update_layout(
    xaxis=dict(title='Año', tickangle=90),
    yaxis=dict(title='Velocidad Media de Descarga'),
    legend=dict(orientation='h', x=0, y=-0.2),
    showlegend=True
)
st.plotly_chart(fig)
provincias_regiones = pd.read_excel('provincias_localidades_coorde.xlsx', sheet_name='Provincias')
if st.checkbox('Mostrar Provincias por Region'):
    st.dataframe(provincias_regiones[['Region', 'Provincia']].sort_values('Region'))


#5to grafico
st.markdown('***')
st.markdown('### Accesos por Tecnología y por Provincia 📶🗺️')
dim = st.radio('Seleccionar tecnología a visualizar:',('adsl', 'cableModem','fibraOptica','wireless', 'otras_tecno'), horizontal=True)
anio = st.radio('Selecciona el año:', (2014,2015,2016,2017,2018,2019,2020,2021,2022), horizontal=True)
df6 = dataProvincia[['anio','trimestre','provincia','adsl', 'cableModem','fibraOptica','wireless', 'otras_tecno']]
df_region = df6[(df6['anio'] == anio) & (df6['trimestre'] == trim)].reset_index()
df_mapa = df_region.copy()
df_mapa['provincia']=df_mapa['provincia'].replace({
    'Santiago Del Estero':'Santiago del Estero', 
    'Tierra Del Fuego - Antártida E Islas Del Atlántico Sur': 'Tierra del Fuego',
    'Ciudad De Buenos Aires':'Capital Federal',
    'Tucumán':'TucumÃ¡n',
    'Córdoba':'CÃ³rdoba',
    'Entre Ríos':'Entre RÃ­os',
    'Neuquén':'NeuquÃ©n',
    'Río Negro':'RÃ­o Negro'
    })
with open('ProvinciasArgentina.geojson') as f:   
    data = json.load(f)

fig = px.choropleth_mapbox(df_mapa, geojson=data,featureidkey='properties.nombre', locations='provincia', color=dim,
                           color_continuous_scale="Viridis",
                           range_color=(df_mapa[dim].min(), df_mapa[dim].max()),
                           mapbox_style= "open-street-map", 
                           zoom=3, center = {"lat": -38.40, "lon": -63.60},
                           opacity=0.4,
                           labels={'Cantidad':dim}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig)
if st.checkbox('Mostrar Provincias y Region'):
    st.dataframe(df_region)


#6to grafico
st.markdown('***')
st.markdown('### Velocidad Media de Descarga por Año 📶📅')
df4 = dataProvincia[['anio','trimestre','provincia','region','velocidadMediaDesc']]
lista_anios = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
fig = go.Figure()
for anio in reversed(lista_anios):
    df_año = df4[df4['anio'] == anio].reset_index()
    df_año = df_año.groupby(['provincia', 'anio'])[['velocidadMediaDesc']].mean().reset_index()
    provincia = df_año['provincia']
    provincia = provincia.str.replace('Tierra Del Fuego - Antártida E Islas Del Atlántico Sur','Tierra del Fuego')
    velocidadMediaDesc = df_año['velocidadMediaDesc']
    fig.add_trace(go.Scatter(x=provincia, y=velocidadMediaDesc, name=f'Año {anio}', fill='tozeroy'))
fig.update_layout(
    xaxis=dict(title='Provincias'),
    yaxis=dict(title='Mbps'),
    legend=dict(x=1, y=0.5),
    margin=dict(l=20, r=20, t=60, b=20),
    showlegend=True
)
st.plotly_chart(fig)

#7mo gráfico:
st.markdown('***')
st.markdown('### Gráfico de población proyectada por grupo etario - Provincias 📈')
grupo_etario = st.radio('Selecciona el grupo etario', ('rango_0_a_9','rango_10_a_19','rango_20_a_29','rango_30_a_49','rango_mayor_a_50','total_rangos'), horizontal=True)
df7 = pd.read_excel('provincias_anio_edad.xlsx', sheet_name='provincias-anio-edad')
df7 = df7[['Anio','Provincia','rango_0_a_9','rango_10_a_19','rango_20_a_29','rango_30_a_49','rango_mayor_a_50','total_rangos']]
lista_regiones = st.multiselect('Selecciona la provincia o provincias a visualizar:', ('Buenos Aires', 'CABA', 'Catamarca', 'Chaco', 'Chubut', 'Córdoba', 'Corrientes', 'Entre Ríos', 'Formosa', 'Jujuy', 'La Pampa', 'La Rioja', 'Mendoza', 'Misiones', 'Neuquén', 'Río Negro', 'Salta', 'San Juan', 'San Luis', 'Santa Cruz', 'Santa Fe', 'Santiago del Estero', 'Tierra del Fuego', 'Tucumán'))
fig = make_subplots(rows=1, cols=1)
traces = []
df_filtered = df7.copy()  # Crear una copia del DataFrame original
for r in lista_regiones:
    df_region = df_filtered[df_filtered['Provincia'] == r]  # Filtrar la copia en lugar del DataFrame original
    anio = df_region['Anio']
    edad = df_region[grupo_etario]
    trace = go.Scatter(x=anio, y=edad, name=r)
    traces.append(trace)
for trace in traces:
    fig.add_trace(trace)
fig.update_layout(
    xaxis=dict(title='Año', tickangle=90),
    yaxis=dict(title='Cantidad de personas en el grupo etario'),
    legend=dict(orientation='h', x=0, y=-0.2),
    showlegend=True
)
st.plotly_chart(fig)

if st.checkbox('Mostrar dataframe:'):
    st.dataframe(df7)