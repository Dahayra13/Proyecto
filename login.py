import streamlit as st
from PIL import Image
import time

# Configurar el diseño de la página
st.set_page_config(layout="centered")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")

# Credenciales de inicio de sesión
User = "41650931"
Password = "cayetano"

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .login-container {
        background-color: white;
        width: 400px;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
    }
    .portal-title {
        text-align: center;
        color: #1A4D80;
        margin-bottom: 20px;
        font-size: 32px;
        font-weight: bold;
    }
    .form-field {
        margin-bottom: 20px;
    }
    .form-field label {
        font-size: 16px;
        font-weight: bold;
        color: #1A4D80;
        margin-bottom: 5px;
    }
    .form-field input {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 10px;
        background-color: #f0f0f0;
        font-size: 16px;
    }
    .submit-button {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 10px;
        background-color: #1A4D80;
        color: white;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .submit-button:hover {
        background-color: #134266;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image(university_logo, use_column_width=True)
st.markdown("<div class='login-container'><h1 class='portal-title'>🎓 Portal de Matrícula - UPCH</h1>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input(" Usuario: ", value=User)
    password = st.text_input("Contraseña:", type="password", value=Password)
    submit = st.form_submit_button("Iniciar Sesión", use_container_width=True)

# Cerrar el div del login-container
st.markdown("</div>", unsafe_allow_html=True)

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == User and password == Password:
        st.success("¡Correct user!")
        time.sleep(2)
        st.balloons()
    else:
        st.error("Invalid username or password. Please try again.")
















