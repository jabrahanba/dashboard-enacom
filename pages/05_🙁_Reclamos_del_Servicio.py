import streamlit as st
import pandas as pd

# Setup web page
st.set_page_config(
     page_title="🙁Reclamos del Servicio",
     page_icon= "internet.png",
     layout="wide")

st.title('🙁Reclamos del Servicio')
st.markdown('***')

total_tipo = pd.read_excel('DENUN-Y-RECLA-12878.xlsx', sheet_name='Total por Tipo')
st.markdown('### Total de Reclamos por tipo, enero a mayo 2023')
st.dataframe(total_tipo)

reclamo_servicio = pd.read_excel('DENUN-Y-RECLA-12878.xlsx', sheet_name='Reclamos_servicio')
st.markdown('### Cantidad de Reclamos por Servicios, enero a mayo 2023')
st.dataframe(reclamo_servicio)

internet = pd.read_excel('DENUN-Y-RECLA-12878.xlsx', sheet_name='Cinco_internet')
st.markdown('### Reclamos por prestador de servicio de Internet, enero a mayo 2023')
st.dataframe(internet)