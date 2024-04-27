# -- coding: utf-8 --
"""Untitled56.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sz2x9ImUCHfZMYMgolIOZCn-G93ZBBJb
"""
import streamlit as st
import os

# Definir credenciales de inicio de sesión
usuario_correcto = "41650931"
contrasenia_correcta = "cayetano"

# Cargar logo de la universidad
logo_path =  "Logo_upch.png"
if os.path.exists  (logo_path):
    logo = st.image (logo_path, width = 300, use_column_width = False)
else:
    st.error("No se encontró el archivo de logo de la universidad.")

# Función para autenticar al usuario
def authenticate(username_entered, password_entered):
    if username_entered == usuario_correcto and password_entered == contrasenia_correcta:
        return True
    else:
        return False

# Ejecutar la aplicación
if __name__ == '__main__':
    st.markdown("""
    <div style="background-color: #d6eb9d; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 1024px 768x rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto;">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #ad1c2d;">𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐚𝐥 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢𝐜𝐮𝐥𝐚</h1>
            <p style="color: #0d0c0c;">Aᴄᴄᴇsᴏ ᴀᴜᴛᴏʀɪᴢᴀᴅᴏ ᴀʟ ᴄᴜʀʀɪ́ᴄᴜʟᴏ ᴀᴄᴀᴅᴇ́ᴍɪᴄᴏ</p>
        </div>
        <form>
            <div class="form-group">
                <label for="usuario" style="color: #030303;">𝚄𝚂𝚄𝙰𝚁𝙸𝙾:</label>
                <input type="text" class="form-control" id="usuario" placeholder="Ingrese su usuario" style="width: 100%; padding: 0.7rem; margin-bottom: 1rem;" required>
            </div>
            <div class="form-group">
                <label for="contrasenia" style="color: #030303;">𝙲𝙾𝙽𝚃𝚁𝙰𝚂𝙴𝙽̃𝙰:</label>
                <input type="password" class="form-control" id="contrasenia" placeholder="Ingrese su contraseña" style="width: 100%; padding: 0.5rem; margin-bottom: 1rem;" required>
            </div>
            <div class="form-group" style="text-align: center;">
                <button type="button" class="btn btn-primary" onclick="handleLogin()" style="padding: 0.5rem 2rem; background-color: #9c2121; color: grey; border: none; border-radius: 0.3rem;">𝐈𝐧𝐢𝐜𝐢𝐚𝐫 𝐬𝐞𝐬𝐢𝐨́𝐧</button>
            </div>
        </form>
        <div id="result-message" style="color: red; text-align: center; margin-top: 1rem;"></div>
    </div>
    """, unsafe_allow_html=True)

    username_entered = st.text_input("Usuario", "")
    password_entered = st.text_input("Contraseña", "", type="password")

    if st.button("Iniciar sesión"):
        if authenticate(username_entered, password_entered):
            st.markdown('<div id="result-message" style="color: green; text-align: center; margin-top: 1rem;">Inicio de sesión exitoso.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div id="result-message" style="color: red; text-align: center; margin-top: 1rem;">Credenciales incorrectas. Por favor, inténtalo de nuevo.</div>', unsafe_allow_html=True)




   
