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



   
