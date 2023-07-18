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
     page_title="🌍Contexto Global",
     page_icon= "internet.png",
     layout="wide")

st.title('🌍Contexto Global')
st.markdown('A continuación se presentan los gráficos relativos al acceso a internet a nivel global en Argentina')


st.markdown('***')
st.markdown("La siguiente información fue extraida del informe 'El estado de digitalización de América Latina frente a la pandemia del COVID 19, disponible en: https://scioteca.caf.com/bitstream/handle/123456789/1540/El_estado_de_la_digitalizacion_de_America_Latina_frente_a_la_pandemia_del_COVID-19.pdf?sequence=1&isAllowed=y ")
st.markdown("## Estado de la digitalización en América Latina")
