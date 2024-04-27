import streamlit as st

# Título de la página con el logo de la universidad
st.image('logo_upch.png', use_column_width=True)
st.title('Iniciar sesión')

# Icono de usuario
st.image('user_icon.png', width=100)

# Campo de texto para Nombre de Usuario
username = st.text_input('Nombre de Usuario', placeholder='Ingrese su nombre de usuario', key='username')

# Botón para continuar
if st.button('CONTINUAR', key='continue_btn'):
    # Aquí puedes agregar la lógica para manejar el inicio de sesión

# Enlace para recuperar contraseña
st.write('[¿Olvidaste tu contraseña?](#)', unsafe_allow_html=True)

# Selector de idioma
language = st.selectbox('Selecciona el idioma', ['Español (Latinoamérica)', 'English', 'Otros'])
