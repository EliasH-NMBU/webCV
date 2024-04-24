from pathlib import Path

import streamlit as st
from PIL import Image

# ------ PATH Settings ------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-3.pdf"
grade_card = current_dir / "assets" / "grade_card.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"








# ------ General Settings ------
PAGE_TITLE = "Portfolio"
PAGE_ICON = "📚"
NAME = "Elias Evjen Hartmark"
DESCRIPTION = "Civil Engineer | Robotics & Cybernetics Engineer | Software & Machine Learning Engineer"
EMAIL = "elias.hartmark@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sourav-sahoo-1b8b3b1a4/",
    "GitHub": "e",
    "IEEE": "https://ieeexplore.ieee.org/author/37086547200"}
PROJECTS = {
    "📚 Chain weight weighing station": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
    "📚 Self driving RC Car": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
    "📚 Model Boat Competition": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
    "📚 Labyrint Robot": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
    "📚 Matlab Drone Robot": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
    "📚 Thorvald Robot Running with Runtime Verification Platform": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
    "📚 Hovercraft Project": "https://www.youtube.com/watch?v=BXAeMICmUSQ",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)




# ------ CSS Styling ------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
with open(grade_card, "rb") as pdf2_file:
    PDFbyte = pdf2_file.read()
profile_pic = Image.open(profile_pic)



# ------ HERO section ------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        )
    st.write(f"📧 {EMAIL}")
    st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/elias-hartmark-robotics/)")
    st.markdown("🔗 [GitHub](https://github.com/EliasH-NMBU)")

# ------ EXPERIENCE & QUALIFICATIONS ------
st.write("#")
st.subheader("Work Experience & Qualifications")
st.write(
    """
    - 🎓 MSc in Applied Robotics, Autonomous Systems and Control (📅 2019 - 2024)
    - 🎓 High School Vestby Videregående Skole, Science Division (📅 2015 - 2018)

    - 🏢 **Robotics Engineer/Researcher** at [NMBU](https://www.sintef.no/en/projects/2022/robofarmer-safe-and-reliable-sensing-learning-and-control-of-an-autonomous-multi-arm-agri-robot-platform/) (📅 2023 - Present)
    - 🏢 **Teaching Assistant, TMP100** at [NMBU](https://www.nmbu.no/emne/TMP100) (📅 2022)
    - 🏢 **Teaching Assistant, TIP100** at [NMBU](https://www.nmbu.no/emne/TMP100) (📅 2022- 2023)
    - 🏢 **Project Manager and Researcher** at [NMBU](https://www.nmbu.no/fakulteter/fakultet-realfag-og-teknologi/eik-lab) (📅 2021 - 2023)
    - 🏢 **Shop Employee** at [Outland](https://www.outland.no/) (📅 2018 - 2020)
    
    - 🏆 **Twice winner of Young Entrepreneur Competition at High School** at [VVS](https://afk.no/vestby-vgs/aktuelt/ungt-entreprenorskap.207574.aspx) (📅 2024)
    """)

# ------ Skills ------
st.write("#")
st.subheader("Skills")
st.write(
    """
    - 🐍 **Programming**: Python, C++, Matlab, Java
    - 🤖 **Robotics**: ROS2, Gazebo, Matlab Robotics Toolbox
    - 📚 **Machine Learning**: PyTorch, TensorFlow, Scikit-learn, OpenCV
    - 📊 **Data Analysis**: Pandas, Numpy, Matplotlib, Seaborn
    - 📝 **Documentation**: LaTeX, Markdown, Word
    - 🧠 **Deep Learning**: CNN, RNN, LSTM
    - 📦 **Tools**: Git, Docker, Jupyter Notebook, VSCode
    - 📡 **IoT**: Raspberry Pi, Arduino, ESP32, I2C, SPI
    - 🌐 **Web Development**: HTML, CSS, JavaScript
    - 🛠️ **CAD Software**: SolidWorks, Fusion 360
    - 📏 **Simulation Software**: Simulink, Rviz
    - 📡 **Communication Protocols**: HTTP, WebSockets
    - 🛠️ **Prototyping**: 3D Printing, Laser Cutting, Soldering, General Machining Skills

    """
)

# ------ Projects ------
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"🔗 [{project}]({link})")