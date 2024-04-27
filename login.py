import streamlit as st
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(layout="centered")

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
        background-color: #010a1c;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .portal-title {
        text-align: center;
        color: #fcfcfc;
        margin-bottom: 10px;
        font-size: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.image(university_logo, use_column_width=True)
st.markdown("<div class='login-container'><h3 class='portal-title'> 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢̄𝐜𝐮𝐥𝐚 - 𝐔𝐏𝐂𝐇 </h3>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input(" 𝚄𝚜𝚎𝚛: ", value=User)
    password = st.text_input("𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍:", type="password", value=Password)
    submit = st.form_submit_button("𝕃𝕠𝕘 𝕀𝕟")

# Cerrar el div del login-container
st.markdown("</div>", unsafe_allow_html=True)

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == User and password == Password:
        st.success("¡correct user!")
    else:
        st.error("Invalid username or password. Please try again.")
















