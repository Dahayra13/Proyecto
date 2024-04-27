import streamlit as st
import pandas as pd

# Cargar datos desde el archivo CSV
data = pd.read_csv("database.csv")

# Configurar el diseño de la página
st.set_page_config(page_title="Gestión de Cursos UPCH", page_icon=":books:", layout="wide")

# Encabezado y descripción
st.title("Gestión de Cursos de Ingeniería Informática - UPCH")
st.write("Esta aplicación web permite visualizar los cursos de los 10 ciclos de la carrera de Ingeniería Informática en la Universidad Peruana Cayetano Heredia (UPCH), junto con sus prerrequisitos y detalles.")

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
    if ciclo.startswith("PRIMER"):
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
    st.write(cursos.style.apply(lambda x: [f"background-color: {get_bg_color(ciclo)}"] * len(x), axis=1).to_html(), unsafe_allow_html=True)

# Nota al pie
st.write("Nota: Los cursos en color tienen prerrequisitos que deben ser aprobados antes de llevarlos.")

