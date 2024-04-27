import streamlit as st
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(page_title="UPCH - Portal de Matrícula", page_icon=":mortar_board:")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")

# Crear el diseño del formulario de inicio de sesión
st.markdown("<h1 style='text-align: center; color: #1A4D80;'>Universidad Cayetano</h1>", unsafe_allow_html=True)
st.image(university_logo, use_column_width=True)
st.markdown("<h2 style='text-align: center; color: #1A4D80;'>Portal de Matrícula</h2>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input("User: ")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Log In")

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == "admin" and password == "password":
        st.success("Logged in successfully!")
    else:
        st.error("Invalid username or password. Please try again.")

# Aplicar el fondo de color "Cayetano"
st.markdown(
    """
    <style>
    .stApp {
        background-color: #1A4D80;
    }
    </style>
    """,
    unsafe_allow_html=True
)





