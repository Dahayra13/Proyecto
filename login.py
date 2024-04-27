import streamlit as st
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(page_title="𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐩𝐥𝐚𝐧 𝐝𝐞 𝐄𝐬𝐭𝐮𝐝𝐢𝐨𝐬", page_icon=":mortar_board:")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")

# Credenciales de inicio de sesión
User = "41650931"
Password = "cayetano"

# Crear el diseño del formulario de inicio de sesión
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d2b69;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .login-container {
        background-color: #9ee6cf;
        width: 300px;
        padding: 30px;
        border-radius: 20px;
        align-items: center;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .portal-title {
        text-align: center;
        color: #1A4D80;
        margin-bottom: 10px;
        font-size: 80px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image(university_logo, use_column_width=True)
st.markdown(
    "<div class='login-container'><h3 class='portal-title'>𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐩𝐥𝐚𝐧 𝐝𝐞 𝐄𝐬𝐭𝐮𝐝𝐢𝐨𝐬</h3>",
    unsafe_allow_html=True
)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input("User: ", value=User)
    password = st.text_input("Password:", type="password", value=Password)
    submit = st.form_submit_button("Log In")

# Cerrar el div del login-container
st.markdown("</div>", unsafe_allow_html=True)

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == User and password == Password:
        st.success("¡correct user!")
    else:
        st.error("Invalid username or password. Please try again.")












