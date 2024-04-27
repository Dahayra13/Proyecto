import streamlit as st
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(layout="centered")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")
lock_image = Image.open("universidad.jpg")  # Carga la imagen del candado

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
    .form-field {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .form-field label {
        font-size: 16px;
        font-weight: bold;
        color: #fcfcfc;
        margin-right: 10px;
    }
    .form-field input {
        flex: 1;
        padding: 10px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
    }
    .form-field img {
        width: 24px;
        height: 24px;
        margin-left: 10px;
    }
    .submit-button {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 5px;
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
st.markdown("<div class='login-container'><h3 class='portal-title'> 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢̄𝐜𝐮𝐥𝐚 - 𝐔𝐏𝐂𝐇 </h3>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    with st.container():
        with st.container():
            username_container = st.container()
            with username_container:
                st.markdown("<div class='form-field'>", unsafe_allow_html=True)
                st.markdown("<label> 𝚄𝚜𝚎𝚛: </label>", unsafe_allow_html=True)
                username = st.text_input(" ", value=User, label_visibility="collapsed")
                st.image(lock_image, use_column_width=False)
                st.markdown("</div>", unsafe_allow_html=True)
    with st.container():
        password_container = st.container()
        with password_container:
            st.markdown("<div class='form-field'>", unsafe_allow_html=True)
            st.markdown("<label>𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍:</label>", unsafe_allow_html=True)
            password = st.text_input(" ", type="password", value=Password, label_visibility="collapsed")
            st.image(lock_image, use_column_width=False)
            st.markdown("</div>", unsafe_allow_html=True)
    submit = st.form_submit_button("𝕃𝕠𝕘 𝕀𝕟")

# Cerrar el div del login-container
st.markdown("</div>", unsafe_allow_html=True)

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == User and password == Password:
        st.success("¡correct user!")
    else:
        st.error("Invalid username or password. Please try again.")

















