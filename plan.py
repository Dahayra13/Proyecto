# -*- coding: utf-8 -*-
"""Untitled56.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sz2x9ImUCHfZMYMgolIOZCn-G93ZBBJb
"""

import streamlit as st
import pandas as pd

# Cargar datos desde el archivo CSV
data = pd.read_csv("/content/database.csv")

# Mostrar cursos
def show_courses():
    st.markdown("""
        <style>
        body {
            background-color: #FFFAF0; /* Amarillo claro */
            color: #333333; /* Gris oscuro */
        }
        </style>
    """, unsafe_allow_html=True)
    st.title("Gestión de Cursos de Ingeniería Informática - UPCH")

    # Estilos CSS
    hide_table_row_index = """
        <style>
        tbody th {display:none;}
        .blank {display:none;}
        </style>
    """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    # Función para obtener el color de fondo según el ciclo
    def get_bg_color(ciclo, prereq):
        if prereq == "NINGUNO":
            return "#D3D3D3"  # Gris claro
        elif ciclo.startswith("PRIMER"):
            return "#F0F8FF"  # Azul claro
        elif ciclo.startswith("SEGUNDO"):
            return "#E0FFFF"  # Turquesa claro
        elif ciclo.startswith("TERCER"):
            return "#FAFAD2"  # Amarillo claro
        elif ciclo.startswith("CUARTO"):
            return "#FAF0E6"  # Lino
        elif ciclo.startswith("QUINTO"):
            return "#FFF5EE"  # Seashell
        elif ciclo.startswith("SEXTO"):
            return "#F5F5DC"  # Beige
        elif ciclo.startswith("SEPTIMO"):
            return "#E6E6FA"  # Lavanda
        elif ciclo.startswith("OCTAVO"):
            return "#FFF0F5"  # Lavanda rojizo
        elif ciclo.startswith("NOVENO"):
            return "#F8F8FF"  # Azul fantasma
        elif ciclo.startswith("DECIMO"):
            return "#F5DEB3"  # Wheat
        else:
            return ""  # Sin color de fondo

    # Mostrar los cursos por ciclo
    for ciclo in data["CICLO"].unique():
        cursos = data[data["CICLO"] == ciclo]
        st.subheader(f"{ciclo}")
        styled_cursos = cursos.style.apply(lambda value: [f"background-color: {get_bg_color(ciclo, value['PRE REQUISITO'])};color: black;"], axis=1, subset=["PRE REQUISITO"])
        st.write(styled_cursos.to_html(), unsafe_allow_html=True)

    st.write("Nota: Los cursos en color tienen prerrequisitos que deben ser aprobados antes de llevarlos.")

# Iniciar la aplicación
login()

