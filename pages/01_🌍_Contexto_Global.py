import streamlit as st
import os
image_path1 = os.path.join(os.getcwd(), "imagen1.jpg")
image_path2 = os.path.join(os.getcwd(), "imagen2.jpg")
image_path3 = os.path.join(os.getcwd(), "imagen3.jpg")
image_path4 = os.path.join(os.getcwd(), "imagen4.jpg")
image_path5 = os.path.join(os.getcwd(), "imagen5.jpg")
image_path6 = os.path.join(os.getcwd(), "imagen6.jpg")
# Setup web page
st.set_page_config(
     page_title="🌍Contexto Global",
     page_icon= "internet.png",
     layout="wide")

st.title('🌍Contexto Global')
st.markdown('***')

st.markdown("La siguiente información fue extraida del informe 'El estado de digitalización de América Latina frente a la pandemia del COVID 19, disponible en: https://scioteca.caf.com/bitstream/handle/123456789/1540/El_estado_de_la_digitalizacion_de_America_Latina_frente_a_la_pandemia_del_COVID-19.pdf?sequence=1&isAllowed=y ")

st.markdown('***')
st.markdown("## Digitalización Global")
st.image(image=image_path1, caption="Digitalización Global", use_column_width=True)
    
st.markdown('***')
st.markdown("## Aumento tráfico de Wi-Fi")
st.image(image=image_path2, caption="Aumento tráfico de Wi-Fi", use_column_width=True)

st.markdown('***')
st.markdown("## Penetración Internet América Latina")
st.image(image=image_path3, caption="Penetración de internet América Latina", use_column_width=True)

st.markdown('***')
st.markdown("## Penetración Facebook América Latina")
st.image(image=image_path4, caption="Penetración Facebook", use_column_width=True)

st.markdown('***')
st.markdown("## Uso de Plataformas Digitales")
st.image(image=image_path5, caption="Plataformas Digitales", use_column_width=True)

st.markdown('***')
st.markdown("## Digitalización Cadena de Aprovisionamiento")
st.image(image=image_path6, caption="Cadena de Aprovisionamiento", use_column_width=True)