
import streamlit as st
from datetime import date

# ==========================================
# SciQuest | Created by Kaushal Patil
# ==========================================

st.set_page_config(
    page_title="SciQuest | Kaushal Patil",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM DESIGN ----------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #08111f 0%, #101c32 55%, #0b1220 100%);
        color: #f1f5f9;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #f8fafc !important;
    }

    p, li {
        color: #cbd5e1;
    }

    [data-testid="stSidebar"] {
        background-color: #0b1424;
    }

    .hero {
        padding: 2rem;
        border-radius: 22px;
        border: 1px solid #263954;
        background: linear-gradient(120deg, #132541, #101827);
        margin-bottom: 1.5rem;
    }

    .eyebrow {
        color: #60a5fa;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 0.8rem;
    }

    .hero-title {
        font-size: clamp(2rem, 5vw, 3.2rem);
        font-weight: 800;
        color: #ffffff;
        margin: 0.5rem 0;
    }

    .muted {
        color: #a9bad0;
        line-height: 1.8;
    }

    .profile-card {
        padding: 1.5rem;
        border: 1px solid #293c58;
        background: rgba(20, 35, 57, 0.85);
        border-radius: 18px;
        margin-bottom: 1rem;
        height: 100%;
    }

    .profile-label {
        color: #60a5fa;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 1.5px;
        font-weight: 700;
    }

    .profile-heading {
        color: #f8fafc;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0.6rem 0;
    }

    .skill {
        display: inline-block;
        padding: 0.4rem 0.75rem;
        margin: 0.25rem 0.25rem 0.25rem 0;
        border-radius: 20px;
        background: #172e4d;
        border: 1px solid #315784;
        color: #bfdbfe;
        font-size: 0.85rem;
    }

    .footer {
        border-top: 1px solid #263954;
        padding-top: 1rem;
        margin-top: 2rem;
        text-align: center;
        color: #8fa4bf;
        font-size: 0.85rem;
    }

    div[data-testid="stMetric"] {
        background: #132541;
        border: 1px solid #293c58;
        padding: 1rem;
        border-radius: 14px;
    }

    .stButton button {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- PAGE NAVIGATION STATE ----------
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

def go_to_page(page_name):
    st.session_state.selected_page = page_name
if "visited_pages" not in st.session_state:
    st.session_state.visited_pages = set()

if st.session_state.selected_page != "Home":
    st.session_state.visited_pages.add(
        st.session_state.selected_page
    )
# ---------- SIDEBAR ----------
st.sidebar.markdown("## 🔬 SciQuest")
st.sidebar.caption("INTERACTIVE SCIENCE LAB")
st.sidebar.divider()

page = st.sidebar.radio(
    "EXPLORE",
    [
        "Home",
        "Electricity Lab",
        "Space Explorer",
        "Science Quiz",
        "Light & Optics Lab",
        "Eco Impact Calculator",
        "About the Creator"
    ],
    key="selected_page"
)
st.sidebar.divider()
st.sidebar.caption("Created by Kaushal Patil")


# ---------- COMMON HEADER ----------
st.markdown("""
<div class="hero">
    <div class="eyebrow">INTERACTIVE VIRTUAL SCIENCE LAB</div>
    <div class="hero-title">🔬 SciQuest</div>
    <div class="muted">
        Discover. Experiment. Learn.<br>
        Making science more interactive, one experiment at a time.
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================
if page == "Home":

    st.header("Welcome to SciQuest 🚀")

    st.write(
        "Explore scientific ideas through interactive "
        "experiments. Change values, observe results, "
        "and discover the science behind them."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">EXPERIMENT 01</div>
            <div class="profile-heading">⚡ Electricity Lab</div>
            <p class="muted">
                Explore how voltage and resistance affect
                electric current using Ohm's law.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">OUR MISSION</div>
            <div class="profile-heading">🧠 Learn by Exploring</div>
            <p class="muted">
                Make science easier to understand through
                interactive demonstrations and discovery.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.info(
        "Choose Electricity Lab in the sidebar to "
        "start your first experiment."
    )

    st.markdown("### Built by a student developer")

    st.write(
        "SciQuest is a school science exhibition project "
        "created by Kaushal Patil."
    )
    st.markdown("## 📊 Your Science Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔬 Interactive Labs", "4")

    with col2:
        st.metric("🪐 Worlds to Explore", "9")

    with col3:
        st.metric("🧠 Questions per Round", "5")

    st.markdown("---")
    st.markdown("## 🎯 Your Exploration Progress")

    visited = st.session_state.visited_pages
    total = 3
    completed = sum(
        name in visited
        for name in [
            "Electricity Lab",
            "Space Explorer",
            "Science Quiz"
        ]
    )

    st.progress(completed / total)
    st.write(f"You have explored {completed} out of {total} activities!")

    st.markdown("### ✨ What you can explore")
    feature_col1, feature_col2, feature_col3 = st.columns(3)

    with feature_col1:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">PHYSICS</div>
            <div class="profile-heading">⚡ Electricity & Light</div>
            <p class="muted">Explore current, resistance, and reflection.</p>
        </div>
        """, unsafe_allow_html=True)

    with feature_col2:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">SPACE</div>
            <div class="profile-heading">🪐 Space Explorer</div>
            <p class="muted">Compare gravity and weight across worlds.</p>
        </div>
        """, unsafe_allow_html=True)

    with feature_col3:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">ENVIRONMENT</div>
            <div class="profile-heading">🌱 Eco Impact</div>
            <p class="muted">Estimate resource savings and earn a certificate.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("## 🚀 Launch an Experiment")
    st.write("Choose a lab and start exploring science!")

    st.markdown("## 🧪 Explore Your Labs")

    card1, card2 = st.columns(2)

    with card1:
        st.markdown("""
        <div class="profile-card">
            <h3>⚡ Electricity Lab</h3>
            <p>Learn how voltage, resistance,
            and electric current work.</p>
            <p><b>Concept:</b> Ohm's Law</p>
        </div>
        """, unsafe_allow_html=True)

    with card2:
        st.markdown("""
        <div class="profile-card">
            <h3>🪐 Space Explorer</h3>
            <p>Explore planets and discover
            how gravity affects your weight.</p>
            <p><b>Concept:</b> Gravity</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button(
            "⚡ Electricity Lab",
            on_click=go_to_page,
            args=("Electricity Lab",),
            use_container_width=True
        )

    with col2:
        st.button(
            "🪐 Space Explorer",
            on_click=go_to_page,
            args=("Space Explorer",),
            use_container_width=True
        )

    with col3:
        st.button(
            "🧠 Science Quiz",
            on_click=go_to_page,
            args=("Science Quiz",),
            use_container_width=True
        )

# ==========================================
# ELECTRICITY LAB
# ==========================================
elif page == "Electricity Lab":

    st.header("⚡ Electricity Lab")

    st.write(
        "Investigate the relationship between voltage, "
        "resistance, and electric current."
    )

    st.latex(r"I = \frac{V}{R}")

    st.caption(
        "Ohm's law: current equals voltage divided by resistance."
    )

    col1, col2 = st.columns(2)

    with col1:
        voltage = st.slider(
            "Voltage (V)",
            min_value=1,
            max_value=12,
            value=6
        )

    with col2:
        resistance = st.slider(
            "Resistance (Ω)",
            min_value=1,
            max_value=12,
            value=3
        )

    current = voltage / resistance

    st.divider()
    st.subheader("Your experimental results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Voltage", f"{voltage} V")
    col2.metric("Resistance", f"{resistance} Ω")
    col3.metric("Current", f"{current:.2f} A")

    st.markdown("### What does this mean?")

    st.write(
        f"With a voltage of {voltage} V and resistance "
        f"of {resistance} Ω, the calculated current is "
        f"{current:.2f} amperes."
    )

    if voltage == resistance:
        st.success(
            "Voltage and resistance have the same numerical "
            "value, so the current is 1 ampere."
        )
    elif current > 1:
        st.info(
            "The current is greater than 1 ampere. "
            "Try increasing resistance to see what happens."
        )
    else:
        st.info(
            "The current is 1 ampere or less. "
            "Try increasing voltage or reducing resistance."
        )

    st.caption(
        "This is an ideal mathematical simulation, "
        "not a real electrical circuit."
    )


# ==========================================
# ABOUT THE CREATOR
# ==========================================

elif page == "Light & Optics Lab":
    import math
    import matplotlib.pyplot as plt

    st.markdown("## 🔦 Light & Optics Lab")
    st.write(
        "Explore how light reflects from a plane mirror. "
        "Change the incoming angle and observe the reflected ray."
    )

    angle = st.slider(
        "Angle of incidence (degrees)",
        min_value=0,
        max_value=80,
        value=30
    )

    reflection_angle = angle

    st.markdown("### 📐 Your Results")
    col1, col2 = st.columns(2)

    col1.metric("Incident angle", f"{angle}°")
    col2.metric("Reflection angle", f"{reflection_angle}°")

    st.success(
        f"The angle of reflection is {reflection_angle}°, "
        "equal to the angle of incidence."
    )

    # Draw the mirror and light rays
    radians = math.radians(angle)
    ray_length = 4

    incident_x = -ray_length * math.sin(radians)
    incident_y = ray_length * math.cos(radians)

    reflected_x = ray_length * math.sin(radians)
    reflected_y = ray_length * math.cos(radians)

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.plot([-4, 4], [0, 0], linewidth=4, label="Plane mirror")
    ax.plot([0, 0], [-0.5, 4.5], linestyle="--",
            label="Normal")

    ax.annotate(
        "", xy=(0, 0), xytext=(incident_x, incident_y),
        arrowprops=dict(arrowstyle="->", linewidth=2)
    )
    ax.annotate(
        "", xy=(reflected_x, reflected_y), xytext=(0, 0),
        arrowprops=dict(arrowstyle="->", linewidth=2)
    )

    ax.text(incident_x * 0.6, incident_y * 0.6,
            "Incident ray", ha="center")
    ax.text(reflected_x * 0.6, reflected_y * 0.6,
            "Reflected ray", ha="center")

    ax.set_title("Law of Reflection")
    ax.set_xlabel("Horizontal direction")
    ax.set_ylabel("Vertical direction")
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-0.5, 4.5)
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.2)
    ax.legend()

    st.pyplot(fig)
    plt.close(fig)

    st.markdown("### 🧠 What did you learn?")
    st.info(
        "1. The incident ray is the incoming light ray.\n\n"
        "2. The reflected ray is the light ray that bounces off "
        "the mirror.\n\n"
        "3. Both angles are measured from the normal, "
        "an imaginary line perpendicular to the mirror.\n\n"
        "4. The angle of incidence equals the angle of reflection."
    )

elif page == "Eco Impact Calculator":
    st.markdown("## 🌍 Eco Impact Calculator")
    st.write(
        "Explore how small daily habits can help save "
        "electricity and water."
    )

    st.markdown("### ⚡ Electricity Savings")

    saved_units = st.slider(
        "Electricity saved per month (kWh)",
        min_value=0,
        max_value=100,
        value=10
    )

    # Approximate illustrative estimate, not a precise emissions audit
    emission_factor = 0.7
    co2_saved = saved_units * emission_factor

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Monthly electricity saved", f"{saved_units} kWh")

    with col2:
        st.metric("Estimated CO₂ avoided", f"{co2_saved:.1f} kg")

    st.markdown("---")
    st.markdown("### 💧 Water Savings")

    water_saved = st.slider(
        "Water saved per day (litres)",
        min_value=0,
        max_value=100,
        value=10
    )

    monthly_water = water_saved * 30

    col3, col4 = st.columns(2)

    with col3:
        st.metric("Daily water saved", f"{water_saved} litres")

    with col4:
        st.metric("Estimated monthly water saved", f"{monthly_water} litres")

    st.markdown("### 🌱 Your Environmental Impact")

    if saved_units > 0 or water_saved > 0:
        st.success(
            "Great! Small, consistent savings can make a "
            "meaningful difference over time."
        )
    else:
        st.info(
            "Move either slider to explore how saving "
            "resources can help."
        )

    st.caption(
        "Note: The CO₂ estimate uses an illustrative factor of "
        "0.7 kg per kWh. Actual emissions vary by electricity source."
    )

    st.markdown("---")
    st.markdown("## 🏆 Eco Challenge")
    st.write("Answer three questions to discover your eco habits!")

    lights = st.radio(
        "1. Do you switch off lights when leaving a room?",
        ["Always", "Sometimes", "Rarely"],
        key="eco_lights"
    )

    water = st.radio(
        "2. Do you turn off the tap while brushing?",
        ["Always", "Sometimes", "Rarely"],
        key="eco_water"
    )

    plastic = st.radio(
        "3. Do you carry a reusable water bottle?",
        ["Always", "Sometimes", "Rarely"],
        key="eco_bottle"
    )

    scores = {"Always": 2, "Sometimes": 1, "Rarely": 0}

    if st.button("🌿 Calculate My Eco Score", key="eco_score_button"):
        score = scores[lights] + scores[water] + scores[plastic]
        st.session_state["eco_score"] = score
        st.metric("Your Eco Score", f"{score}/6")

        if score >= 5:
            st.success("Excellent habits! Keep protecting our planet.")
        elif score >= 3:
            st.info("Good start! Try improving one habit this week.")
        else:
            st.warning("Choose one small eco-friendly habit to practise today.")

        st.markdown("### 💡 Your Next Steps")
        if lights != "Always":
            st.write("- Switch off unnecessary lights and fans.")
        if water != "Always":
            st.write("- Turn off the tap while brushing.")
        if plastic != "Always":
            st.write("- Carry a reusable bottle when practical.")

    st.markdown("### 📊 Your Monthly Savings Chart")

    import pandas as pd

    savings_data = pd.DataFrame({
        "Resource": ["Electricity (kWh)", "Water (litres)"],
        "Monthly Savings": [saved_units, monthly_water]
    })

    st.bar_chart(
        savings_data,
        x="Resource",
        y="Monthly Savings",
        color="#38BDF8"
    )

    st.caption(
        "The chart compares the numerical savings for each resource. "
        "Because the units differ, compare electricity and water separately."
    )

    st.markdown("---")
    st.markdown("## 🏆 Eco Achievement Certificate")
    st.write(
        "Enter your name and generate a printable PDF certificate "
        "after calculating your Eco Challenge score."
    )

    visitor_name = st.text_input(
        "Certificate recipient name",
        key="eco_certificate_name",
        placeholder="Enter your full name"
    )

    if st.button("🎓 Generate PDF Certificate", key="generate_eco_certificate"):
        if not visitor_name.strip():
            st.warning("Please enter your name first.")
        elif "eco_score" not in st.session_state:
            st.warning("Please calculate your Eco Score first.")
        else:
            certificate_score = st.session_state["eco_score"]

            if certificate_score >= 5:
                achievement = "Eco Champion"
            elif certificate_score >= 3:
                achievement = "Eco Guardian"
            else:
                achievement = "Eco Beginner"

            try:
                from io import BytesIO
                from reportlab.lib.pagesizes import A4, landscape
                from reportlab.lib.colors import HexColor, white
                from reportlab.pdfgen import canvas

                pdf_buffer = BytesIO()
                page_width, page_height = landscape(A4)
                pdf = canvas.Canvas(pdf_buffer, pagesize=(page_width, page_height))

                # Certificate background and double border
                pdf.setFillColor(white)
                pdf.rect(0, 0, page_width, page_height, fill=1, stroke=0)

                pdf.setStrokeColor(HexColor("#166534"))
                pdf.setLineWidth(5)
                pdf.roundRect(22, 22, page_width - 44, page_height - 44, 18, fill=0, stroke=1)

                pdf.setStrokeColor(HexColor("#D4AF37"))
                pdf.setLineWidth(1.8)
                pdf.roundRect(33, 33, page_width - 66, page_height - 66, 14, fill=0, stroke=1)

                # Header
                pdf.setFillColor(HexColor("#166534"))
                pdf.setFont("Helvetica-Bold", 15)
                pdf.drawCentredString(page_width / 2, page_height - 78, "SCIQUEST • ENVIRONMENTAL LEARNING")

                pdf.setFillColor(HexColor("#173B2A"))
                pdf.setFont("Helvetica-Bold", 29)
                pdf.drawCentredString(page_width / 2, page_height - 125, "ECO ACHIEVEMENT CERTIFICATE")

                pdf.setFillColor(HexColor("#64748B"))
                pdf.setFont("Helvetica", 13)
                pdf.drawCentredString(page_width / 2, page_height - 160, "This certificate is proudly presented to")

                # Recipient
                pdf.setFillColor(HexColor("#0F172A"))
                pdf.setFont("Helvetica-Bold", 27)
                pdf.drawCentredString(page_width / 2, page_height - 205, visitor_name.strip()[:70])

                pdf.setStrokeColor(HexColor("#D4AF37"))
                pdf.setLineWidth(1.5)
                pdf.line(page_width * 0.25, page_height - 218, page_width * 0.75, page_height - 218)

                # Achievement badge
                pdf.setFillColor(HexColor("#E8F5E9"))
                pdf.roundRect(page_width / 2 - 115, page_height - 267, 230, 32, 12, fill=1, stroke=0)
                pdf.setFillColor(HexColor("#166534"))
                pdf.setFont("Helvetica-Bold", 16)
                pdf.drawCentredString(page_width / 2, page_height - 256, achievement)

                pdf.setFillColor(HexColor("#334155"))
                pdf.setFont("Helvetica", 13)
                pdf.drawCentredString(
                    page_width / 2, page_height - 300,
                    f"Eco Challenge Score: {certificate_score}/6"
                )
                pdf.drawCentredString(
                    page_width / 2, page_height - 324,
                    "For learning practical ways to conserve resources and care for our planet."
                )

                pdf.setFillColor(HexColor("#475569"))
                pdf.setFont("Helvetica", 11)
                pdf.drawString(58, 62, f"Issued: {date.today().strftime('%d %B %Y')}")
                pdf.drawRightString(page_width - 58, 62, "Created by Kaushal Patil • SciQuest")

                pdf.save()
                pdf_bytes = pdf_buffer.getvalue()
                pdf_buffer.close()

                st.success(f"Congratulations, {visitor_name.strip()}! Your PDF certificate is ready.")
                st.download_button(
                    label="📥 Download Your PDF Certificate",
                    data=pdf_bytes,
                    file_name="SciQuest_Eco_Achievement_Certificate.pdf",
                    mime="application/pdf",
                    key="download_eco_certificate"
                )
                st.caption("Tip: Print in landscape orientation for the best result.")

            except ImportError:
                st.error("PDF support needs ReportLab. In the VS Code terminal, run: pip install reportlab")

elif page == "About the Creator":

    # Profile introduction
    st.markdown("""
    <div class="hero">
        <div class="eyebrow">MEET THE CREATOR</div>
        <div class="hero-title">👨‍💻 Kaushal Patil</div>
        <h3 style="color:#93c5fd !important;">
            Student Developer
        </h3>
        <p class="muted">
            Curious about science. Learning to code.
            Building ideas into interactive experiences.
        </p>
        <div class="skill">Python</div>
        <div class="skill">Basic Programming</div>
        <div class="skill">Science & Technology</div>
    </div>
    """, unsafe_allow_html=True)

    st.header("About Me")

    st.markdown("""
    <div class="profile-card">
        <div class="profile-label">MY INTRODUCTION</div>
        <p class="muted">
            I am a student at Sane Guruji Nutan Madhyamik
            Vidyalay. I am 14 years old and interested in
            programming, science, and technology.
        </p>
        <p class="muted">
            I am learning programming step by step and
            exploring how technology can turn ideas into
            useful applications and websites.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 💡 Why I Created SciQuest")

    st.markdown("""
    <div class="profile-card">
        <p class="muted">
            I created SciQuest because I want to make science
            easier and more interactive for students.
            My goal is to help learners explore scientific
            concepts by experimenting with values and
            observing results instead of only reading theory.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🛠️ My Current Skills")

    skill_col1, skill_col2 = st.columns(2)

    with skill_col1:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">PROGRAMMING</div>
            <div class="profile-heading">Python</div>
            <p class="muted">
                Learning programming fundamentals, logic,
                variables, conditions, and calculations.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with skill_col2:
        st.markdown("""
        <div class="profile-card">
            <div class="profile-label">DEVELOPMENT</div>
            <div class="profile-heading">Basic Programming</div>
            <p class="muted">
                Developing problem-solving skills by building
                and improving my first interactive application.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 🎯 My Interests")

    st.markdown("""
    <div class="profile-card">
        <span class="skill">💻 Programming</span>
        <span class="skill">🔬 Science</span>
        <span class="skill">⚙️ Technology</span>
        <span class="skill">🌐 App Development</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚀 My Future Goal")

    st.markdown("""
    <div class="profile-card">
        <div class="profile-label">WHAT'S NEXT?</div>
        <div class="profile-heading">
            Build Useful Apps and Websites
        </div>
        <p class="muted">
            I want to continue improving my programming
            knowledge and create applications and websites
            that are useful to people.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧪 My First Science Exhibition Project")

    st.write(
        "SciQuest brings together my interest in programming "
        "and science. It is a project I can keep improving as "
        "I learn new skills and develop new experiments."
    )


# ==========================================
# SPACE EXPLORER
# ==========================================
elif page == "Space Explorer":

    st.header("🪐 Space Explorer")

    st.write(
        "Explore how gravity affects an object's weight "
        "on different worlds in our Solar System."
    )

    # Approximate surface gravity in m/s²
    planets = {
        "Mercury": 3.70,
        "Venus": 8.87,
        "Earth": 9.81,
        "Moon": 1.62,
        "Mars": 3.71,
        "Jupiter": 24.79,
        "Saturn": 10.44,
        "Uranus": 8.69,
        "Neptune": 11.15
    }

    col1, col2 = st.columns(2)

    with col1:
        world = st.selectbox(
            "Choose a world",
            list(planets.keys()),
            index=2
        )

    with col2:
        mass = st.number_input(
            "Object's mass (kg)",
            min_value=0.1,
            max_value=500.0,
            value=60.0,
            step=1.0
        )

    gravity = planets[world]
    weight = mass * gravity

    st.divider()
    st.subheader(f"Your result on {world} 🌌")

    result1, result2, result3 = st.columns(3)

    result1.metric("Mass", f"{mass:.1f} kg")
    result2.metric("Gravity", f"{gravity:.2f} m/s²")
    result3.metric("Weight", f"{weight:.1f} N")

    st.latex(r"W = m \times g")

    st.write(
        f"Weight = {mass:.1f} × {gravity:.2f} "
        f"= {weight:.1f} newtons"
    )

    st.info(
        f"Your object's mass remains {mass:.1f} kg "
        f"on {world}, but its weight changes because "
        f"the surface gravity is different."
    )

    st.caption(
        "Values are approximate. The Moon is included "
        "for comparison, although it is not a planet."
    )

# ==========================================
# SCIENCE QUIZ
# ==========================================
elif page == "Science Quiz":

    st.header("🧠 SciQuest Science Quiz")
    st.write(
        "Choose a difficulty, answer five randomized questions, "
        "and review explanations after submitting."
    )

    question_bank = {
        "Easy": [
            {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Mercury"], "answer": "Mars", "explanation": "Mars looks reddish because iron-rich minerals on its surface have oxidized."},
            {"question": "What is the chemical formula of water?", "options": ["CO2", "O2", "H2O", "NaCl"], "answer": "H2O", "explanation": "A water molecule contains two hydrogen atoms and one oxygen atom."},
            {"question": "What is the SI unit of electric current?", "options": ["Volt", "Ohm", "Watt", "Ampere"], "answer": "Ampere", "explanation": "Electric current is measured in amperes (A)."},
            {"question": "Which gas do plants absorb during photosynthesis?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "answer": "Carbon dioxide", "explanation": "Plants use carbon dioxide, water, and light to make sugars."},
            {"question": "What force attracts objects toward Earth?", "options": ["Friction", "Gravity", "Magnetism", "Buoyancy"], "answer": "Gravity", "explanation": "Gravity is the attractive force between objects that have mass."},
            {"question": "Which star is closest to Earth?", "options": ["Sirius", "The Sun", "Polaris", "Vega"], "answer": "The Sun", "explanation": "The Sun is our nearest star and provides most of Earth's energy."},
            {"question": "Which part of a plant usually absorbs water from soil?", "options": ["Flower", "Leaf", "Root", "Fruit"], "answer": "Root", "explanation": "Roots absorb water and dissolved minerals from the soil."},
            {"question": "At what temperature does pure water freeze at standard pressure?", "options": ["0°C", "10°C", "50°C", "100°C"], "answer": "0°C", "explanation": "Pure water freezes at 0°C at standard atmospheric pressure."},
        ],
        "Medium": [
            {"question": "What is the approximate value of acceleration due to gravity at Earth's surface?", "options": ["1.6 m/s²", "9.8 m/s²", "24.8 m/s²", "100 m/s²"], "answer": "9.8 m/s²", "explanation": "Near Earth's surface, gravitational acceleration is approximately 9.8 m/s²."},
            {"question": "Which law relates voltage, current, and resistance?", "options": ["Newton's law", "Ohm's law", "Kepler's law", "Snell's law"], "answer": "Ohm's law", "explanation": "Ohm's law is V = I × R."},
            {"question": "Which cell structure contains most of a eukaryotic cell's genetic material?", "options": ["Nucleus", "Ribosome", "Cell membrane", "Vacuole"], "answer": "Nucleus", "explanation": "The nucleus contains most of the DNA in a eukaryotic cell."},
            {"question": "Which type of lens converges parallel rays of light?", "options": ["Concave lens", "Convex lens", "Plane glass", "Prism only"], "answer": "Convex lens", "explanation": "A convex lens is converging for parallel rays in air."},
            {"question": "What is the pH of a neutral solution at about 25°C?", "options": ["2", "5", "7", "12"], "answer": "7", "explanation": "At about 25°C, a neutral aqueous solution has pH 7."},
            {"question": "Which blood cells help transport oxygen?", "options": ["Red blood cells", "Platelets", "White blood cells", "Plasma only"], "answer": "Red blood cells", "explanation": "Haemoglobin in red blood cells binds and transports oxygen."},
            {"question": "What is the main gas in Earth's atmosphere?", "options": ["Oxygen", "Carbon dioxide", "Nitrogen", "Hydrogen"], "answer": "Nitrogen", "explanation": "Nitrogen makes up about 78% of Earth's atmosphere."},
            {"question": "Which instrument measures atmospheric pressure?", "options": ["Thermometer", "Barometer", "Ammeter", "Voltmeter"], "answer": "Barometer", "explanation": "A barometer measures atmospheric pressure."},
        ],
        "Hard": [
            {"question": "Which particle has a negative electric charge?", "options": ["Proton", "Neutron", "Electron", "Alpha particle"], "answer": "Electron", "explanation": "Electrons carry a negative elementary electric charge."},
            {"question": "Which relationship describes the reflection of light from a plane mirror?", "options": ["Angle of incidence equals angle of reflection", "Incident angle is always double", "Reflected angle is always 90°", "Angles are unrelated"], "answer": "Angle of incidence equals angle of reflection", "explanation": "Both angles are measured from the normal to the reflecting surface."},
            {"question": "What is the SI unit of power?", "options": ["Joule", "Watt", "Newton", "Pascal"], "answer": "Watt", "explanation": "Power is the rate of transferring or using energy, measured in watts."},
            {"question": "Which process produces most of the Sun's energy?", "options": ["Chemical combustion", "Nuclear fission", "Nuclear fusion", "Radioactive decay only"], "answer": "Nuclear fusion", "explanation": "The Sun releases energy by fusing hydrogen nuclei into helium."},
            {"question": "Which quantity remains the same when an object moves from Earth to the Moon?", "options": ["Weight", "Mass", "Gravitational force", "Apparent weight"], "answer": "Mass", "explanation": "Mass is a measure of matter and does not depend on local gravity."},
            {"question": "What happens to the resistance of a typical metal wire as its temperature rises?", "options": ["It usually increases", "It always becomes zero", "It usually decreases to zero", "It never changes"], "answer": "It usually increases", "explanation": "Higher temperature increases lattice vibrations, usually increasing resistance in metals."},
            {"question": "Which electromagnetic wave has the shortest wavelength among these options?", "options": ["Radio waves", "Microwaves", "Visible light", "Gamma rays"], "answer": "Gamma rays", "explanation": "Gamma rays are at the short-wavelength, high-frequency end of the electromagnetic spectrum."},
            {"question": "Which principle explains why a ship can float?", "options": ["Archimedes' principle", "Ohm's law", "Law of reflection", "Hooke's law"], "answer": "Archimedes' principle", "explanation": "A floating object displaces fluid whose buoyant force balances its weight."},
        ],
    }

    difficulty = st.selectbox(
        "Choose quiz difficulty",
        ["Easy", "Medium", "Hard"],
        key="quiz_difficulty_choice"
    )

    def start_new_quiz_round():
        import random
        selected_difficulty = st.session_state.get("quiz_difficulty_choice", "Easy")
        st.session_state["quiz_questions"] = random.sample(
            question_bank[selected_difficulty], 5
        )
        st.session_state["quiz_active_difficulty"] = selected_difficulty
        st.session_state["quiz_round"] = st.session_state.get("quiz_round", 0) + 1
        st.session_state.pop("quiz_last_result", None)

    if st.button("🎲 Start / Shuffle Quiz", key="start_science_quiz"):
        start_new_quiz_round()

    if "quiz_questions" not in st.session_state:
        st.info("Choose a difficulty above, then click **Start / Shuffle Quiz** to begin.")
    else:
        questions = st.session_state["quiz_questions"]
        active_difficulty = st.session_state.get("quiz_active_difficulty", "Easy")
        st.caption(f"Current round: {active_difficulty} difficulty • 5 questions")

        with st.form("science_quiz_form"):
            answers = []
            round_number = st.session_state.get("quiz_round", 1)

            for i, q in enumerate(questions):
                st.markdown(f"### Question {i + 1}")
                st.write(q["question"])
                selected = st.radio(
                    "Choose your answer:",
                    q["options"],
                    index=None,
                    key=f"quiz_question_{round_number}_{i}"
                )
                answers.append(selected)
                st.divider()

            submitted = st.form_submit_button(
                "Submit Answers 📝",
                use_container_width=True
            )

        if submitted:
            unanswered = sum(answer is None for answer in answers)
            score = sum(
                answer == q["answer"]
                for answer, q in zip(answers, questions)
            )
            percentage = score / len(questions) * 100

            st.session_state["quiz_last_result"] = {
                "score": score,
                "percentage": percentage,
                "answers": answers,
                "questions": questions,
                "unanswered": unanswered,
                "difficulty": active_difficulty,
            }

        if "quiz_last_result" in st.session_state:
            result = st.session_state["quiz_last_result"]
            score = result["score"]
            percentage = result["percentage"]
            st.subheader("🏆 Your Results")
            result_col1, result_col2, result_col3 = st.columns(3)
            result_col1.metric("Your Score", f"{score}/5")
            result_col2.metric("Percentage", f"{percentage:.0f}%")
            result_col3.metric("Difficulty", result["difficulty"])
            st.progress(percentage / 100)

            if score == 5:
                st.success("Perfect score! Outstanding science knowledge! 🎉")
            elif score >= 3:
                st.success("Good work! Review the explanations to learn even more.")
            else:
                st.info("Keep practising! Read the explanations and try another round.")

            if result["unanswered"]:
                st.caption(f"{result['unanswered']} question(s) were left unanswered and counted as incorrect.")

            st.markdown("### 📚 Answer Review")
            for i, q in enumerate(result["questions"]):
                if result["answers"][i] == q["answer"]:
                    st.write(f"✅ **Question {i + 1}: Correct!**")
                else:
                    st.write(f"❌ **Question {i + 1}: Correct answer — {q['answer']}**")
                st.caption(q["explanation"])

            st.button(
                "🔁 Play Another Round",
                key="play_another_quiz",
                on_click=start_new_quiz_round
            )

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    SciQuest · Designed and developed by Kaushal Patil<br>
    A student science exhibition project
</div>
""", unsafe_allow_html=True)
