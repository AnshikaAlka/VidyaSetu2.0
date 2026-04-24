from __future__ import annotations

import base64
import html
from collections import OrderedDict
from datetime import datetime
from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="VidyaSetu",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)


DEEP_BLUE = "#6A4C93"
MID_BLUE = "#B19CD9"
SOFT_BLUE = "#F3ECFF"
WHITE = "#FFFFFF"
TEXT = "#2D1B4E"
MUTED = "#7A6B8F"
BORDER = "#E2D4F5"
BOARD_EXAM_DATE = datetime(2027, 2, 15, 8, 0, 0)


def apply_theme() -> None:
    st.markdown(
        f"""
        <style>
            :root {{
                --deep-blue: {DEEP_BLUE};
                --mid-blue: {MID_BLUE};
                --soft-blue: {SOFT_BLUE};
                --white: {WHITE};
                --text: {TEXT};
                --muted: {MUTED};
                --border: {BORDER};
            }}

            .stApp {{
                background:
                    radial-gradient(circle at top right, rgba(177, 156, 217, 0.25), transparent 30%),
                    linear-gradient(180deg, #FAF6FF 0%, #F0E6FF 100%);
                color: var(--text);
            }}

            .block-container {{
                padding-top: 1.5rem;
                padding-bottom: 2rem;
            }}

            .hero-card,
            .metric-card,
            .feature-shell {{
                background: rgba(255, 255, 255, 0.95);
                border: 1px solid var(--border);
                border-radius: 22px;
                box-shadow: 0 18px 40px rgba(106, 76, 147, 0.10);
                padding: 1.25rem 1.35rem;
            }}

            .hero-card {{
                padding: 1.75rem;
                background: linear-gradient(135deg, rgba(106, 76, 147, 0.98), rgba(177, 156, 217, 0.95));
                color: white;
                border: none;
            }}

            .hero-title {{
                font-size: 2.2rem;
                font-weight: 700;
                margin-bottom: 0.4rem;
            }}

            .hero-subtitle {{
                font-size: 1rem;
                line-height: 1.6;
                opacity: 0.94;
            }}

            .section-title {{
                font-size: 1.25rem;
                font-weight: 700;
                color: var(--deep-blue);
                margin-bottom: 0.8rem;
            }}

            .mini-label {{
                text-transform: uppercase;
                letter-spacing: 0.08em;
                font-size: 0.74rem;
                font-weight: 700;
                color: #EBDFFB;
                margin-bottom: 0.5rem;
            }}

            .card-title {{
                font-size: 1.08rem;
                font-weight: 700;
                color: var(--deep-blue);
                margin-bottom: 0.25rem;
            }}

            .card-copy {{
                color: var(--muted);
                line-height: 1.55;
            }}

            .countdown-shell {{
                background: rgba(255,255,255,0.14);
                border: 1px solid rgba(255,255,255,0.18);
                border-radius: 18px;
                padding: 1rem;
                margin-top: 1rem;
            }}

            .count-grid {{
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 0.8rem;
                text-align: center;
            }}

            .count-box {{
                background: rgba(255,255,255,0.16);
                border-radius: 16px;
                padding: 0.8rem 0.5rem;
            }}

            .count-value {{
                font-size: 1.65rem;
                font-weight: 800;
            }}

            .count-label {{
                font-size: 0.78rem;
                letter-spacing: 0.08em;
                text-transform: uppercase;
                opacity: 0.85;
            }}

            .gallery-card {{
                background: rgba(255, 255, 255, 0.55);
                backdrop-filter: blur(14px);
                -webkit-backdrop-filter: blur(14px);
                border-radius: 22px;
                border: 1px solid rgba(255, 255, 255, 0.65);
                padding: 1rem;
                box-shadow: 0 18px 38px rgba(106, 76, 147, 0.14),
                            inset 0 1px 0 rgba(255, 255, 255, 0.8);
                height: 100%;
                transition: transform 0.25s ease, box-shadow 0.25s ease;
            }}

            .gallery-card:hover {{
                transform: translateY(-3px);
                box-shadow: 0 26px 48px rgba(106, 76, 147, 0.18),
                            inset 0 1px 0 rgba(255, 255, 255, 0.9);
            }}

            @keyframes vs-fade-in {{
                from {{ opacity: 0; transform: translateY(8px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}

            .stTabs [data-baseweb="tab-panel"],
            .block-container > div > div > div[data-testid="stVerticalBlock"] {{
                animation: vs-fade-in 0.45s ease both;
            }}

            .gallery-card img {{
                border-radius: 16px;
                object-fit: cover;
                width: 100%;
                aspect-ratio: 4/5;
                margin-bottom: 0.9rem;
            }}

            .pill {{
                display: inline-block;
                background: var(--soft-blue);
                color: var(--mid-blue);
                border-radius: 999px;
                padding: 0.3rem 0.7rem;
                font-size: 0.78rem;
                font-weight: 700;
                margin-bottom: 0.6rem;
            }}

            .cta-link {{
                display: inline-block;
                width: 100%;
                text-align: center;
                text-decoration: none;
                color: white !important;
                background: linear-gradient(135deg, var(--deep-blue), var(--mid-blue));
                border-radius: 14px;
                padding: 0.7rem 0.9rem;
                font-weight: 700;
                margin-top: 0.85rem;
            }}

            .chat-bubble-user,
            .chat-bubble-guide {{
                padding: 0.9rem 1rem;
                border-radius: 16px;
                margin-bottom: 0.75rem;
                max-width: 85%;
            }}

            .chat-bubble-user {{
                background: linear-gradient(135deg, var(--deep-blue), var(--mid-blue));
                color: white;
                margin-left: auto;
            }}

            .chat-bubble-guide {{
                background: white;
                border: 1px solid var(--border);
                color: var(--text);
            }}

            .chat-bubble-bot {{
                padding: 0.9rem 1rem;
                border-radius: 16px;
                margin-bottom: 0.75rem;
                max-width: 85%;
                background: linear-gradient(135deg, #F3ECFF, #E5D6FA);
                border: 1px solid #C9B6E8;
                color: var(--text);
                box-shadow: 0 6px 14px rgba(106, 76, 147, 0.10);
            }}

            section[data-testid="stSidebar"] {{
                background: linear-gradient(180deg, #F5EEFF 0%, #E8DCFB 100%);
                border-right: 1px solid var(--border);
            }}

            section[data-testid="stSidebar"] * {{
                color: var(--text);
            }}

            .stButton > button,
            .stDownloadButton > button,
            .stFormSubmitButton > button {{
                background: linear-gradient(135deg, var(--mid-blue), #C9B6E8);
                color: white !important;
                border: none;
                border-radius: 14px;
                font-weight: 700;
                padding: 0.6rem 1rem;
                box-shadow: 0 8px 18px rgba(106, 76, 147, 0.18);
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }}

            .stButton > button:hover,
            .stDownloadButton > button:hover,
            .stFormSubmitButton > button:hover {{
                transform: translateY(-1px);
                box-shadow: 0 12px 22px rgba(106, 76, 147, 0.25);
                background: linear-gradient(135deg, var(--deep-blue), var(--mid-blue));
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_state() -> None:
    if "uploaded_books" not in st.session_state:
        st.session_state.uploaded_books = []
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = [
            {
                "sender": "Mitra",
                "text": "Namaste! This is the Parishad lounge. Ask a doubt, share a win, or start a study sprint together.",
            }
        ]


def book_cover_data_uri(uploaded_file) -> str:
    raw = uploaded_file.getvalue()
    mime = uploaded_file.type or "image/png"
    encoded = base64.b64encode(raw).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def render_countdown_widget() -> None:
    target = BOARD_EXAM_DATE.isoformat()
    components.html(
        f"""
        <div class="countdown-shell">
            <div style="font-weight:700; margin-bottom:0.8rem;">Board Exam Countdown</div>
            <div class="count-grid">
                <div class="count-box">
                    <div class="count-value" id="days">0</div>
                    <div class="count-label">Days</div>
                </div>
                <div class="count-box">
                    <div class="count-value" id="hours">0</div>
                    <div class="count-label">Hours</div>
                </div>
                <div class="count-box">
                    <div class="count-value" id="minutes">0</div>
                    <div class="count-label">Minutes</div>
                </div>
                <div class="count-box">
                    <div class="count-value" id="seconds">0</div>
                    <div class="count-label">Seconds</div>
                </div>
            </div>
            <div style="margin-top:0.75rem; font-size:0.82rem; opacity:0.86;">
                Target set for 15 February 2027, 08:00 AM.
            </div>
        </div>
        <script>
            const targetDate = new Date("{target}").getTime();
            const ids = ["days", "hours", "minutes", "seconds"];
            function updateCountdown() {{
                const now = new Date().getTime();
                const gap = Math.max(0, targetDate - now);
                const days = Math.floor(gap / (1000 * 60 * 60 * 24));
                const hours = Math.floor((gap / (1000 * 60 * 60)) % 24);
                const minutes = Math.floor((gap / (1000 * 60)) % 60);
                const seconds = Math.floor((gap / 1000) % 60);
                const values = [days, hours, minutes, seconds];
                ids.forEach((id, index) => {{
                    document.getElementById(id).innerText = values[index];
                }});
            }}
            updateCountdown();
            setInterval(updateCountdown, 1000);
        </script>
        """,
        height=230,
    )


def render_home() -> None:
    col1, col2 = st.columns([1.35, 1], gap="large")

    with col1:
        st.markdown(
            """
            <div class="hero-card">
                <div class="mini-label">VidyaSetu Learning Hub</div>
                <div class="hero-title">Bridge your study flow with clarity, rhythm, and confidence.</div>
                <div class="hero-subtitle">
                    VidyaSetu brings together your visual library, planning tools, peer exchange, and live help
                    inside one focused pastel workspace built for board exam preparation.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="feature-shell">
                <div class="section-title"><span style="font-size:1.55rem; margin-right:0.5rem;">⏳</span>Pariksha Kala</div>
            """,
            unsafe_allow_html=True,
        )
        render_countdown_widget()
        st.markdown("</div>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3, gap="large")
    metrics = [
        ("Kosh Pustakein", "3+", "Curated visual resources ready to download"),
        ("Sarathi Kriya", "2", "Smart AI tools for exam planning and instant flashcards"),
        ("Parishad Flow", "Live", "Session chat stays active while you study"),
    ]
    for col, metric in zip((m1, m2, m3), metrics):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="card-title">{metric[0]}</div>
                    <div style="font-size:2rem; font-weight:800; color:{DEEP_BLUE}; margin:0.35rem 0;">{metric[1]}</div>
                    <div class="card-copy">{metric[2]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def default_books() -> list[dict[str, str]]:
    return [
        {
            "title": "Vigyan Pravesh",
            "subject": "Science",
            "image": "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=900&q=80",
            "download": "https://ncert.nic.in/textbook.php",
        },
        {
            "title": "Ganita Darpan",
            "subject": "Mathematics",
            "image": "https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&w=900&q=80",
            "download": "https://ncert.nic.in/textbook.php",
        },
        {
            "title": "Angla Patha",
            "subject": "English",
            "image": "https://images.unsplash.com/photo-1455390582262-044cdead277a?auto=format&fit=crop&w=900&q=80",
            "download": "https://ncert.nic.in/textbook.php",
        },
    ]


def render_book_card(book: dict[str, str]) -> None:
    st.markdown(
        f"""
        <div class="gallery-card">
            <img src="{html.escape(book['image'])}" alt="{html.escape(book['title'])}" />
            <div class="pill">{html.escape(book['subject'])}</div>
            <div class="card-title">{html.escape(book['title'])}</div>
            <div class="card-copy">Visual edition resource card with one-click access.</div>
            <a class="cta-link" href="{html.escape(book['download'])}" target="_blank">Download</a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_kosh() -> None:
    st.markdown(
        """
        <div class="feature-shell">
            <div class="section-title"><span style="font-size:1.55rem; margin-right:0.5rem;">🎒</span>Kosh: The Visual Vault</div>
            <div class="card-copy">Browse your core books as a visual gallery, then add custom covers and titles to build your own study shelf.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.expander("Granth Aropana - Upload your own book", expanded=True):
        upload_col1, upload_col2 = st.columns([1.1, 1], gap="large")
        with upload_col1:
            custom_title = st.text_input("Pustak Title", placeholder="e.g. Objective Biology Capsule")
            custom_subject = st.text_input("Subject Name", placeholder="e.g. Biology")
        with upload_col2:
            custom_image = st.file_uploader(
                "Book Cover Image",
                type=["png", "jpg", "jpeg", "webp"],
                accept_multiple_files=False,
            )

        if st.button("Upload to Kosh", use_container_width=True):
            if not custom_title or not custom_subject or not custom_image:
                st.warning("Please add a title, subject, and cover image before uploading.")
            else:
                st.session_state.uploaded_books.append(
                    {
                        "title": custom_title.strip(),
                        "subject": custom_subject.strip(),
                        "image": book_cover_data_uri(custom_image),
                        "download": book_cover_data_uri(custom_image),
                    }
                )
                st.success("Your book has been added to the Kosh gallery for this session.")

    all_books = default_books() + st.session_state.uploaded_books
    cols = st.columns(3, gap="large")
    for idx, book in enumerate(all_books):
        with cols[idx % 3]:
            render_book_card(book)


def generate_study_plan(topics_text: str) -> list[tuple[str, int, str]]:
    raw_topics = [line.strip("-• ").strip() for line in topics_text.splitlines() if line.strip()]
    ordered_topics = list(OrderedDict.fromkeys(raw_topics))
    if not ordered_topics:
        return []

    total_minutes = 180
    remaining = total_minutes
    plan = []
    for index, topic in enumerate(ordered_topics):
        if index == len(ordered_topics) - 1:
            minutes = remaining
        else:
            topics_left = len(ordered_topics) - index
            minutes = max(20, remaining // topics_left)
        remaining -= minutes
        focus = "Concept build" if index == 0 else "Active recall + practice"
        if index == len(ordered_topics) - 1:
            focus = "Rapid revision + self-test"
        plan.append((topic, minutes, focus))
    return plan


def notes_to_flashcards(notes: str) -> list[tuple[str, str]]:
    lines = [line.strip() for line in notes.splitlines() if line.strip()]
    flashcards = []

    for line in lines:
        if ":" in line:
            front, back = line.split(":", 1)
            flashcards.append((f"What is {front.strip()}?", back.strip()))
        elif " is " in line:
            subject, detail = line.split(" is ", 1)
            flashcards.append((f"What is {subject.strip()}?", detail.strip()))
        elif " are " in line:
            subject, detail = line.split(" are ", 1)
            flashcards.append((f"What are {subject.strip()}?", detail.strip()))
        else:
            flashcards.append((f"What should you remember about: {line}?", line))

    return flashcards[:12]


def render_sarathi() -> None:
    st.markdown(
        """
        <div class="feature-shell">
            <div class="section-title"><span style="font-size:1.55rem; margin-right:0.5rem;">🧠</span>Sarathi: AI Guide</div>
            <div class="card-copy">Convert rough topics into a guided 3-hour session and turn messy notes into revision-ready flashcards.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    planner_tab, flashcard_tab, sample_tab = st.tabs(["Adhyayan Yojana", "Smriti Patra", "Pratidarpana"])

    with planner_tab:
        st.subheader("Study Planner")
        topics_text = st.text_area(
            "Enter syllabus topics",
            height=180,
            placeholder="Chemical reactions\nAcids, bases and salts\nMetals and non-metals\nCarbon compounds",
        )
        if st.button("Generate 3-Hour Plan", use_container_width=True):
            plan = generate_study_plan(topics_text)
            if not plan:
                st.warning("Please enter at least one topic.")
            else:
                st.success("Sarathi has generated your 3-hour study flow.")
                for idx, (topic, minutes, focus) in enumerate(plan, start=1):
                    st.markdown(
                        f"""
                        <div class="metric-card" style="margin-bottom:0.8rem;">
                            <div class="pill">Segment {idx}</div>
                            <div class="card-title">{html.escape(topic)}</div>
                            <div class="card-copy"><strong>{minutes} minutes</strong> allocated for {html.escape(focus)}.</div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

    with flashcard_tab:
        st.subheader("Flashcard Generator")
        notes_text = st.text_area(
            "Paste your notes",
            height=220,
            placeholder="Mitochondria: powerhouse of the cell\nDemocracy is a system of government by elected representatives",
        )
        if st.button("Create Flashcards", use_container_width=True):
            cards = notes_to_flashcards(notes_text)
            if not cards:
                st.warning("Please add notes to convert into flashcards.")
            else:
                st.success("Smriti Patra cards are ready.")
                for idx, (question, answer) in enumerate(cards, start=1):
                    with st.container(border=True):
                        st.markdown(f"**Q{idx}. {question}**")
                        st.write(answer)

    with sample_tab:
        st.subheader("Pratidarpana — Official CBSE Sample Papers")
        st.markdown(
            """
            <div class="card-copy" style="margin-bottom:0.9rem;">
                Pick a subject to open the latest official Class 10 sample paper from CBSE Academic.
            </div>
            """,
            unsafe_allow_html=True,
        )
        sample_papers = {
            "Mathematics": "https://cbseacademic.nic.in/web_material/SQP/ClassX_2023_24/Maths-Standard-SQP.pdf",
            "Science": "https://cbseacademic.nic.in/web_material/SQP/ClassX_2023_24/Science-SQP.pdf",
            "English": "https://cbseacademic.nic.in/web_material/SQP/ClassX_2023_24/English-Lang-Lit-SQP.pdf",
            "Social Science (SST)": "https://cbseacademic.nic.in/web_material/SQP/ClassX_2023_24/Social-Science-SQP.pdf",
        }
        selected_subject = st.selectbox("Choose a subject", list(sample_papers.keys()))
        selected_url = sample_papers[selected_subject]
        st.markdown(
            f"""
            <div class="metric-card" style="margin-top:0.6rem;">
                <div class="pill">CBSE Academic</div>
                <div class="card-title">{html.escape(selected_subject)} — Sample Question Paper</div>
                <div class="card-copy">Official PDF hosted on cbseacademic.nic.in. Opens in a new tab.</div>
                <a class="cta-link" href="{html.escape(selected_url)}" target="_blank">Open Sample Paper</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            "<div class='section-title' style='margin-top:1.4rem;'>All Subjects</div>",
            unsafe_allow_html=True,
        )
        link_cols = st.columns(2, gap="large")
        for idx, (subject, url) in enumerate(sample_papers.items()):
            with link_cols[idx % 2]:
                st.markdown(
                    f"""
                    <div class="metric-card" style="margin-bottom:0.8rem;">
                        <div class="card-title">{html.escape(subject)}</div>
                        <a class="cta-link" href="{html.escape(url)}" target="_blank">Download PDF</a>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def marketplace_items() -> list[dict[str, str]]:
    return [
        {
            "title": "Class 10 Science Handbook",
            "price": "₹220",
            "condition": "Gently used",
            "seller": "Aarav",
            "phone": "919039100413",
            "image": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?auto=format&fit=crop&w=900&q=80",
        },
        {
            "title": "Mathematics Practice Set",
            "price": "₹180",
            "condition": "Annotated",
            "seller": "Meera",
            "phone": "919039100413",
            "image": "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=900&q=80",
        },
        {
            "title": "English Writing Guide",
            "price": "₹150",
            "condition": "Like new",
            "seller": "Kabir",
            "phone": "919039100413",
            "image": "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=900&q=80",
        },
    ]


def render_vinimaya() -> None:
    st.markdown(
        """
        <div class="feature-shell">
            <div class="section-title"><span style="font-size:1.55rem; margin-right:0.5rem;">🛒</span>Vinimaya: Marketplace</div>
            <div class="card-copy">Explore second-hand books from fellow learners and jump straight into a pre-filled WhatsApp conversation with the seller.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="large")
    for idx, item in enumerate(marketplace_items()):
        message = quote(f"Namaste {item['seller']}, I would like to buy '{item['title']}' listed on VidyaSetu.")
        wa_link = f"https://wa.me/{item['phone']}?text={message}"
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div class="gallery-card">
                    <img src="{html.escape(item['image'])}" alt="{html.escape(item['title'])}" />
                    <div class="pill">{html.escape(item['condition'])}</div>
                    <div class="card-title">{html.escape(item['title'])}</div>
                    <div class="card-copy">
                        Seller: {html.escape(item['seller'])}<br/>
                        Price: <strong>{html.escape(item['price'])}</strong>
                    </div>
                    <a class="cta-link" href="{wa_link}" target="_blank">Buy via WhatsApp</a>
                </div>
                """,
                unsafe_allow_html=True,
            )


SMART_BOT_HINTS = [
    ("photosynthesis", "Photosynthesis happens in chloroplasts: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂. Light reactions make ATP and NADPH; the Calvin cycle uses them to fix carbon."),
    ("mitochondria", "Mitochondria are the powerhouse of the cell — they generate ATP via oxidative phosphorylation in the inner membrane (cristae)."),
    ("newton", "Newton's three laws: (1) inertia, (2) F = m·a, (3) every action has an equal and opposite reaction. Most mechanics problems start by drawing a free-body diagram."),
    ("gravity", "Universal gravitation: F = G·m₁·m₂ / r². On Earth's surface, g ≈ 9.8 m/s². Remember weight = mass × g."),
    ("trigonometry", "Core identity: sin²θ + cos²θ = 1. Memorise sin/cos/tan of 0°, 30°, 45°, 60°, 90° — most problems collapse to these."),
    ("quadratic", "Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a. The discriminant b² - 4ac tells you how many real roots exist."),
    ("algebra", "When stuck on algebra, isolate the variable step-by-step and check by substituting the answer back into the original equation."),
    ("calculus", "Derivatives measure rate of change; integrals measure accumulation. Practice the power rule and chain rule until they feel automatic."),
    ("democracy", "Democracy = government by the people. Key features: free elections, rule of law, fundamental rights, and an independent judiciary."),
    ("constitution", "The Indian Constitution came into effect on 26 January 1950. Remember the Preamble keywords: Sovereign, Socialist, Secular, Democratic, Republic."),
    ("history", "For history, build a timeline first, then layer causes and consequences on top. Dates without context are hard to retain."),
    ("geography", "Use map sketches while revising — locating features visually almost always beats memorising names from a list."),
    ("essay", "Essay structure that scores: hook → thesis → 2-3 body paragraphs (each with claim + evidence + analysis) → reflective conclusion."),
    ("grammar", "Tip: read the sentence aloud. If it sounds wrong, it usually is. Then identify the rule (tense agreement, subject-verb, article use)."),
    ("english", "For comprehension, skim the questions first, then read the passage with a purpose — you'll spot the answers faster."),
    ("acid", "Acids release H⁺ ions in solution, bases release OH⁻. Stronger acid → lower pH. Neutralisation: acid + base → salt + water."),
    ("chemistry", "Balance equations by atoms, not by feel: list each element on both sides and adjust coefficients one at a time."),
    ("physics", "When you see a physics problem, list (1) what's given, (2) what's asked, (3) which formula links them. Units must match."),
    ("biology", "For biology diagrams, label parts with arrows and add one-line functions next to each — recall improves dramatically."),
    ("revision", "Use active recall over re-reading. Close the book and try to write the concept from memory, then check what you missed."),
    ("memory", "Spaced repetition beats cramming: revise after 1 day, 3 days, 7 days, 14 days. Smriti Patra flashcards are perfect for this."),
    ("stress", "If you feel overwhelmed, try the 4-7-8 breathing pattern for two minutes, then start with the easiest topic to build momentum."),
    ("time", "Try the 90/20 rule: 90 minutes of focused study, 20 minutes break. The break is when your brain consolidates what you learned."),
    ("sleep", "Sleep before an exam matters more than one extra hour of revision. Memory consolidation happens during deep sleep."),
]

GENERIC_HINTS = [
    "Break the topic into 3 smaller sub-questions and tackle them one at a time — clarity comes from decomposition.",
    "Try teaching this concept aloud to an imaginary classmate. If you stumble, that's exactly the gap to revise.",
    "Sketch a quick diagram or mind-map. Visual encoding makes recall under exam pressure much faster.",
    "Open Sarathi's Smriti Patra and turn this doubt into a flashcard so it sticks for the long term.",
    "Look for the 'why' behind the rule, not just the rule. Concepts you understand stay; rules you memorise fade.",
]


def generate_smart_insight(text: str) -> str:
    lower = text.lower()
    for keyword, hint in SMART_BOT_HINTS:
        if keyword in lower:
            return hint
    index = sum(ord(ch) for ch in lower) % len(GENERIC_HINTS)
    return GENERIC_HINTS[index]


def is_question(text: str) -> bool:
    lower = text.strip().lower()
    if lower.endswith("?"):
        return True
    starters = ("what", "why", "how", "when", "where", "which", "who", "explain", "define", "is ", "are ", "can ", "does ", "do ")
    return lower.startswith(starters)


def render_chat_message(sender: str, text: str) -> None:
    if sender == "You":
        css_class = "chat-bubble-user"
    elif sender == "Mitra Bot":
        css_class = "chat-bubble-bot"
    else:
        css_class = "chat-bubble-guide"
    badge = ""
    if sender == "Mitra Bot":
        badge = '<span style="background:#B39DDB;color:#FFFFFF;border-radius:999px;padding:0.12rem 0.55rem;font-size:0.68rem;font-weight:700;margin-left:0.45rem;letter-spacing:0.04em;">SMART-BOT</span>'
    st.markdown(
        f"""
        <div class="{css_class}">
            <div style="font-weight:700; margin-bottom:0.25rem;">{html.escape(sender)}{badge}</div>
            <div>{html.escape(text)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_parishad() -> None:
    left, right = st.columns([1.5, 1], gap="large")

    with left:
        st.markdown(
            """
            <div class="feature-shell">
                <div class="section-title"><span style="font-size:1.55rem; margin-right:0.5rem;">🤝</span>Parishad: Study Lounge</div>
                <div class="card-copy">A lightweight real-time session chat powered by Streamlit session state. Your conversation stays alive while the session stays open.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for message in st.session_state.chat_messages:
            render_chat_message(message["sender"], message["text"])

        chat_text = st.text_input("Send a message", placeholder="Ask a doubt or share your next goal...")
        if st.button("Post to Parishad", use_container_width=True):
            cleaned = chat_text.strip()
            if cleaned:
                st.session_state.chat_messages.append({"sender": "You", "text": cleaned})
                insight = generate_smart_insight(cleaned)
                if is_question(cleaned):
                    bot_reply = f"That's a great question! While we wait for a peer to join, here is a quick insight: {insight}"
                else:
                    bot_reply = f"Thanks for sharing. While the lounge picks up, here is a quick insight to keep your momentum: {insight}"
                st.session_state.chat_messages.append({"sender": "Mitra Bot", "text": bot_reply})
                st.session_state.chat_messages.append(
                    {
                        "sender": "Mitra",
                        "text": "Other learners can chime in here — your message is now visible in the lounge.",
                    }
                )
                st.rerun()

    with right:
        st.markdown(
            """
            <div class="hero-card">
                <div class="mini-label">Live Collaboration</div>
                <div class="card-title" style="color:white; font-size:1.4rem;">Join a doubt-solving room instantly.</div>
                <div class="hero-subtitle">Use Jitsi for a frictionless live study session with peers, mentors, or a focused revision group.</div>
                <a class="cta-link" href="https://jit.si" target="_blank" style="margin-top:1rem;">Join Live Doubt Session</a>
            </div>
            """,
            unsafe_allow_html=True,
        )


def main() -> None:
    apply_theme()
    initialize_state()

    with st.sidebar:
        st.markdown(
            f"""
            <div style="padding:0.4rem 0 1rem 0; text-align:center;">
                <div style="font-size:1.9rem; font-weight:800; letter-spacing:0.02em;
                            background: linear-gradient(90deg, #6A4C93 0%, #B39DDB 55%, #E2D4F5 100%);
                            -webkit-background-clip: text; background-clip: text;
                            -webkit-text-fill-color: transparent; color: transparent;">VIDYASETU</div>
                <div style="display:inline-block; margin-top:0.55rem; padding:0.4rem 0.95rem;
                            background:#B39DDB; color:#FFFFFF; border-radius:999px;
                            font-weight:700; font-size:0.82rem; letter-spacing:0.04em;
                            box-shadow:0 6px 14px rgba(106,76,147,0.20);">
                    Bridging Effort to Excellence
                </div>
                <div style="margin-top:0.45rem; color:{MUTED}; font-size:0.78rem; font-style:italic;">
                    श्रमं प्रति साफल्यम्
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        page = st.radio(
            "Navigate",
            ["Griha", "Kosh", "Sarathi", "Vinimaya", "Parishad"],
            label_visibility="collapsed",
        )

    if page == "Griha":
        render_home()
    elif page == "Kosh":
        render_kosh()
    elif page == "Sarathi":
        render_sarathi()
    elif page == "Vinimaya":
        render_vinimaya()
    elif page == "Parishad":
        render_parishad()


if __name__ == "__main__":
    main()
