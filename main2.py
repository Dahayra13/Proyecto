import streamlit as st
import pandas as pd

# Configurar el diseño de la página
st.set_page_config(page_title="Gestión de Cursos UPCH", page_icon="🎓", layout="wide")

# Cargar datos desde el archivo CSV
data = pd.read_csv("database.csv")

# Credenciales de acceso
username = "41650931"
password = "cayetano"

# Función para autenticar al usuario
def authenticate(username_entered, password_entered):
    if username_entered == username and password_entered == password:
        return True
    else:
        return False

# Página de inicio de sesión
def login():
    st.markdown("""
        <style>
        body {
            background-color: #F8F8FF; /* Azul fantasma */
            color: #333333; /* Gris oscuro */
        }
        </style>
    """, unsafe_allow_html=True)
    st.title("Inicio de Sesión - UPCH")
    username_entered = st.text_input("Usuario", key="username")
    password_entered = st.text_input("Contraseña", type="password", key="password")
    if st.button("Ingresar"):
        if authenticate(username_entered, password_entered):
            st.success("Inicio de sesión exitoso")
            show_courses()
        else:
            st.error("Credenciales incorrectas")

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
