import streamlit as st
import pandas as pd

# Cargar datos desde el archivo CSV
data = pd.read_csv("database.csv")

# Configurar el diseño de la página
st.set_page_config(page_title="Gestión de Cursos UPCH", page_icon=":books:", layout="wide")

# Bienvenida al estudiante con globos
st.balloons()
st.write("# ¡Bienvenido, Estudiante! 🎈🎉")

# Descripción de la aplicación
st.write("""
## Bienvenido a la Plataforma de Gestión de Cursos de Ingeniería Informática - UPCH

En esta aplicación, podrás explorar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH). Descubre los cursos, sus prerrequisitos y detalles para planificar tu trayectoria académica de manera efectiva.

¡Sumérgete en el mundo de la ingeniería informática y construye tu camino hacia el éxito académico!

""")

# Estilos CSS
hide_table_row_index = """
            <style>
            tbody th {display:none;}
            .blank {display:none;}
            </style>
            """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Función para obtener el color de fondo según el ciclo
def get_bg_color(ciclo):
    colores = {
        "PRIMER": "#F0F8FF",   # Azul claro
        "SEGUNDO": "#E0FFFF",  # Turquesa claro
        "TERCER": "#FAFAD2",   # Amarillo claro
        "CUARTO": "#FAF0E6",   # Lino
        "QUINTO": "#FFF5EE",   # Seashell
        "SEXTO": "#F5F5DC",    # Beige
        "SEPTIMO": "#E6E6FA",  # Lavanda
        "OCTAVO": "#FFF0F5",   # Lavanda rojizo
        "NOVENO": "#F8F8FF",   # Azul fantasma
        "DECIMO": "#F5DEB3"    # Wheat
    }
    return colores.get(ciclo, "")  # Obtener el color correspondiente al ciclo o vacío si no hay coincidencia

# Mostrar los cursos por ciclo con colores personalizados
for ciclo in data["CICLO"].unique():
    cursos = data[data["CICLO"] == ciclo]
    st.subheader(f"{ciclo}")
    st.write(cursos.style.apply(lambda x: [f"background-color: {get_bg_color(ciclo)}"] * len(x), axis=1).to_html(escape=False), unsafe_allow_html=True)

# Nota al pie
st.write("Nota: Los cursos en color tienen prerrequisitos que deben ser aprobados antes de llevarlos.")

