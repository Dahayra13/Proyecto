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
import numpy as np

# Lista de colores pastel
colores_pastel = ['#FFD1DC', '#B19CD9', '#FFCBA4', '#B2EC5D', '#A2DFFF']

def main():
    st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

    # CSS para cambiar el tipo de letra a Times New Roman
    st.markdown(
        """
        <style>
        body {
            font-family: 'Times New Roman', Times, serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo_upch.png")

    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    User = "0000"  # Tu usuario
    Password = "0000"  # Tu contraseña

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    set_background()

    if not st.session_state.logged_in:
        login(encoded_logo, User, Password)
    else:
        app = MultiApp()

        app.add_app("Home", home_app)
        app.add_app("Modelar Salones", modelar_salones_app)
        app.add_app("Modelar Ambientes", modelar_ambientes_app)
        app.add_app("Modelar Cursos", modelar_cursos_app)
        app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
        app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
        app.add_app("Optimización de Horarios", optimizar_horarios_app)

        selected_app = st.sidebar.selectbox("Selecciona una sección", [app['title'] for app in app.apps])

        for app_page in app.apps:
            if app_page['title'] == selected_app:
                app_page['function']()
                break

        # Ejemplo de gráfico de barras con colores pastel
        def grafico_ejemplo():
            datos = np.random.randint(1, 10, size=5)
            etiquetas = ['A', 'B', 'C', 'D', 'E']
            
            fig, ax = plt.subplots()
            ax.bar(etiquetas, datos, color=colores_pastel)
            ax.set_xlabel('Etiquetas')
            ax.set_ylabel('Datos')
            ax.set_title('Gráfico con colores pastel')
            
            st.pyplot(fig)

        # Llamamos a la función del gráfico de ejemplo
        grafico_ejemplo()

if __name__ == "__main__":
    main()
