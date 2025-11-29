import streamlit as st
import numpy as np
import pandas as pd

# ------------ PAGE CONFIG ------------
st.set_page_config(
    page_title="Ghanshyam | Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)

# ------------ BASIC INFO ------------
NAME = "Ghanshyam Seervi"
ROLE = "B.Tech CSE Student"
UNIVERSITY = "Vivekananda Global University, Jaipur"
COURSE = "Computer Science Engineering"
TAGLINE = "Aspiring Developer | Python • Java • C • SQL • Power BI"

EMAIL = "your_email@example.com"          # <- change this
LINKEDIN_URL = "https://www.linkedin.com/in/your-profile" 
GITHUB_URL = "https://github.com/your-username"            

skills = {
    "Python": 90,
    "Java": 75,
    "C": 70,
    "SQL": 80,
    "Power BI": 85,
}

# ------------ SIDEBAR ------------
st.sidebar.image(
    "https://static-00.iconduck.com/assets.00/developer-emoji-2048x2048-7t9u9p5g.png",
    width=120,
)

st.sidebar.title("👨‍💻 Ghanshyam's Portfolio")
st.sidebar.markdown(f"{NAME}")
st.sidebar.markdown(ROLE)
st.sidebar.markdown(UNIVERSITY)

page = st.sidebar.radio(
    "Go to",
    ["Home", "Skills", "Projects", "Dashboard Demo", "Contact"],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.markdown("*Connect with me*")
st.sidebar.markdown(f"[LinkedIn]({LINKEDIN_URL})")
st.sidebar.markdown(f"[GitHub]({GITHUB_URL})")
st.sidebar.markdown(f" {EMAIL}")

# ------------ HOME PAGE ------------
if page == "Home":
    st.title(f"Hi, I'm {NAME}")
    st.subheader(TAGLINE)

    st.write(
        f"""
I am a *{ROLE}* at *{UNIVERSITY}, studying **{COURSE}*.

I enjoy:
- Learning programming
- Building small projects
- Exploring data and dashboards

This portfolio is a simple Streamlit app to show my skills and projects.
"""
    )

# ------------ SKILLS PAGE ------------
elif page == "Skills":
    st.title("🛠 Skills")

    st.write("Here are some of the skills I am learning and using:")

    for skill, level in skills.items():
        st.write(f"- {skill} ({level}%)")

# ------------ PROJECTS PAGE ------------
elif page == "Projects":
    st.title(" Projects")

    st.subheader("1. Interactive Dashboard using Streamlit")
    st.write(
        """
A basic dashboard built using *Streamlit*.

- Simple layout
- Basic widgets
- Good for learning how web apps work with Python
"""
    )

    st.subheader("2. Unit Converter (Python)")
    st.write(
        """
A small *Unit Converter* project in Python.

- Converts units like length, weight, temperature
- Uses functions and if-else conditions
"""
    )

    st.subheader("More Projects Coming Soon")
    st.write("I will keep adding more projects here as I build them.")

# ------------ DASHBOARD DEMO PAGE ------------
elif page == "Dashboard Demo":
    st.title(" Dashboard Demo (Sample)")

    st.write(
        """
This is a very simple example of a small dashboard.
The data below is randomly generated just for demo.
"""
    )

    # simple sample data
    x = np.arange(10)
    y = np.random.randint(1, 10, size=10)
    df = pd.DataFrame({"X": x, "Y": y})

    st.write("Sample Data:")
    st.table(df)

    st.write("Simple Line Chart:")
    st.line_chart(df, x="X", y="Y")

# ------------ CONTACT PAGE ------------
elif page == "Contact":
    st.title(" Contact")

    st.write("You can reach out to me here:")
    st.write(f"- Email: {EMAIL}")
    st.write(f"- LinkedIn: {LINKEDIN_URL}")
    st.write(f"- GitHub: {GITHUB_URL}")
