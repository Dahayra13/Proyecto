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
logo_path = "Logo_upch.png"
if os.path.exists(logo_path):
    logo = st.image(logo_path, width=250, use_column_width=False)
else:
    st.error("No se encontró el archivo de logo de la universidad.")

# Cargar imagen de usuario
st.write("icono.png:")
usuario_image = st.file_uploader("icono.png", type=["png", "jpg", "jpeg"])

# Diseño mejorado del formulario de inicio de sesión
st.markdown("""
<div style="background-color: #f8f9fa; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 1024px 768x rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto;">
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #ad1c2d;">Bienvenido al Portal de Matrícula UPCH</h1>
        <p style="color: #1c1b1c;">Inicia sesión para acceder a la aplicación</p>
    </div>
    <form>
        <div class="form-group">
            <label for="usuario" style="color: #262424;">USUARIO</label>
            <input type="text" class="form-control" id="USUARIO" placeholder="Ingrese su usuario" style="width: 100%; padding: 0.5rem; margin-bottom: 1rem;" required>
        </div>
        <div class="form-group">
            <label for="contrasenia" style="color: #262424;">CONTRASEÑA</label>
            <input type="password" class="form-control" id="contrasenia" placeholder="Ingrese su contraseña" style="width: 100%; padding: 0.5rem; margin-bottom: 1rem;" required>
        </div>
        <div class="form-group" style="text-align: center;">
            <button type="button" class="btn btn-primary" onclick="handleLogin()" style="padding: 0.5rem 2rem; background-color: #ad1c2d; color: white; border: none; border-radius: 0.3rem;">Iniciar Sesión</button>
        </div>
    </form>
</div>
""", unsafe_allow_html=True)

# Función para manejar el inicio de sesión
def handleLogin():
    usuario = st.text_input("Usuario", key="usuario")
    contrasenia = st.text_input("Contraseña", type="password", key="contrasenia")

    if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
        st.success("¡Inicio de sesión exitoso!")
    else:
        st.error("Usuario o contraseña incorrectos.")

