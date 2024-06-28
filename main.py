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
import matplotlib.pyplot as plt

def main():
    # Configuración de la página
    st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

    # Cargar el logotipo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo_upch.png")
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    # Credenciales de inicio de sesión
    User = "0000"
    Password = "0000"

    # Verificar si el usuario ha iniciado sesión
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    set_background()

    # Mostrar la pantalla de inicio de sesión si el usuario no ha iniciado sesión
    if not st.session_state.logged_in:
        login(encoded_logo, User, Password)
    else:
        # Crear la aplicación multiapp
        app = MultiApp()
        app.add_app("Inicio", home_app)
        app.add_app("Modelar Salones", modelar_salones_app)
        app.add_app("Modelar Ambientes", modelar_ambientes_app)
        app.add_app("Modelar Cursos", modelar_cursos_app)
        app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
        app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
        app.add_app("Optimización de Horarios", optimizar_horarios_app)

        # Ejecutar la aplicación multiapp
        selected_app = st.sidebar.selectbox("Selecciona una sección", [app_info['title'] for app_info in app.apps])
        for app_info in app.apps:
            if app_info['title'] == selected_app:
                app_info['function']()
                break

    # Cambiar el tipo de letra a Times New Roman
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.size"] = 14

if __name__ == "__main__":
    main()
