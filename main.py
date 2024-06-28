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
    # Establece la configuración de la página
    st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

    # Carga el logotipo de la UPCH
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo_upch.png")
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    # Credenciales de inicio de sesión
    User = "0000"
    Password = "0000"

    # Verifica si el usuario ha iniciado sesión
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    set_background()

    # Si el usuario no ha iniciado sesión, muestra la pantalla de inicio de sesión
    if not st.session_state.logged_in:
        login(encoded_logo, User, Password)
    else:
        # Crea una aplicación MultiApp
        app = MultiApp()

        # Agrega las secciones de la aplicación
        app.add_app("Home", home_app)
        app.add_app("Modelar Salones", modelar_salones_app)
        app.add_app("Modelar Ambientes", modelar_ambientes_app)
        app.add_app("Modelar Cursos", modelar_cursos_app)
        app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
        app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
        app.add_app("Optimización de Horarios", optimizar_horarios_app)

        # Permite al usuario seleccionar la sección que desea ver
        selected_app = st.sidebar.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

        # Muestra la sección seleccionada
        for app_page in app.apps:
            if app_page['title'] == selected_app:
                app_page['function']()
                break

if __name__ == "__main__":
    main()

