import streamlit as st

# Setup web page
st.set_page_config(
     page_title="Data Analytics ENACOM 🌐🇦🇷",
     page_icon= "internet.png",
     layout="wide")


st.title('Análisis de Datos de Acceso a Internet en Argentina 🌐🇦🇷')

st.markdown('***')
st.markdown('# Informe Analítico de Datos Abiertos del Servicio de Internet en Argentina 📊')

st.markdown("### Tecnologías de Acceso a Internet 🖥️📡")
st.markdown("Internet es una red de redes de computadoras que se conectan mediante diferentes medios, como líneas telefónicas, fibras ópticas, cables submarinos y enlaces por satélite. Los usuarios se conectan a través de proveedores de acceso que ofrecen servicios de conexión, ya sea mediante comunicaciones telefónicas (dial-up), banda ancha (ADSL, cablemódem, conexión inalámbrica o satelital) o enlaces punto a punto.")
st.markdown("Existen varias tecnologías utilizadas para el acceso a internet en Argentina:")

st.subheader("Cuentas de Internet")
st.markdown("Las cuentas de internet se refieren a la cantidad de conexiones contratadas entre proveedores de acceso y sus respectivos clientes, por las cuales se paga un abono mensual.")

st.subheader("Banda Estrecha")
st.markdown("Las conexiones de banda estrecha utilizan un ancho de banda reducido, siendo la conexión más común el dial-up (acceso telefónico) que se realiza a través de una llamada telefónica local utilizando un módem. En este tipo de conexión, se abonan los pulsos telefónicos consumidos y el servicio de acceso a Internet.")

st.subheader("Banda Ancha")
st.markdown("Las conexiones de banda ancha utilizan un mayor ancho de banda, lo que implica mayores velocidades y un mayor tráfico de datos, voz e imágenes. Los usuarios suelen tener acceso permanente a internet, aunque existen modalidades limitadas a determinadas bandas horarias. En este tipo de conexión, no se abonan pulsos telefónicos.")
st.markdown("- **DSL (Digital Subscriber Line - Línea de Abonado Digital)**: conexiones realizadas mediante el cableado de los operadores telefónicos. La tecnología DSL presenta diferentes alternativas y velocidades de acceso a internet, siendo la más frecuente en Argentina el ADSL.")
st.markdown("- **Cablemódem**: conexiones realizadas mediante cable coaxial, aprovechando la red de los operadores de cable. Los abonados a este tipo de conexión comparten el ancho de banda proporcionado por una línea de cable coaxial, por lo que la velocidad puede variar según la cantidad de usuarios que estén utilizando el servicio simultáneamente.")
st.markdown("- **Fibra Óptica**: tecnología que utiliza cables de fibra óptica para transmitir datos a velocidades mucho más altas que las tecnologías DSL o cablemódem. Permite velocidades de conexión significativamente mayores, en el orden de diez o cien veces más Mbps. Además, la fibra óptica puede proporcionar servicios adicionales como telefonía por internet (VoIP) y vídeo bajo demanda.")
st.markdown("- **Inalámbrica (Wireless)**: conexiones realizadas sin cables, clasificadas como fijas o móviles según la tecnología utilizada en la red. Los servicios de banda ancha inalámbrica fija más comunes son WiFi y WiMax, mientras que los servicios de banda ancha inalámbrica móvil, como el 3G, se obtienen a través de compañías de telefonía móvil y otros proveedores.")
st.markdown("- **Satelital**: conexiones que se realizan mediante un satélite alquilado por el proveedor de servicios de internet (ISP). El usuario realiza la conexión utilizando una antena instalada en su domicilio proporcionada por el ISP.")



## SIDEBAR:
st.sidebar.markdown('Análisis realizados:')