import pyshorteners
import streamlit as st
from PIL import Image

def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

# Creamos app web con Streamlit
st.set_page_config(page_title="Acortador de URL", page_icon="✏️", layout="centered")
#st.image("images/cabecera.png", use_column_width=True)
#st.image("images/cabecera.png", use_container_width=True)
image = Image.open("images/cabecera.png")
st.image(image, caption="Cabecera", width=700)  # Ajusta el ancho según lo necesites


st.title("Acortador de URL")

# Texto explicativo con color verde para "Acortador de URL"
st.markdown("""
    Bienvenido al <span style="color:rgb(85, 197, 159)"><strong>**Acortador de URL**</strong></span>. Esta herramienta te permite transformar tus enlaces largos en versiones más cortas y fáciles de compartir.
    Solo tienes que introducir la URL que deseas acortar en el campo de texto y hacer clic en el botón para generar el enlace corto.
    ¡Prueba ahora y haz tus enlaces más manejables!
""", unsafe_allow_html=True)

url = st.text_input("Introduce la URL")
if st.button("Genera la URL corta"):
    st.write("Acortador de URL: ", shorten_url(url))
