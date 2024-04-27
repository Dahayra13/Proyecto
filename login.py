import streamlit as st
from PIL import Image

# Configurar el diseño de la página
st.set_page_config(layout="centered")

# Cargar la imagen de la insignia de la universidad
university_logo = Image.open("Logo_upch.png")

# Credenciales de inicio de sesión
User = "41650931"
Password = "cayetano"

# Cargar datos desde el archivo CSV
data = pd.read_csv("database.csv")

# Crear el diseño del formulario de inicio de sesión
st.markdown(
    """
    <style>
    .stApp {
        background-color: #010a1c;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .portal-title {
        text-align: center;
        color: #fcfcfc;
        margin-bottom: 10px;
        font-size: 25px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.image(university_logo, use_column_width=True)
st.markdown("<div class='login-container'><h3 class='portal-title'> 🎓 𝐏𝐨𝐫𝐭𝐚𝐥 𝐝𝐞 𝐌𝐚𝐭𝐫𝐢̄𝐜𝐮𝐥𝐚 - 𝐔𝐏𝐂𝐇 </h3>", unsafe_allow_html=True)

# Crear los campos de usuario y contraseña
with st.form(key="login_form"):
    username = st.text_input(" 𝚄𝚜𝚎𝚛: ", value=User)
    password = st.text_input("𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍:", type="password", value=Password)
    submit = st.form_submit_button("𝕃𝕠𝕘 𝕀𝕟")

# Cerrar el div del login-container
st.markdown("</div>", unsafe_allow_html=True)

# Verificar las credenciales y mostrar un mensaje de éxito o error
if submit:
    if username == User and password == Password:
        st.success("¡correct user!")
    else:
        st.error("Invalid username or password. Please try again.")


#########################################################################################
st.balloons()  # Agregar globos de fiesta para hacer la bienvenida más didáctica
            
            # Mostrar la página de visualización de cursos
            st.title("Gestión de Cursos de Ingeniería Informática - UPCH")
            st.write("A continuación, podrás visualizar tu plan de estudios desde el primer hasta el décimo ciclo.")

            # Mostrar los cursos por ciclo
            for ciclo in data["CICLO"].unique():
                cursos = data[data["CICLO"] == ciclo]
                st.subheader(f"{ciclo}")
                st.write(cursos.style.apply(lambda x: [f"background-color: {get_bg_color(ciclo)}"] * len(x), axis=1).to_html(), unsafe_allow_html=True)

            # Sección de gráfico de prerrequisitos
            st.subheader("Visualización de Prerrequisitos")
            st.write("A continuación, se muestra un gráfico que ilustra las relaciones de prerrequisitos entre los cursos.")

            # Generar el gráfico de prerrequisitos
            G = nx.DiGraph()
            for _, row in data.iterrows():
                curso = row["CURSO"]
                prerequisitos = row["PREREQUISITOS"].split(", ")
                G.add_node(curso)
                for p in prerequisitos:
                    G.add_edge(p, curso)

            # Mostrar el gráfico de prerrequisitos
            fig, ax = plt.subplots(figsize=(12, 8))
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_color="#1A4D80", edge_color="#1A4D80", font_color="white", ax=ax)
            st.pyplot(fig)

            # Nota al pie
            st.write("Nota: Los cursos en colores tienen prerrequisitos que deben ser aprobados antes de llevarlos.")
        else:
            st.error("Invalid username or password. Please try again.")
else:
    # Si el usuario ya ha iniciado sesión, redirigir directamente a la página de visualización de cursos
    st.title("Gestión de Cursos de Ingeniería Informática - UPCH")
    st.write("A continuación, podrás visualizar tu plan de estudios desde el primer hasta el décimo ciclo.")

    # Mostrar los cursos por ciclo
    for ciclo in data["CICLO"].unique():












