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
     page_icon= "internet.png",
     layout="wide")

st.title('📊Análisis Global')
st.markdown('A continuación se presentan los gráficos relativos al acceso a internet a nivel global en Argentina')

#importar dataframe:
dataGlobal = pd.read_csv('dataGlobal.csv')

#1er gráfico:
st.markdown('***')
#Seleccionar el tema:
#dim = st.radio('Seleccionar tema:',('plotly', 'plotly_white', 'plotly_dark', 'ggplot2', 'seaborn', 'simple_white', 'none'), horizontal=True)
dim = 'plotly'
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


# grafico 4
st.markdown('***')
st.markdown('### Gráfico de población proyectada por grupo etario 📈')
df4 = pd.read_excel('provincias_anio_edad.xlsx', sheet_name='pais-anio-edad')
df4 = df4[['Anio', 'rango_0_a_9', 'rango_10_a_19', 'rango_20_a_29', 'rango_30_a_49', 'rango_mayor_a_50', 'total_rangos']]
rangos = ['rango_0_a_9', 'rango_10_a_19', 'rango_20_a_29', 'rango_30_a_49', 'rango_mayor_a_50','total_rangos']
# Crear subplots
fig = make_subplots(rows=1, cols=1)
traces = []
for r in rangos:
    anio = df4['Anio']
    rango = df4[r]
    trace = go.Scatter(x=anio, y=rango, name=r)
    traces.append(trace)

for trace in traces:
    fig.add_trace(trace)

fig.update_layout(
    xaxis=dict(title='Año', tickangle=90),
    yaxis=dict(title='Personas'),
    legend=dict(orientation='h', x=0, y=-0.2),
    showlegend=True
)

buttons = []
for i, r in enumerate(rangos):
    visible = [False] * len(traces)
    visible[i] = True

    button = dict(
        label=r,
        method='update',
        args=[{'visible': visible}, {'title': f'Grupo Etario: {r}'}]
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
if st.checkbox('Mostrar Dataframe'):
    st.dataframe(df4)