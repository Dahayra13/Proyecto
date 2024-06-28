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

    # Cargar y codificar el logo de la UPCH
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo_upch.png")
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    # Definir las credenciales de usuario y contraseña
    User = "0000"  # Tu usuario
    Password = "0000"  # Tu contraseña

    # Inicializar el estado de sesión de inicio de sesión
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # Establecer el fondo de la aplicación
    set_background()

    # Verificar si el usuario ha iniciado sesión
    if not st.session_state.logged_in:
        # Si no ha iniciado sesión, llamar a la función de inicio de sesión
        login(encoded_logo, User, Password)
    else:
        # Si ya ha iniciado sesión, mostrar la aplicación
        app = MultiApp()

        # Agregar las diferentes secciones de la aplicación
        app.add_app("Home", home_app)
        app.add_app("Modelar Salones", modelar_salones_app)
        app.add_app("Modelar Ambientes", modelar_ambientes_app)
        app.add_app("Modelar Cursos", modelar_cursos_app)
        app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
        app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
        app.add_app("Optimización de Horarios", optimizar_horarios_app)

        # Mostrar el menú desplegable en la barra lateral para seleccionar la sección
        selected_app = st.sidebar.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

        # Ejecutar la sección seleccionada
        for app_page in app.apps:
            if app_page['title'] == selected_app:
                app_page['function']()
                break

if __name__ == "__main__":
    main()


