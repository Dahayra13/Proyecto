# -- coding: utf-8 --
import streamlit as st
import os

# Definir credenciales de inicio de sesión
usuario_correcto = "41650931"
contrasenia_correcta = "cayetano"

# Función para autenticar al usuario
def authenticate(username_entered, password_entered):
    if username_entered == usuario_correcto and password_entered == contrasenia_correcta:
        return True
    else:
        return False

# Cargar logo de la universidad
logo_path =  "Logo_upch.png"
if os.path.exists(logo_path):
    logo = st.image(logo_path, width=300, use_column_width=False)
else:
    st.error("No se encontró el archivo de logo de la universidad.")

# Ejecutar la aplicación
if __name__ == '__main__':
    st.markdown("""
    <div style="background-color: #ffffff; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 1024px 768x rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto;">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #ad1c2d;">𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢𝐜𝐮𝐥𝐚</h1>
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
    </div>
    """, unsafe_allow_html=True)

 # Autenticar al usuario
    if st.button("Iniciar sesión"):
        if authenticate(username, password):
            st.success("¡Inicio de sesión exitoso!")
            st.markdown("""
            <div style="text-align: center; margin-top: 2rem;">
                <h2 style="color: #ad1c2d;">¡Bienvenido a tu Portal de Matrícula!</h2>
                <p style="color: #0d0c0c;">Aquí podrás visualizar tu historial académico y los cursos que has llevado desde el primer ciclo hasta el décimo.</p>
            </div>
            """, unsafe_allow_html=True)
            # Aquí puedes agregar el código para mostrar los cursos y el historial académico
        else:
            st.error("Usuario o contraseña incorrectos.")

