import streamlit as st
import os

# Definir credenciales de inicio de sesión
usuario_correcto = "41650931"
contrasenia_correcta = "cayetano"

# Cargar logo de la universidad
logo = st.file_uploader("Carga el logo de UPCH", type=["png", "jpg", "jpeg"])

# Ruta de la imagen de fondo
fondo_path = "tu_ruta_del_fondo.jpg"

# Diseño del formulario de inicio de sesión
st.markdown("""
<div style="background-image: url('{fondo_path}'); background-size: cover; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 0 50px rgba(0, 0, 0, 0.1); width: 1024px; height: 768px;">
    <div style="text-align: center; margin-bottom: 2rem;">
        {'<img src="data:image/png;base64,{}" width="250">'.format(logo.getvalue().decode()) if logo else ""}
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
""".format(fondo_path=fondo_path), unsafe_allow_html=True)

# Función para manejar el inicio de sesión
def handleLogin():
    usuario = st.text_input("Usuario", key="usuario")
    contrasenia = st.text_input("Contraseña", type="password", key="contrasenia")

    if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
        st.success("¡Inicio de sesión exitoso!")
    else:
        st.error("Usuario o contraseña incorrectos.")


    if usuario == usuario_correcto and contrasenia == contrasenia_correcta:
        st.success("¡Inicio de sesión exitoso!")
    else:
        st.error("Usuario o contraseña incorrectos.")
