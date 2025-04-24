from pathlib import Path

import streamlit as st
from PIL import Image
import itertools
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(
    page_title="Elias E. Hartmark, MSc Robotocist and Fabricator",
    page_icon="assets/favicon.ico",
)

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("assets/background.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ------ PATH Settings ------
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-6.pdf"
grade_card = current_dir / "assets" / "grade_card.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# ------ General Settings ------
PAGE_TITLE = "Elias E. Hartmark, MSc Robotocist and Fabricator"
PAGE_ICON = "assets/favicon.ico"
NAME = "Elias Evjen Hartmark"
DESCRIPTION = "Civil Engineer | Robotics & Cybernetics Engineer | Software & Machine Learning Engineer"
EMAIL = "elias.hartmark@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sourav-sahoo-1b8b3b1a4/",
    "GitHub": "https://github.com/EliasH-NMBU",
    "IEEE": "https://ieeexplore.ieee.org/author/37086547200"}
PROJECTS = {
    "📚 Labyrint Robot": "assets/robotimrt.gif",
    "📚 Self Driving RC Car, Machine Learning": "assets/selfcar.gif",
    "📚 Steel Chain Weighing/Pawn Station": "assets/weight.gif",
    "📚 Model Boat - Ocean Space Race": "assets/boatrace.gif",
    "📚 Matlab Drone, Matlab Simulink": "assets/Barrel_roll.gif", 
    "📚 Hovercraft Project": "assets/hover.gif",
    "📚 Runtime Verification Field Work": "assets/throvaldshort.gif",
    "📚 Eyemech System": "assets/eyemech.gif",
}


# ------ CSS Styling ------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



# ------ HERO section ------
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(str(profile_pic), width=130, use_container_width=True, caption="Me")


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
st.markdown('<div class="titlesection-header"><div style="text-align: center;"><b>Work Experience & Qualifications</b></div></div>', unsafe_allow_html=True)

with stylable_container(
    key="education",
    css_styles=["""
        .stMarkdown{
            font-size: 28px;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        """,
    ]
):

    st.markdown("<p><strong>🎓 MSc in Applied Robotics, Autonomous Systems and Control</strong> (📅 2019 - 2024)</p> <p><strong>🎓 High School Vestby Videregående Skole, Science Division</strong> (📅 2015 - 2018)</p>", unsafe_allow_html=True)


st.markdown(
    '''
    <div style="text-align: center;">
        🏆 <strong>Twice winner of Young Entrepreneur Competition at High School</strong> at 
        <a href="https://afk.no/vestby-vgs/aktuelt/ungt-entreprenorskap.207574.aspx" target="_blank">VVS</a> (📅 2015, 2018)
    </div>
    ''',
    unsafe_allow_html=True
)
st.write("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="titlesection-header"><div style="text-align: center;"> <b>Robotics Engineer/Researcher | NMBU</b></div></div>',
    unsafe_allow_html=True
)
st.write('<div class="timeline"><div style="text-align: center;">05/2023 - Present</div></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="text">
        <ul>
            <li> Done in collaboration with Robofarmer, PhD candidate Mustafa Adam, Master candidate Tage Andersen and NMBU.</li>
            <li>► Head researcher and developer of RV (runtime verification) platform, with the use of software developed by NASA (FRET & OGMA).</li>
            <li>► Skills used: ROS2, Python, Javascript, Linux, CSS, Flask, FRET, OGMA, Formal Methods, Websockets, Temporal Logic.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("<br>", unsafe_allow_html=True)


st.markdown(
    '<div class="titlesection-header"><div style="text-align: center;"> <b>Teaching Assistant, TIP100 | NMBU</b></div></div>',
    unsafe_allow_html=True
)
st.write('<div class="timeline"><div style="text-align: center;">01/2022 - 12/2023</div></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="text">
        <ul>
            <li>► TIP100 stands for Industrial Innovation and Technology, and is a course teached at NMBU.</li>
            <li>► I was responsible for teaching the students how to use Peter Corke’s robotics package for Matlab.</li>
            <li>► Skills used: Matlab, Kinematics, Peter Corke Robotics Toolbox, Path Planning Algorithms.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("<br>", unsafe_allow_html=True)


st.markdown(
    '<div class="titlesection-header"><div style="text-align: center;"> <b>Project Manager and Researcher | Eik Lab, NMBU</b></div></div>',
    unsafe_allow_html=True
)
st.write('<div class="timeline"><div style="text-align: center;">02/2021 - 10/2023</div></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="text">
        <ul>
            <li>► Eik Lab is a student-driven lab at NMBU, where students can work on projects of their own choice. Here I engaged myself in multiple projects.</li>
            <li>► The most notable projects I contributed to were a self-drivable RC car using machine learning and a Steel Chain weighing station for automotive vehicles.</li>
            <li>► Skills used: Python, Machine Learning, TensorFlow, PyTorch, C++, Arduino, Raspberry Pi, JavaScript, SolidWorks, Fusion 360, 3D Printing, Laser Cutting, Soldering, General Machining Skills.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("<br>", unsafe_allow_html=True)


st.markdown(
    '<div class="titlesection-header"><div style="text-align: center;"> <b>Teaching Assistant, TMP100 | NMBU</b></div></div>',
    unsafe_allow_html=True
)
st.write('<div class="timeline"><div style="text-align: center;">08/2022-12/2022</div></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="text">
        <ul>
            <li>► TMP stands for Mechanical Engineering and Process Technology. I was responsible for teaching and planning this course in 2022.</li>
            <li>► My role included managing electrical wiring, acquiring parts, and instructing on CAD, 3D printing, and laser cutting tools.</li>
            <li>► Skills used: BOM list, CAD, 3D Printing, Laser Cutting, Soldering, General Machining Skills, Datasheet Reading.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("<br>", unsafe_allow_html=True)


st.markdown(
    '<div class="titlesection-header"><div style="text-align: center;"> <b>Shop Employee | Outland Oslo</b></div></div>',
    unsafe_allow_html=True
)
st.write('<div class="timeline"><div style="text-align: center;">2018 - 2020</div></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="text">
        <ul>
            <li>► Outland is a shop that sells board games, card games, roleplaying games, and other related items.</li>
            <li>► In this job I was entrusted with responsibility of a product group, and I was used as an expert on the topic of board games. My job was to help customers, control inventory, and to help with the weekly events that happened.</li>
            <li>► Skills used: Customer Service, Inventory Control, Event Planning.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)
st.write("<br>", unsafe_allow_html=True)


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

with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# ------ Projects ------
st.write("#")
st.subheader("Projects")

# Define the number of columns in the grid
num_columns = 2

# Calculate the number of rows based on the number of projects and columns
num_rows = -(-len(PROJECTS) // num_columns)  # Ceiling division

# Iterate over the projects and display them in a grid

for row in range(num_rows):
    cols = st.columns(num_columns)
    for col_index in range(num_columns):
        project_index = row * num_columns + col_index
        if project_index < len(PROJECTS):
            project, gif_path = list(PROJECTS.items())[project_index]
            
            with cols[col_index]:
                with stylable_container(
                    key = f"gifs_{project_index}",
                    css_styles=["""
                        div[data-testid="stImage"] > img {
                            border-radius: 15px;
                            border: 2px solid #ccc;
                            max-width: 100%;
                            height: auto;
                            position: relative;
                            display: inline-block;
                            transition: transform 0.5s ease;
                            z-index: 1; 
                        }
                        """,
                        """
                        div[data-testid="stImage"] > img:hover {
                            transform: scale(2.0);
                            z-index: 2;

                        }
                        """,
                        """
                            div[data-testid="stImage"] > .caption {
                            visibility: hidden;
                            position: absolute;
                            background-color: rgba(0, 0, 0, 0.7);
                            color: white;
                            padding: 10px;
                            border-radius: 5px;
                            bottom: 10%;
                            left: 50%;
                            transform: translateX(-50%);
                            transition: opacity 0.3s ease;
                            z-index: 2;
                        }
                        """,
                        """
                            div[data-testid="stImage"]:hover > .caption {
                            visibility: visible;
                            opacity: 1;
                        }
                        """,
                        """
                        button[title="View fullscreen"]{
                        visibility: hidden;}
                        """,
                    ]
                ):
                    # Display the GIF using st.image
                    st.image(gif_path, caption=f"{project}", width=350, use_container_width=True)
    st.write("---")
