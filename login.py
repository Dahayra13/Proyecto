# -- coding: utf-8 --
import streamlit as st
import os

# Credenciales de inicio de sesión
usuario_correcto = "41650931"
contrasenia_correcta = "cayetano"

# Función para autenticar al usuario
def authenticate(username_entered, password_entered):
    if username_entered == usuario_correcto and password_entered == contrasenia_correcta:
        return True
    else:
        return False

# Cargar logo de la universidad
logo_path = "Logo_upch.png"
if os.path.exists(logo_path):
    logo = st.image(logo_path, width=300, use_column_width=False)
else:
    st.error("No se encontró el archivo de logo de la universidad.")

# Diseño mejorado del formulario de inicio de sesión
st.markdown("""
<div style="background-color: #d6eb9d; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 1024px 768x rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto;">
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #ad1c2d;">𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐚𝐥 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢𝐜𝐮𝐥𝐚</h1>
        <p style="color: #0d0c0c;">Aᴄᴄᴇsᴏ ᴀᴜᴛᴏʀɪᴢᴀᴅᴏ ᴀʟ ᴄᴜʀʀɪ́ᴄᴜʟᴏ ᴀᴄᴀᴅᴇ́ᴍɪᴄᴏ</p>
    </div>
    <form>

# Ejecutar la aplicación
if __name__ == '__main__':
    # Obtener las credenciales del usuario
    username = st.text_input("Usuario", "", placeholder="Ingrese su usuario")
    password = st.text_input("Contraseña", "", type="password", placeholder="Ingrese su contraseña")

    # Autenticar al usuario
    if st.button("Iniciar sesión"):
        if authenticate(username, password):
            st.success("¡Inicio de sesión exitoso!")
        else:
            st.error("Usuario o contraseña incorrectos.")



   
