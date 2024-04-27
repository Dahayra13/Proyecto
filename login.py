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

# Mostrar información del alumno
    st.markdown("<h2 style='text-align: center; color: #fcfcfc;'>¡Bienvenido, Estudiante!</h2>", unsafe_allow_html=True)
    
    # Obtener los datos del alumno desde el archivo CSV
    student_data = data[data['ID'] == int(username)]
    
    # Mostrar el plan de estudios del alumno
    st.markdown("<h3 style='color: #fcfcfc;'>Plan de Estudios</h3>", unsafe_allow_html=True)
    for ciclo in range(1, 11):
        materias = student_data[f'Ciclo {ciclo}'].dropna().tolist()
        if materias:
            st.markdown(f"<h4 style='color: #fcfcfc;'>Ciclo {ciclo}</h4>", unsafe_allow_html=True)
            for materia in materias:
                st.write(f"- {materia}")
    
    # Mostrar la plantilla de grafos
    st.markdown("<h3 style='color: #fcfcfc;'>Plantilla de Grafos</h3>", unsafe_allow_html=True)
    st.image("https://d41chssnpqdne.cloudfront.net/user_upload_by_module/chat_bot/files/982946/UmvaSdeIctqoSwrX.jpg?Expires=1715458372&Signature=c4eF7nmi7LjjeHJ80Cdd8xFuWCyGeumjSGlpyrXoWdzVss4SCJOhiKyaSGUY6g9hkABV48UPDtESXipdenZSGtaxE~iF5w0Btj1DhcrsNz2G1ui2q67wyt~pBv12Ve6Z8mfQRW0fi3Y3F3BnIdGt8g-eUTSNHmQS6DCluuSKD78uy15fDZ1nIO44CCewwnU2Esbn1CWjh0RCdid8RlN33tsEI21tC4zIxgJMV0wpclYhbImmgQ0NougBm1EaEUSCWcHu9l79ifS5Aa2CWnNJGWWwFIWSLM8D20Cpv8D8eBFXwBVCfEi~WiHlKyzOnlS-J6rc5Q5Gg38dWdFCI9hcAQ__&Key-Pair-Id=K3USGZIKWMDCSX", use_column_width=True)











