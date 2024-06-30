import requests
from pathlib import Path
from streamlit_lottie import st_lottie

import streamlit as st
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding =load_lottieurl( "https://lottie.host/cf3f918d-6b50-4a88-b8f0-dace365f0cae/BqeTrVojTB.json")


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Priyasha"
PAGE_ICON = ":wave:"
NAME = "Priyasha Ghosh"
DESCRIPTION = """
Application Developer.
"""
EMAIL = "ghoshpriyasha29@gmail.com.com"
SOCIAL_MEDIA = {

    "LinkedIn": "https://www.linkedin.com/in/priyasha-ghosh-523273220/",
    "GitHub": "https://github.com/Priyasha2002",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Lily House -  Ecommerce app": "https://github.com/Priyasha2002/Lily_House",
    "🏆 Lily House Admin App -  Ecommerce Admin app": "https://github.com/Priyasha2002/Lily_House_Admin_App",
    "🏆 Quizlet - Quiz app using Flutter": "https://github.com/Priyasha2002/Quizlet_app",
    "🏆 VIT Bhopal Chatbot App - Assistant app for VIT Bhopal students": "https://github.com/Priyasha2002/VITB_chatbot_app",
    "🏆 Sentiment Analysis - Web app using Python, analyzing text sentiment.": "https://github.com/Priyasha2002/Sentiment_Analysis",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1 year experience as Data Analyst at KAIZEN IT SERVICES PRIVATE LIMITED
- ✔️ Strong hands on experience and knowledge in Python and Flutter
- ✔️ Good understanding of Amazon Web Services (AWS)
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), Flutter, SQL
- ☁️ Cloud Computing: AWS Cloud, Firebase
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Database: MySQL

"""
)
with st.container():
    left_column , right_column = st.columns(2)
    with left_column:
# --- SKILLS ---
            st.write('\n')
            st.subheader("Certifications")
            st.write(
                """
            - ☁️ AWS Certified Cloud Practitioner
            - 🐍 Python
            - 🤖 Machine Learning
            - ☁️ Google Cloud
            
            """
            )
with right_column:
    st_lottie(lottie_coding, height= 300, key="coding")

# --- LANGUAGES ---
st.write('\n')
st.subheader("Languages")
st.write(
    """
- 🌍 🇺🇸 English
- 🌼 🇧🇩 Bengali
- 🌟 🇮🇳 Hindi
- 🎌 🇯🇵 Japanese

"""
)




# --- INTERNSHIPS ---
st.write('\n')
st.subheader("INTERNSHIPS")
st.write("---")

# --- JOB 1
st.write("🚧", "** Data Analyst | Kaizen IT Services Private Limited**")
st.write("02/2023 - 02/2024")
st.write(
    """
- ► Developed a smart chat application using AI, enhancing user interaction and experience through natural language processing and machine learning algorithms.
- ► Utilized Python and TensorFlow to train and deploy chatbots, improving response accuracy and user satisfaction by 25%.
- ► Employed SQL and Firebase for efficient data storage and retrieval, ensuring seamless app performance and scalability.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Application Developer | Bharat Intern**")
st.write("01/2024 - 02/2024")
st.write(
    """
- ► Developed a weather application using Flutter, providing users with real-time weather updates and forecasts through a sleek and intuitive interface.
- ► Created a To-Do application using Flutter, enabling users to efficiently manage tasks with features such as reminders, priority settings, and data synchronization across devices.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Acolyte | TheCyberDelta**")
st.write("11/2022 - 05/2023")
st.write(
    """
- ► Collaborated with the management team to streamline operational workflows and enhance project efficiency.
- ► Conducted market research and competitive analysis to identify strategic opportunities and support decision-making processes.
- ► Managed communication channels and facilitated meetings to ensure effective team collaboration and project progress tracking.
- ► Assisted in project planning, resource allocation, and timeline management to meet organizational goals and client expectations.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")







