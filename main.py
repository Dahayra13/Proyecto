import streamlit as st
from multiapp import MultiApp
from login import login, set_background
from home import app as home_app
from modelar_salones import app as modelar_salones_app
from modelar_ambientes import app as modelar_ambientes_app
from modelar_cursos import app as modelar_cursos_app
from requerimiento_ambientes import app as requerimiento_ambientes_app
from asignacion_alumnos import app as asignacion_alumnos_app
from optimizar_horarios import app as optimizar_horarios_app
import os
import base64

def main():
    # Configurar la página de Streamlit
    st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

    # Cargar y codificar el logo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo_upch.png")
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    # Definir credenciales
    User = "0000"
    Password = "0000"

    # Inicializar estado de sesión
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Establecer fondo
    set_background()

    # Verificar si se ha iniciado sesión
    if not st.session_state.logged_in:
        # Iniciar sesión
        login(encoded_logo, User, Password)
    else:
        # Mostrar aplicación
        app = MultiApp()
        app.add_apps()
        selected_app = st.sidebar.selectbox("Selecciona una sección", [app['title'] for app in app.apps])
        for app_page in app.apps:
            if app_page['title'] == selected_app:
                app_page['function']()
                break

if __name__ == "__main__":
    main()

