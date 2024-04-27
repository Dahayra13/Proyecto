# -- coding: utf-8 --
import streamlit as st
import os

# Definir credenciales de inicio de sesión
usuario_correcto = "41650931"
contrasenia_correcta = "cayetano"

# Cargar datos desde el archivo CSV
data = pd.read_csv("database.csv")

# Función para autenticar al usuario
def authenticate(username_entered, password_entered):
    if username_entered == usuario_correcto and password_entered == contrasenia_correcta:
        return True
    else:
        return False

# Cargar logo de la universidad
logo_path =  "Logo_upch.png"
if os.path.exists(logo_path):
    logo = st.image(logo_path, width=300, use_column_width=False)
else:
    st.error("No se encontró el archivo de logo de la universidad.")

# Ejecutar la aplicación
if __name__ == '__main__':
    st.markdown("""
    <div style="background-color: #ffffff; padding: 2rem; border-radius: 0.7rem; box-shadow: 0 1024px 768x rgba(0, 0, 0, 0.1); max-width: 600px; margin: auto;">
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 style="color: #ad1c2d;">𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐚𝐥 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢𝐜𝐮𝐥𝐚</h1>
            <p style="color: #0d0c0c;">Aᴄᴄᴇsᴏ ᴀᴜᴛᴏʀɪᴢᴀᴅᴏ ᴀʟ ᴄᴜʀʀɪ́ᴄᴜʟᴏ ᴀᴄᴀᴅᴇ́ᴍɪᴄᴏ</p>
        </div>
        <form>
            <div class="form-group">
                <label for="usuario" style="color: #030303;">𝚄𝚂𝚄𝙰𝚁𝙸𝙾:</label>
                <input type="text" class="form-control" id="usuario" placeholder="Ingrese su usuario" style="width: 100%; padding: 0.7rem; margin-bottom: 1rem;" required>
            </div>
            <div class="form-group">
                <label for="contrasenia" style="color: #030303;">𝙲𝙾𝙽𝚃𝚁𝙰𝚂𝙴𝙽̃𝙰:</label>
                <input type="password" class="form-control" id="contrasenia" placeholder="Ingrese su contraseña" style="width: 100%; padding: 0.5rem; margin-bottom: 1rem;" required>
            </div>
            <div class="form-group" style="text-align: center;">
                <button type="button" class="btn btn-primary" onclick="handleLogin()" style="padding: 0.5rem 2rem; background-color: #9c2121; color: grey; border: none; border-radius: 0.3rem;">𝐈𝐧𝐢𝐜𝐢𝐚𝐫 𝐬𝐞𝐬𝐢𝐨́𝐧</button>
            </div>
        </form>
        <div id="result-message" style="color: red; text-align: center; margin-top: 1rem;"></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

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





   
