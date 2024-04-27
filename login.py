import streamlit as st
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(page_title="Portal de Plan de Estudios", page_icon=":mortar_board:")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")

# Cargar la imagen de fondo
background_image = Image.open("universidad.jpg")

# Credenciales de inicio de sesión
User = "41650931"
Password = "cayetano"

# Crear el diseño del formulario de inicio de sesión
st.markdown("<h1 style='text-align: center; color: #1A4D80;'>Universidad Cayetano</h1>", unsafe_allow_html=True)
st.image(university_logo, use_column_width=True)
st.markdown("<h3 style='text-align: center; color: #f8f9fa;'>Portal de Plan de Estudios</h3>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input("User: ", value=User)
    password = st.text_input("Password:", type="password", value=Password)
    submit = st.form_submit_button("Log In")

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == User and password == Password:
        st.success("¡correct user!")
    else:
        st.error("Invalid username or password. Please try again.")

# Aplicar la imagen de fondo
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{background_image.tobytes('jpeg')}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)







