import streamlit as st
import time
from datetime import datetime
st.set_page_config(layout="wide")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "menu_open" not in st.session_state:
    st.session_state.menu_open = False    
st.markdown("""
<style>
.stApp{
    background:
        radial-gradient(
            circle at center,
            rgba(168,85,247,0.28) 0%,
            rgba(168,85,247,0.18) 20%,
            rgba(168,85,247,0.08) 40%,
            transparent 70%
        ),

        linear-gradient(
            135deg,
            #0B1026 0%,
            #11122A 45%,
            #1A1D3A 75%,
            #0B1026 100%
        );

    background-attachment: fixed;
}
.logoP {
    font-size: 80px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #00c6ff, #8e2de2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 0px 20px rgba(142,45,226,0.6);
}

.pyverse {
    font-size: 40px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #00c6ff, #ffffff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    font-size: 16px;
    text-align: center;
    color: #cccccc;
    letter-spacing: 2px;
}
</style>

<div class="logoP">&lt;/&gt; P</div>
<div class="pyverse">PYVERSE</div>
<div class="tagline">CODE • LEARN • BUILD • EVOLVE</div>
""", unsafe_allow_html=True)
# ---------- TOP BAR ----------
left, mid, right = st.columns([1,8,1], vertical_alignment="center")

with left:
    if st.button("☰", use_container_width=True):
        st.session_state.menu_open = not st.session_state.menu_open

with right:
    if st.button("👤", use_container_width=True):
        if st.session_state.get("logged_in", False):
            st.switch_page("pages/3profile.py")
        else:
            st.warning("Please SignIn First")
if st.session_state.menu_open:
    with st.expander("Menu", expanded=True):
        if st.button("🔑 SignIn"):
            st.switch_page("pages/1SignIn.py")            
            
# -------- stat card------
hours = minutes = seconds = 0
efficiency = 0
streak =0
if st.session_state.logged_in:

    
    if "start_time" not in st.session_state:
        st.session_state.start_time = time.time()

    current_time = time.time()
    time_spent = int(current_time - st.session_state.start_time)

    hours = time_spent // 3600
    minutes = (time_spent % 3600) // 60
    seconds = time_spent % 60

    
    today = datetime.now().date()

    if "last_login" not in st.session_state:
        st.session_state.last_login = today
        st.session_state.streak = 1
    else:
        if st.session_state.last_login != today:
            st.session_state.streak += 1
            st.session_state.last_login = today

    streak = st.session_state.streak

    
    efficiency = min(100, int((time_spent / 3600) * 100))

# -------- CARD UI --------
st.markdown("""
<style>
.card {
    background: rgba(17, 18, 42, 0.7);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding:20px;
    border: 1px solid #2E2F5B;
    box-shadow: 0 0 15px rgba(77,163,255,0.2);
    transition: 0.3s ease;
}
.card:hover {
    box-shadow: 
        0 0 25px rgba(59,130,246,0.5),
        0 0 45px rgba(168,85,247,0.6);
}

.title {
    color: #9CA3AF;
    font-size: 25px;
}
.value {
    color: #38BDF8;
    font-size: 20px;
    font-weight: bold;
}
@media (max-width:768px){

div[data-testid="column"]{
    padding:10px !important;
}

.card{
    margin-bottom:15px !important;
}
}
</style>
""", unsafe_allow_html=True)

# -------- STAT CARDS (ALWAYS VISIBLE) --------
col1, col2, col3 = st.columns([5,5,5],gap="small")

with col1:
    st.markdown(
        f'<div class="card"><div class="title">⏱ Tracked</div><div class="value">{hours}h {minutes}m {seconds}s</div></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f'<div class="card"><div class="title">🔥 Strike</div><div class="value">{streak}</div></div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f'<div class="card"><div class="title">📊 Efficiency</div><div class="value">{efficiency}%</div></div>',
        unsafe_allow_html=True
    )

# ---------- BOTTOM SECTION ----------
left, right = st.columns(2)
#bottom left card
with left:
    st.markdown("""
    <style>
    .outer-card {
    background: rgba(17, 18, 42, 0.7);
    backdrop-filter: blur(12px);
    border-radius: 16px;
    padding: 25px;
    width: 100%;
    max-width: 900px;   /* Desktop aur Laptop dono ke liye same */
    margin: auto;
    border: 1px solid #2E2F5B;
    box-shadow: 0 0 15px rgba(77,163,255,0.2);
   }
/* Sirf Mobile */
@media (max-width:768px){
    .outer-card{
        max-width:340px !important;   /* Ya 320px/350px apne hisaab se */
        padding:18px !important;
    }
}
   .outer-card:hover {
    box-shadow: 
        0 0 25px rgba(59,130,246,0.5),
        0 0 45px rgba(168,85,247,0.6);
   }

   .inner-card {
         background:#F5EBDB;
         border-radius: 12px;
         padding: 15px;
         border: 1px solid #2E2F5B;
         color: #000000;
   }

    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="outer-card">
    <h2 style="color:#9CA3AF;">PyVerse</h2>
    <p> With the ultimate developer learning platform for mastering programming language.</p>
    <div class="inner-card">
    <h3>What you'll get</h3>
    <p>step-by-step guided lessions</p>
    <p>Interactive quizzes and exercises</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("<h2 style='margin-bottom:0;color:#9CA3AF;'>Explore</h2>", unsafe_allow_html=True)
st.markdown("<p style='margin-top:0;color:#9CA3AF;'>Learn all easily</p>", unsafe_allow_html=True)    
st.markdown("""
<style>
.bottom-card {
   background: rgba(17, 18, 42, 0.7);
   backdrop-filter: blur(12px);
   border-radius: 16px;
   padding: 80px;
   border: 1px solid #2E2F5B;
   box-shadow: 0 0 15px rgba(77,163,255,0.2);
   transition: 0.3s ease;
   color: #9CA3AF;
}

.bottom-card:hover {
    box-shadow: 
        0 0 25px rgba(59,130,246,0.5),
        0 0 45px rgba(168,85,247,0.6);
}
/* button spacing fix */
div.stButton {
     text-align: center;
     margin-top: -40px;
}
button{
        background:linear-gradient(90deg,#0040ff,#8c00ff);
        color:white;
        border:none;
        border-radius:10px;
        padding:10px 22px;
        font-weight:bold;
}

button:hover{
        background:linear-gradient(90deg,#005eff,#a855f7);
}
</style>
""", unsafe_allow_html=True)
# ✅ Layout
col1, col2 = st.columns(2)
# 🔹 LEFT CARD (Python)
with col1:
    st.markdown("""
    <div class="card">
        <h3 style="color:#9CA3AF;">PYTHON</h3>
        <p style="color:#9CA3AF;">Learn all basics programming</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="python-btn">', unsafe_allow_html=True)

    if st.button("View More", key="python_btn"):
       if st.session_state.get("logged_in", False):
          st.switch_page("pages/4python.py")
       else:
          st.warning("SignIn first!!!")

    st.markdown("</div>", unsafe_allow_html=True)
    
# 🔹 RIGHT CARD (dsa)
with col2:
    st.markdown("""
    <div class="card">
        <h3 style="color:#9CA3AF;">DSA</h3>
        <p style="color:#9CA3AF;">Practice data structure</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<div class="python-btn">', unsafe_allow_html=True)

    if st.button("View More", key="dsa_btn"):
      if st.session_state.get("logged_in", False):
        st.switch_page("pages/dsa.py")
      else:
        st.warning("SignIn first!!!")

st.markdown("</div>", unsafe_allow_html=True)
    
#footer
st.markdown("<hr style='border:1px solid #2E2F5B;'>", unsafe_allow_html=True)

st.markdown("""
<h4 style="text-align:center;color:#9CA3AF;">
🚀 Built with <span style="color:#90E0EF;">Streamlit</span>
</h4>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color:#90E0EF;'>Tutorials</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9CA3AF;'>• Python</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9CA3AF;'>• DSA</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #9CA3AF;'>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;color:#9CA3AF;">
© 2026 <b>PyVerse</b><br>
<span style="letter-spacing:2px;">Code • Learn • Build • Evolve</span>
</div>
""", unsafe_allow_html=True)
