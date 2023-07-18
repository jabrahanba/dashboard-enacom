import streamlit as st
import os
image_path1 = os.path.join(os.getcwd(), "imagen1.jpg")

# Setup web page
st.set_page_config(
     page_title="🌍Contexto Global",
     page_icon= "internet.png",
     layout="wide")

st.title('🌍Contexto Global')

st.markdown('***')
st.markdown("La siguiente información fue extraida del informe 'El estado de digitalización de América Latina frente a la pandemia del COVID 19, disponible en: https://scioteca.caf.com/bitstream/handle/123456789/1540/El_estado_de_la_digitalizacion_de_America_Latina_frente_a_la_pandemia_del_COVID-19.pdf?sequence=1&isAllowed=y ")
st.markdown("## Estado de la digitalización en América Latina")
st.image(image=image_path1, caption="Digitalización Global", use_column_width=True)
    
