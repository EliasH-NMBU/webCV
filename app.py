from pathlib import Path

import streamlit as st
from PIL import Image

# ------ PATH Settings ------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-3.pdf"
grade_card = current_dir / "assets" / "grade_card.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"
gif_path = "assets/Barrel_roll.gif"








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




# ------ HERO section ------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(str(profile_pic), width=230)

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
    """)

st.write("""    
    - 🏆 **Twice winner of Young Entrepreneur Competition at High School** at [VVS](https://afk.no/vestby-vgs/aktuelt/ungt-entreprenorskap.207574.aspx) (📅 2024)
    """)

st.markdown("🏢 **Robotics Engineer/Researcher | NMBU**", unsafe_allow_html=True)
st.write("05/2023 - Present")
st.write(
    """
    - ► Done in collaboration with Robofarmer, PhD candidate Mustafa Adam, Master candidate Tage Andersen and NMBU.
    - ► Head researcher and developer of RV (runtime verification) platform, with the use of software developed by NASA (FRET & OGMA).
    - ► Skills used: ROS2, Python, Javascript, Linux, CSS, Flask, FRET, OGMA, Formal Methods, Websockets, Temporal Logic.
    """)

st.markdown("🏢 **Teaching Assistant, TIP100 | NMBU**", unsafe_allow_html=True)
st.write("01/2022 - 12/2023")
st.write(
    """
    - ► TIP100 stands for Industrial Innovation and Technology, and is a course teached at NMBU.
    - ► I was responsible for teaching the students how to use Peter Corkes robotics package for Matlab.
    - ► Skills used: Matlab, Kinematics, Peter Corke Robotics Toolbox, Path Planning Algorythms.
    """)

st.markdown("🏢 **Project Manager and Researcher | Eik Lab, NMBU**", unsafe_allow_html=True)
st.write("02/2021 - 10/2023")
st.write(
    """
    - ► Eik Lab is a student driven lab at NMBU, where students can work on projects of their own choice. Here I engaged myself in multiple projects.
    - ► Of the projects I was involved in, the most notable ones were a self drivable RC car, built with the use of machine learning and a Steel Chain weighing station for automotive vehicles.
    - ► Skills used: Python, Machine Learning, Tensorflow, PyTorch, C++, Arduino, Raspberry Pi, JavaScript, SolidWorks, Fusion 360, 3D Printing, Laser Cutting, Soldering, General Machining Skills.
    """)

st.markdown("🏢 **Teaching Assistant, TMP100 | NMBU**", unsafe_allow_html=True)
st.write("08/2022-12/2022")
st.write(
    """
    - ► TMP stands for Mechanical Engineering and Process Technology. I was asked to teaching and planning this course for the students of 2022.
    - ► My management of this course required me to have full control of the electrical wirering, acquisition of parts, and the teaching of CAD, 3d printing and laser cutting tools.
    - ► Skills used: BOM list, CAD, 3D Printing, Laser Cutting, Soldering, General Machining Skills, Datasheet Reading.
    """)

st.markdown("🏢 **Shop Employee | Outland Oslo**", unsafe_allow_html=True)
st.write("2018 - 2020")
st.write(
    """
    - ► Outland is a shop that sells board games, card games, roleplaying games, and other related items.
    - ► In this job I was entrusted with responsibility of a product group, and I was used as an expert on the topic of board games. My job was to help customers, control inventory, and to help with the weekly events that happened.
    - ► Skills used: Customer Service, Inventory Control, Event Planning.
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

# Iterate over each project and display it with a GIF and link in two columns
for i, (project, link) in enumerate(PROJECTS.items(), start=1):
    col1, col2 = st.columns(2)  # Divide into two columns
    with col1:
        # Load and display the GIF for the project
        st.image(gif_path, caption=f"{project} GIF", use_column_width='always')
    with col2:
        # Display the link for the project
        st.markdown(f"🔗 [{project}]({link})")

    # Add a horizontal rule between each project (except for the last one)
    if i < len(PROJECTS):
        st.write("---")
