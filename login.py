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
    
# Ruta de la imagen de fondo
fondo_path = "universidad.jpg"

# Diseño del formulario de inicio de sesión
st.markdown("""
<div style="background-color: #f8f9fa; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 0 50px rgba(0, 0, 0, 0.1); width: 1024px; height: 768px;">
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="color: #ad1c2d;">Bienvenido a UPCH</h1>
        <p style="color: #1c1b1c;">Inicia sesión para acceder a la aplicación</p>
    </div>
    <form action="javascript:void(0);">
        <div class="form-group">
            <label for="usuario" style="color: #262424;">USUARIO</label>
            <input type="text" class="form-control" id="USUARIO" placeholder="Ingrese su usuario" required>
        </div>
        <div class="form-group">
            <label for="contrasenia" style="color: #262424;">CONTRASEÑA</label>
            <input type="password" class="form-control" id="contrasenia" placeholder="Ingrese su contraseña" required>
        </div>
        <div class="form-group" style="text-align: center;">
            <button type="submit" class="btn btn-primary" onclick="handleLogin()">Iniciar Sesión</button>
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

