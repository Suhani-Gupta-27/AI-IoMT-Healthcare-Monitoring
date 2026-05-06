import streamlit as st
import time
import random
from collections import deque
import numpy as np
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import tempfile
from datetime import datetime
import os
from dotenv import load_dotenv
from groq import Groq

# =========================
# LOAD ENV
# =========================
load_dotenv(dotenv_path=".env")

# ✅ CREATE CLIENT (FIXED)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Monitor", layout="wide")

# =========================
# CSS
# =========================
if "css_loaded" not in st.session_state:
    st.session_state.css_loaded = True

    st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    h1, h2, h3 { color: #00FFAA; }
    section[data-testid="stSidebar"] { background-color: #0A0A0A; }
    div[data-testid="metric-container"] {
        background-color: #111111;
        border: 1px solid #00FFAA;
        padding: 12px;
        border-radius: 12px;
    }
    .stButton>button {
        background-color: #00FFAA;
        color: black;
        border-radius: 10px;
        font-weight: bold;
    }
    p, label, span { color: #EAEAEA !important; }
    </style>
    """, unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "started" not in st.session_state:
    st.session_state.started = False

if "patient" not in st.session_state:
    st.session_state.patient = {}

if "data_buffer" not in st.session_state:
    st.session_state.data_buffer = deque(maxlen=60)

if "temp_base" not in st.session_state:
    st.session_state.temp_base = 37.0

if "pulse_base" not in st.session_state:
    st.session_state.pulse_base = 75

if "report" not in st.session_state:
    st.session_state.report = ""

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("Intake Panel")

    if not st.session_state.started:
        name = st.text_input("Patient Name")
        pid = st.text_input("Patient ID")
        age = st.number_input("Age", 0, 120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        condition = st.selectbox("Condition", ["None","Diabetes","Hypertension","Cardiac"])
        doctor = st.text_input("Doctor Name")

        if st.button("Start Monitoring"):
            if name and pid:
                st.session_state.patient = {
                    "name": name,
                    "id": pid,
                    "age": age,
                    "gender": gender,
                    "condition": condition,
                    "doctor": doctor if doctor else "ICU Doctor"
                }
                st.session_state.started = True
                st.rerun()

# =========================
# BLOCK
# =========================
if not st.session_state.started:
    st.title("Monitoring System")
    st.info("Enter patient details to begin")
    st.stop()

# =========================
# HEADER
# =========================
p = st.session_state.patient
st.title(f"Dashboard — {p['name']}")

# =========================
# AI PANEL
# =========================
st.subheader("AI Clinical Intelligence")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Risk Status", "Normal")
c2.metric("Drug Dosage (units)", "0.3")
c3.metric("Light Adjustment (%)", "5.0")
c4.metric("System State", "Active")

# =========================
# SENSOR SIMULATION
# =========================
def smooth(v, step):
    return round(v + random.uniform(-step, step), 2)

st.session_state.temp_base = smooth(st.session_state.temp_base, 0.05)
st.session_state.pulse_base = int(smooth(st.session_state.pulse_base, 0.8))

temp = st.session_state.temp_base
pulse = max(60, min(100, st.session_state.pulse_base))
ldr = int(random.normalvariate(220, 8))

st.session_state.data_buffer.append({
    "temp": temp,
    "pulse": pulse,
    "ldr": ldr
})

# =========================
# VITALS
# =========================
v1, v2, v3 = st.columns(3)
v1.metric("Temperature (°C)", temp)
v2.metric("Pulse (bpm)", pulse)
v3.metric("LDR", ldr)

# =========================
# AI SUMMARY
# =========================
def generate_ai_summary(data, patient):
    date = datetime.now().strftime("%d-%m-%Y")

    prompt = f"""
You are an ICU doctor.

Patient Info:
{patient}

Vitals:
{data}

Give structured report.

End with:
Date: {date}
Signature: {patient.get('doctor')}
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content

# =========================
# BUTTON
# =========================
st.subheader("AI Medical Report")

if st.button("🩺 Generate Full Report"):
    last5 = list(st.session_state.data_buffer)[-5:]
    with st.spinner("Analyzing patient..."):
        st.session_state.report = generate_ai_summary(last5, p)

# =========================
# REPORT
# =========================
if st.session_state.report:
    st.markdown("### Doctor Report")
    st.write(st.session_state.report)

    def create_pdf(text):
        file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        doc = SimpleDocTemplate(file.name)
        styles = getSampleStyleSheet()
        doc.build([Paragraph(text, styles["Normal"])])
        return file.name

    pdf = create_pdf(st.session_state.report)

    with open(pdf, "rb") as f:
        st.download_button("Download Report", f, file_name="ICU_Report.pdf")

# =========================
# GRAPH
# =========================
st.subheader("Vital Trends")

st.line_chart({
    "Temperature":[d["temp"] for d in st.session_state.data_buffer],
    "Pulse":[d["pulse"] for d in st.session_state.data_buffer],
    "LDR":[d["ldr"] for d in st.session_state.data_buffer]
})

# =========================
# LIVE FEED
# =========================
with st.expander("Live Feed"):
    st.write(list(st.session_state.data_buffer)[-10:])

# =========================
# REFRESH
# =========================
time.sleep(3)
st.rerun()