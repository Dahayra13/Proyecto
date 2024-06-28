import streamlit as st
from multiapp import MultiApp
from login import login, set_background
from apps import (
    home_app,
    modelar_salones_app,
    modelar_ambientes_app,
    modelar_cursos_app,
    requerimiento_ambientes_app,
    asignacion_alumnos_app,
    optimizar_horarios_app
)
import os
import base64
import matplotlib.pyplot as plt
import numpy as np

def set_pastel_colors(ax):
    colors = ['#F7CAC9', '#92A8D1', '#FFBF00', '#98FB98', '#ADD8E6', '#FFB6C1']
    ax.set_prop_cycle(color=colors)

def main():
    st.set_page_config(layout="wide", initial_sidebar_state='collapsed', page_title="Gestión de Cursos UPCH")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "logo_upch.png")

    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

    User = "0000"  # Tu usuario
    Password = "0000"  # Tu contraseña

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    set_background()

    app = MultiApp()
    app.add_app("Inicio", home_app)
    app.add_app("Modelar Salones", modelar_salones_app)
    app.add_app("Modelar Ambientes", modelar_ambientes_app)
    app.add_app("Modelar Cursos", modelar_cursos_app)
    app.add_app("Requerimiento de Ambientes", requerimiento_ambientes_app)
    app.add_app("Asignación de Alumnos", asignacion_alumnos_app)
    app.add_app("Optimizar Horarios", optimizar_horarios_app)

    app.run()

    # Cambiar el tipo de letra
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.size"] = 12

    # Modificar los gráficos por cada ciclo con colores pastel
    fig, ax = plt.subplots(figsize=(8, 6))
    set_pastel_colors(ax)
    labels = ['Ciclo 1', 'Ciclo 2', 'Ciclo 3', 'Ciclo 4', 'Ciclo 5', 'Ciclo 6']
    values = [10, 15, 12, 18, 8, 14]
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.set_title('Distribución de Cursos por Ciclo')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
