import streamlit as st
import os
import json
import requests
from streamlit_lottie import st_lottie

# Page configuration
st.set_page_config(
    page_title="Ninad Alurkar | Robotics Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load Lottie animations from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load robotics-themed Lottie animations
lottie_robot = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_ghcyb6un.json")
lottie_arm = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_tjfwrzyx.json")
lottie_loading = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_yx2nzwag.json")

# Custom CSS for robotics theme with enhanced animations
st.markdown("""
<style>
    :root {
        --primary-color: #00d4ff;
        --secondary-color: #ff6b35;
        --dark-bg: #0a0e27;
        --card-bg: #1a1f3a;
        --text-primary: #ffffff;
        --text-secondary: #b0b8d4;
        --accent-1: #00d4ff;
        --accent-2: #ff6b35;
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 100%);
        color: var(--text-primary);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f1429 0%, #1a1f3a 100%);
        border-right: 2px solid var(--primary-color);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid var(--accent-1) !important;
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(255, 107, 53, 0.1));
        border: 2px solid var(--accent-1);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.2);
    }
    
    .project-card {
        background: linear-gradient(135deg, #1a1f3a 0%, #25284f 100%);
        border-left: 4px solid var(--accent-2);
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .project-card:hover {
        transform: translateX(5px);
        box-shadow: 0 6px 25px rgba(255, 107, 53, 0.3);
        border-left-color: var(--accent-1);
    }
    
    .skill-badge {
        display: inline-block;
        background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
        color: white;
        padding: 0.4rem 0.8rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.3rem;
        font-weight: 600;
        box-shadow: 0 2px 10px rgba(0, 212, 255, 0.3);
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { box-shadow: 0 2px 10px rgba(0, 212, 255, 0.3); }
        50% { box-shadow: 0 2px 20px rgba(0, 212, 255, 0.6); }
    }
    
    .video-container {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(255, 107, 53, 0.05));
        border: 2px solid var(--accent-1);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 0 30px rgba(0, 212, 255, 0.2);
    }
    
    .video-container video {
        border-radius: 8px;
        width: 100%;
        box-shadow: 0 0 20px rgba(0, 212, 255, 0.3);
    }
    
    h1, h2, h3 {
        color: var(--text-primary);
    }
    
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: fadeInDown 0.8s ease-out;
    }
    
    h2 {
        font-size: 1.8rem;
        border-bottom: 2px solid var(--accent-1);
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
    }
    
    p {
        color: var(--text-secondary);
        line-height: 1.6;
    }
    
    .divider {
        height: 2px;
        background: linear-gradient(90deg, var(--accent-1), transparent);
        margin: 2rem 0;
    }
    
    a {
        color: var(--accent-1);
        text-decoration: none;
        transition: all 0.3s ease;
    }
    
    a:hover {
        color: var(--accent-2);
        text-shadow: 0 0 10px rgba(0, 212, 255, 0.5);
    }
    
    .hero-section {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(255, 107, 53, 0.05));
        border-radius: 12px;
        padding: 3rem 2rem;
        text-align: center;
        border: 1px solid rgba(0, 212, 255, 0.3);
        margin-bottom: 2rem;
    }
    
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    .stat-box {
        background: rgba(0, 212, 255, 0.1);
        border: 2px solid var(--accent-1);
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
        animation: slideUp 0.6s ease-out;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .stat-box-number {
        font-size: 2rem;
        font-weight: 700;
        color: var(--accent-1);
    }
    
    .stat-box-label {
        color: var(--text-secondary);
        font-size: 0.9rem;
    }
    
    [data-testid="stButton"] > button {
        background: linear-gradient(135deg, var(--accent-1), var(--accent-2)) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.6rem 1.5rem !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stButton"] > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.4) !important;
    }
    
    .animation-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.05), rgba(255, 107, 53, 0.05));
        border-radius: 12px;
        margin: 1.5rem 0;
    }
    
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("### 🤖 Navigation")
    page = st.radio(
        "Select Page",
        ["Home", "Projects", "Skills & Tech", "Education", "Experience", "Contact"],
        label_visibility="collapsed"
    )

# HOME PAGE
if page == "Home":
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        try:
            st.image("image.png", use_column_width=True, caption="Ninad Alurkar")
        except:
            st.info("📸 Place image.png in your repository root")
    
    with col2:
        st.markdown("""
        # Ninad Alurkar
        ### Robotics Engineer | AI Systems Designer
        
        MS Robotics Engineering @ University of Michigan - Dearborn  
        Passionate about **human-robot interaction**, **autonomous systems**, and **computer vision**
        
        ---
        
        I develop intelligent robotic systems that bridge the gap between humans and machines. 
        Currently focused on trust-building in human-AI interactions and autonomous task execution.
        
        **Status:** 🔴 Actively researching adaptive response systems for human-companion robots
        """)
        
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        with col_btn1:
            st.link_button("📧 Email", "mailto:nalurkar@umich.edu")
        with col_btn2:
            st.link_button("🐙 GitHub", "https://github.com/ninadumich")
        with col_btn3:
            st.link_button("💼 LinkedIn", "https://linkedin.com/in/ninad-alurkar")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Robot Animation Section
    st.markdown("### 🤖 Featured Animation")
    col_anim1, col_anim2 = st.columns([1, 1], gap="large")
    
    with col_anim1:
        if lottie_robot:
            st_lottie(lottie_robot, height=300, key="robot_hero")
    
    with col_anim2:
        st.markdown("""
        #### Robotics & AI Integration
        
        Building the next generation of collaborative robots that understand and adapt to human needs through:
        
        - 🧠 **AI-Powered Decision Making**
        - 👁️ **Computer Vision Systems**
        - 🤝 **Human-Robot Interaction**
        - ⚙️ **Real-time Control Systems**
        """)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Quick Stats
    st.markdown("### 📊 Quick Stats")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-box-number">5+</div>
            <div class="stat-box-label">Projects</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-box-number">8</div>
            <div class="stat-box-label">Tech Skills</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-box-number">4</div>
            <div class="stat-box-label">Languages</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-box-number">GPA 3.96</div>
            <div class="stat-box-label">Master's</div>
        </div>
        """, unsafe_allow_html=True)

# PROJECTS PAGE
elif page == "Projects":
    st.markdown("# 🚀 Projects")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("My robotics and AI projects showcasing ROS, Gazebo, and computer vision.")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Project 1 with Animation
    col_proj1, col_proj2 = st.columns([2, 1], gap="large")
    
    with col_proj1:
        st.markdown("""
        <div class="project-card">
            <h3>🤝 Trust Building in Human-AI Interaction</h3>
            <p><strong>Timeline:</strong> Dec 2024 – Present</p>
            <p>Leading development of a human-companion robot for trust building through adaptive responses.</p>
            <ul>
                <li>Platform: Jackal Robot (Clearpath Robotics)</li>
                <li>Tech Stack: ROS, Python, Adaptive Learning, Emotion Recognition</li>
                <li>Focus: Face & Voice emotion recognition, Real-time robot response system</li>
                <li>Goal: Build adaptive learning feedback mechanisms for better human-robot trust</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_proj2:
        if lottie_robot:
            st_lottie(lottie_robot, height=250, key="trust_proj")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # Project 2 with Video
    st.markdown("""
    <div class="project-card">
        <h3>🍞 Autonomous Toasting with Computer Vision</h3>
        <p><strong>Timeline:</strong> Jan 2025 – Mar 2025</p>
        <p>Developed a complete simulated robotic arm system for autonomous cooking tasks.</p>
        <ul>
            <li>Simulation: ROS + Gazebo robotic arm environment</li>
            <li>Vision System: OpenCV for real-time food monitoring</li>
            <li>Task: Autonomous toasting of bread on a pan with visual feedback</li>
            <li>Communication: Arm-Camera integration via ROS topics</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Video Player Section
    st.markdown("### 📹 Robotic Arm Demonstration")
    try:
        video_file = open('video.mp4', 'rb')
        video_bytes = video_file.read()
        st.markdown("""
        <div class="video-container">
        """, unsafe_allow_html=True)
        st.video(video_bytes)
        st.markdown("""
        </div>
        """, unsafe_allow_html=True)
        st.success("✅ Video loaded successfully! Watch the robotic arm in action.")
    except FileNotFoundError:
        st.warning("⚠️ Video file not found. Please upload video.mp4 to the repository root.")
        st.info("📁 To add your video:\n1. Upload 'video.mp4' to your GitHub repo root\n2. Commit and push\n3. Refresh the page")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("### 💡 Technologies Used Across Projects")
    tech_cols = st.columns(4)
    techs = ["ROS", "Gazebo", "OpenCV", "Python", "C/C++", "MATLAB", "SolidWorks", "ANSYS"]
    for i, tech in enumerate(techs):
        with tech_cols[i % 4]:
            st.markdown(f'<span class="skill-badge">{tech}</span>', unsafe_allow_html=True)

# SKILLS & TECH PAGE
elif page == "Skills & Tech":
    st.markdown("# 🛠️ Skills & Technologies")
    
    # Animation at top
    col_anim, col_empty = st.columns([1, 1])
    with col_anim:
        if lottie_arm:
            st_lottie(lottie_arm, height=300, key="arm_skills")
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### 💻 Technical Skills")
        tech_skills = {
            "Robotics": ["ROS", "Gazebo", "Kinematics", "Motion Planning"],
            "Vision": ["OpenCV", "Image Processing", "Real-time Detection"],
            "Programming": ["Python", "C/C++", "MATLAB"],
            "Design & Analysis": ["SolidWorks", "ANSYS", "CAD", "Simulation"]
        }
        
        for category, skills in tech_skills.items():
            st.markdown(f"**{category}**")
            for skill in skills:
                st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
            st.markdown("")
    
    with col2:
        st.markdown("### 🌍 Languages")
        languages = {
            "English": "Professional",
            "Hindi": "Native",
            "Gujarati": "Native",
            "Marathi": "Native",
            "German": "Basic"
        }
        
        for lang, level in languages.items():
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.markdown(f"**{lang}**")
            with col_b:
                st.markdown(f"*{level}*")

# EDUCATION PAGE
elif page == "Education":
    st.markdown("# 🎓 Education")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>🎓 Master of Science in Robotics Engineering</h3>
        <p><strong>University of Michigan – Dearborn</strong></p>
        <p><strong>Duration:</strong> 2024 – 2026</p>
        <p><strong>GPA:</strong> 3.96 / 4.0</p>
        <p style="margin-top: 1rem; color: #b0b8d4;">
            Advanced coursework in robotic control systems, perception, AI integration, and autonomous systems design.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>🏆 Bachelor of Technology in Mechanical Engineering</h3>
        <p><strong>National Institute of Technology (NIT) – Surat, India</strong></p>
        <p><strong>Duration:</strong> 2018 – 2022</p>
        <p><strong>CGPA:</strong> 8.6 / 10.0</p>
        <p style="margin-top: 1rem; color: #b0b8d4;">
            Strong foundation in mechanical design, thermodynamics, mechanics, and engineering fundamentals.
            Thesis focus on robotic applications and mechanical systems optimization.
        </p>
    </div>
    """, unsafe_allow_html=True)

# EXPERIENCE PAGE
elif page == "Experience":
    st.markdown("# 💼 Experience")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>🔬 Research Assistant</h3>
        <p><strong>University of Michigan – Dearborn</strong></p>
        <p><strong>Timeline:</strong> Dec 2024 – Present</p>
        <ul>
            <li>Thesis: Human-AI Interaction using Emotion Recognition (Face & Voice)</li>
            <li>Developing adaptive response systems for human-companion robots</li>
            <li>Implementing feedback mechanisms for trust-building algorithms</li>
            <li>Preparing robotic systems for real-world interaction scenarios</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="project-card">
        <h3>👨‍🏫 Senior Design Project Advisor</h3>
        <p><strong>University of Michigan – Dearborn</strong></p>
        <p><strong>Timeline:</strong> Jan 2025 – Present</p>
        <ul>
            <li>Mentoring undergraduate team on Indoor Agricultural Robot project</li>
            <li>Base Platform: Jackal Robot with robotic arm integration</li>
            <li>Task: Autonomous irrigation system for greenhouse plants (up to 3m height)</li>
            <li>Technology: ROS, arm control, sensor integration, autonomous navigation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# CONTACT PAGE
elif page == "Contact":
    st.markdown("# 📧 Get In Touch")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("### Quick Contact Info")
        st.markdown("""
        📧 **Email:** nalurkar@umich.edu  
        📱 **Phone:** +1 248-990-5119  
        🎓 **Institution:** University of Michigan – Dearborn  
        📍 **Location:** Dearborn, Michigan, USA
        """)
        
        st.markdown("### Social & Professional")
        st.link_button("🐙 GitHub Profile", "https://github.com/ninadumich")
        st.link_button("💼 LinkedIn", "https://linkedin.com/in/ninad-alurkar")
        st.link_button("🎓 UMich Profile", "https://umich.edu")
    
    with col2:
        st.markdown("### Message")
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message", height=150)
            
            if st.form_submit_button("Send Message"):
                if name and email and subject and message:
                    st.success("✅ Thanks for reaching out! I'll get back to you soon.")
                    st.info(f"Message sent to: nalurkar@umich.edu")
                else:
                    st.warning("⚠️ Please fill in all fields")
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<p style='text-align: center; color: #b0b8d4;'>© 2025 Ninad Alurkar | Robotics Engineer</p>", unsafe_allow_html=True)
