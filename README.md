# Ninad Alurkar - Robotics Portfolio

A stunning multi-page Streamlit portfolio showcasing robotics projects, skills, education, and experience.

## 🚀 Quick Start

### Files Included
```
your-repo/
├── streamlit_app.py          # Main app (single file for easy deployment)
├── requirements.txt          # Python dependencies
├── image.png                 # Your profile photo (add this)
├── README.md                 # This file
└── .gitignore               # (Optional) ignore __pycache__, .streamlit secrets
```

### Setup Instructions

#### 1. **Clone or Create Repo**
```bash
git clone https://github.com/your-username/ninad-portfolio.git
cd ninad-portfolio
```

#### 2. **Add Your Photo**
- Save your profile photo as **`image.png`** in the root folder
- Supported formats: PNG, JPG, JPEG, GIF (PNG recommended for quality)

#### 3. **Install Dependencies Locally (Optional - Test Before Deploy)**
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Visit `http://localhost:8501` to preview

#### 4. **Push to GitHub**
```bash
git add .
git commit -m "Initial portfolio setup"
git push origin main
```

#### 5. **Deploy on Streamlit Community Cloud**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Sign in with GitHub
- Click **"New app"**
- Select:
  - Repository: `your-username/ninad-portfolio`
  - Branch: `main`
  - Main file path: `streamlit_app.py`
- Click **Deploy** → Live in ~2 minutes!

---

## 📋 Features

✅ **Multi-Page Navigation**
- Home (Hero with photo, quick stats)
- Projects (Trust-building robot, Vision-based toasting)
- Skills & Tech (ROS, Gazebo, OpenCV, etc. + Languages)
- Education (MS Robotics @ UMich, B.Tech @ NIT Surat)
- Experience (Research Assistant, Senior Design Advisor)
- Contact (Email, phone, social links, message form)

✅ **Robotics-Focused Design**
- Dark theme with cyan (#00d4ff) & orange (#ff6b35) accents
- Animated cards with hover effects
- Gradient backgrounds & glowing borders
- Responsive grid layouts
- Skill badges with shadow effects

✅ **No Backend Needed**
- Fully client-side (no database required)
- GitHub-hosted content
- One-click Streamlit deployment

---

## 🎨 Customization

### Update Project Details
Edit the **Projects** section in `streamlit_app.py`:
```python
st.markdown("""
<div class="project-card">
    <h3>Your Project Title</h3>
    <p><strong>Timeline:</strong> Jan 2025 – Mar 2025</p>
    <p>Your description here...</p>
</div>
""", unsafe_allow_html=True)
```

### Change Colors
Modify CSS variables at the top of `streamlit_app.py`:
```python
--primary-color: #00d4ff;      # Cyan
--secondary-color: #ff6b35;    # Orange
```

### Update Contact Info
Search for `nalurkar@umich.edu` and replace with your email, phone, and links.

---

## 📦 Dependencies
- **streamlit** — Web framework
- **Pillow** — Image handling
- **requests** — HTTP requests (optional, for future features)

---

## 🔧 Troubleshooting

**Image not showing?**
- Ensure `image.png` is in the root folder
- File must be in PNG, JPG, or JPEG format

**Deployment fails?**
- Check `requirements.txt` syntax (one package per line)
- Ensure `streamlit_app.py` is named correctly
- Verify all files are committed to GitHub

**Want to test locally first?**
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📞 Support

- Streamlit Docs: [docs.streamlit.io](https://docs.streamlit.io)
- Community Cloud: [share.streamlit.io](https://share.streamlit.io)
- Deploy Guide: [docs.streamlit.io/deploy](https://docs.streamlit.io/deploy/streamlit-community-cloud)

---

## 📝 License

© 2025 Ninad Alurkar | All rights reserved
