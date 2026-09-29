# ============================================================
#           SOS - SCHOOL OF SKILLS
#         LEARNING MANAGEMENT SYSTEM (LMS)
#                     theme.py
# ============================================================
#
# The visual design system of the app:
#   - CSS        : one stylesheet (white + SOS red) that re-skins
#                  Streamlit and defines the custom components
#   - *_html()   : small functions that return HTML for hero
#                  banners, KPI cards, course cards, etc.
#
# This file does not import Streamlit, so it is easy to test.
# app.py renders the strings with st.markdown(..., unsafe_allow_html=True).
#
# NOTE: every HTML string is built on ONE line. Markdown treats
# blank lines and 4-space indents as special, which would break
# the layout if the HTML were split across indented lines.
# ============================================================

import html as _html
import re
from datetime import date


# ============================================================
#                        HELPERS
# ============================================================

def esc(value):
    """Escape user-entered text so it is safe inside HTML."""
    return _html.escape(str(value))


def money(amount):
    return f"₹{amount:,}"


def initials(name):
    titles = {"mr", "mrs", "ms", "dr", "miss", "prof"}
    words = [
        w for w in re.split(r"[\s.]+", str(name))
        if w and w.lower() not in titles
    ]
    return "".join(w[0] for w in words[:2]).upper() or "?"


def chip(text, kind=""):
    """Small rounded label. kind: '', green, amber, red, grey."""
    return f'<span class="sos-chip {kind}">{esc(text)}</span>'


FEE_CHIP_KIND = {"Paid": "green", "Partial": "amber", "Unpaid": "red"}


# ============================================================
#                        STYLESHEET
# ============================================================

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Poppins:wght@500;600;700&display=swap');

:root {
    --red: #A31F24;
    --red-dark: #7E1519;
    --red-bright: #C62828;
    --tint: #FBEAEA;
    --tint-2: #FFF6F6;
    --line: #F0D6D7;
    --text: #241414;
    --muted: #6F5F5F;
    --shadow: 0 4px 16px rgba(163, 31, 36, 0.08);
    --shadow-lg: 0 10px 30px rgba(163, 31, 36, 0.18);
}

/* ---------- Base ---------- */
.stApp {
    background: #FFFFFF;
    color: var(--text);
    font-family: 'Inter', 'Segoe UI', sans-serif;
}
h1, h2, h3, h4 {
    font-family: 'Poppins', 'Inter', sans-serif;
    color: var(--text);
    letter-spacing: -0.01em;
}
h2, h3 { color: var(--red); }
hr { border: none; border-top: 1px solid var(--line); margin: 1.4rem 0; }

.block-container {
    padding-top: 1.4rem;
    padding-bottom: 3rem;
    max-width: 1300px;
}

/* Hide Streamlit's own chrome */
#MainMenu, footer, .stDeployButton, [data-testid="stDecoration"] {
    visibility: hidden;
    height: 0;
}
header[data-testid="stHeader"] { background: transparent; }

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"] {
    background: #FFFFFF;
    border-right: 1px solid var(--line);
    box-shadow: 4px 0 24px rgba(163, 31, 36, 0.05);
}
section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    justify-content: flex-start;
    text-align: left;
    background: transparent;
    color: var(--text);
    border: none;
    border-left: 4px solid transparent;
    border-radius: 10px;
    padding: 0.42rem 0.8rem;
    font-weight: 500;
    box-shadow: none;
}
section[data-testid="stSidebar"] .stButton > button p { text-align: left; }
section[data-testid="stSidebar"] .stButton > button:hover {
    background: var(--tint);
    color: var(--red);
    transform: none;
    box-shadow: none;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"],
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] {
    background: var(--tint) !important;
    color: var(--red) !important;
    font-weight: 600;
    border-left: 4px solid var(--red) !important;
    box-shadow: none !important;
}
section[data-testid="stSidebar"] div[data-testid="stExpander"] details {
    border: none !important;
    box-shadow: none !important;
    background: transparent !important;
}
section[data-testid="stSidebar"] details summary {
    font-size: 0.74rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 600;
}

.sos-side-tag {
    text-align: center;
    font-size: 0.68rem;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 600;
    margin: 2px 0 14px;
}
.sos-side-label {
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 600;
    margin: 10px 4px 4px;
}

/* ---------- Buttons ---------- */
.stButton > button,
.stDownloadButton > button,
.stFormSubmitButton > button {
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.15s ease;
    border: 1px solid var(--red);
    color: var(--red);
    background: #FFFFFF;
}
.stButton > button:hover,
.stDownloadButton > button:hover,
.stFormSubmitButton > button:hover {
    border-color: var(--red-dark);
    color: var(--red-dark);
    background: var(--tint);
}
.stButton > button[kind="primary"],
.stButton > button[data-testid="stBaseButton-primary"],
.stDownloadButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(135deg, var(--red-bright), var(--red-dark));
    color: #FFFFFF;
    border: none;
    box-shadow: 0 4px 12px rgba(163, 31, 36, 0.28);
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover,
.stDownloadButton > button:hover,
.stFormSubmitButton > button:hover {
    background: linear-gradient(135deg, var(--red), var(--red-dark));
    color: #FFFFFF;
    transform: translateY(-1px);
    box-shadow: var(--shadow-lg);
}

/* ---------- Inputs ---------- */
[data-testid="stWidgetLabel"] p {
    font-weight: 600;
    font-size: 0.85rem;
    color: var(--text);
}
div[data-baseweb="input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: var(--line) !important;
    background: #FFFFFF;
}
div[data-baseweb="input"]:focus-within,
div[data-baseweb="textarea"]:focus-within,
div[data-baseweb="select"]:focus-within {
    border-color: var(--red) !important;
    box-shadow: 0 0 0 3px rgba(163, 31, 36, 0.12) !important;
}
div[role="radiogroup"] label[data-baseweb="radio"] div:first-child {
    border-color: var(--red) !important;
}

/* ---------- Tabs ---------- */
div[data-baseweb="tab-list"] {
    gap: 6px;
    border-bottom: 1px solid var(--line);
}
button[data-baseweb="tab"] {
    border-radius: 10px 10px 0 0;
    padding: 0.5rem 1rem;
    font-weight: 500;
    color: var(--muted);
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--red);
    font-weight: 600;
    background: var(--tint-2);
}
div[data-baseweb="tab-highlight"] {
    background-color: var(--red);
    height: 3px;
}

/* ---------- Streamlit containers ---------- */
div[data-testid="stExpander"] details {
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    background: #FFFFFF;
    box-shadow: var(--shadow);
}
summary { color: var(--red-dark); font-weight: 600; }

div[data-testid="stForm"] {
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1.3rem 1.4rem;
    background: #FFFFFF;
    box-shadow: var(--shadow);
}
div[data-testid="stDataFrame"] {
    border: 1px solid var(--line);
    border-radius: 14px;
    overflow: hidden;
}
div[data-testid="stPlotlyChart"] {
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 8px;
    background: #FFFFFF;
    box-shadow: var(--shadow);
}
div[data-testid="stAlertContainer"] {
    border-radius: 12px;
    border-left: 4px solid var(--red);
}
div[data-testid="stMetric"] {
    background: var(--tint-2);
    border: 1px solid var(--line);
    border-radius: 14px;
    padding: 12px;
}
div[data-testid="stMetricValue"] { color: var(--red-dark); }

/* ============================================================
   CUSTOM COMPONENTS
   ============================================================ */

/* ---------- Hero banner ---------- */
.sos-hero {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 28px;
    padding: 30px 36px;
    border-radius: 22px;
    color: #FFFFFF;
    background: linear-gradient(120deg, #7E1519 0%, #A31F24 55%, #C62828 100%);
    box-shadow: var(--shadow-lg);
    margin-bottom: 22px;
}
.sos-hero:before {
    content: "";
    position: absolute;
    right: -70px;
    top: -90px;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.08);
}
.sos-hero:after {
    content: "";
    position: absolute;
    right: 140px;
    bottom: -120px;
    width: 230px;
    height: 230px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.06);
}
.sos-hero-logo {
    position: relative;
    z-index: 1;
    background: #FFFFFF;
    border-radius: 18px;
    padding: 12px 18px;
    box-shadow: 0 8px 22px rgba(0, 0, 0, 0.2);
}
.sos-hero-logo img { height: 78px; display: block; }
.sos-hero-text { position: relative; z-index: 1; }
.sos-hero-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 1.85rem;
    line-height: 1.2;
    margin-bottom: 6px;
}
.sos-hero-sub { opacity: 0.93; font-size: 1rem; max-width: 640px; }
.sos-hero-tags { margin-top: 14px; display: flex; flex-wrap: wrap; gap: 8px; }
.sos-hero-tags span {
    background: rgba(255, 255, 255, 0.16);
    border: 1px solid rgba(255, 255, 255, 0.28);
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 500;
}

/* ---------- Page header ---------- */
.sos-ph {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin: 0 0 22px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--line);
}
.sos-ph-left { display: flex; align-items: center; gap: 14px; }
.sos-ph-icon {
    width: 50px;
    height: 50px;
    flex: 0 0 50px;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--tint), #FFFFFF);
    border: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    box-shadow: var(--shadow);
}
.sos-ph-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 700;
    font-size: 1.6rem;
    color: var(--text);
    line-height: 1.15;
}
.sos-ph-sub { color: var(--muted); font-size: 0.92rem; margin-top: 3px; }
.sos-date {
    background: var(--tint);
    color: var(--red-dark);
    border-radius: 999px;
    padding: 6px 14px;
    font-size: 0.8rem;
    font-weight: 600;
    white-space: nowrap;
}

/* ---------- Section title ---------- */
.sos-section {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 28px 0 14px;
    font-family: 'Poppins', sans-serif;
    font-size: 1.12rem;
    font-weight: 600;
    color: var(--text);
}
.sos-section:before {
    content: "";
    width: 5px;
    height: 22px;
    border-radius: 3px;
    background: linear-gradient(180deg, var(--red-bright), var(--red-dark));
}

/* ---------- KPI cards ---------- */
.sos-kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap: 14px;
    margin: 0 0 22px;
}
.sos-kpi {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    gap: 14px;
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 16px 18px 16px 22px;
    box-shadow: var(--shadow);
    transition: all 0.15s ease;
}
.sos-kpi:before {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 5px;
    background: linear-gradient(180deg, var(--red-bright), var(--red-dark));
}
.sos-kpi:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); }
.sos-kpi-icon {
    width: 46px;
    height: 46px;
    flex: 0 0 46px;
    border-radius: 13px;
    background: var(--tint);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
}
.sos-kpi-label {
    font-size: 0.7rem;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: var(--muted);
    font-weight: 600;
}
.sos-kpi-value {
    font-family: 'Poppins', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--red-dark);
    line-height: 1.2;
}
.sos-kpi-sub { font-size: 0.74rem; color: var(--muted); margin-top: 1px; }

/* ---------- Cards & grids ---------- */
.sos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 16px;
    margin-bottom: 8px;
}
.sos-card {
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 18px 20px;
    box-shadow: var(--shadow);
    transition: all 0.15s ease;
}
.sos-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
    border-color: #E4B9BB;
}
.sos-card.static:hover {
    transform: none;
    box-shadow: var(--shadow);
    border-color: var(--line);
}
.sos-card-head {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 10px;
    margin-bottom: 8px;
}
.sos-card-title {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    font-size: 1.02rem;
    color: var(--text);
    line-height: 1.3;
}
.sos-card-sub { color: var(--muted); font-size: 0.8rem; }
.sos-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 6px 16px;
    font-size: 0.84rem;
    color: var(--muted);
    margin: 8px 0;
}
.sos-meta b { color: var(--text); }
.sos-divider { height: 1px; background: var(--line); margin: 12px 0; }
.sos-list-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    padding: 9px 0;
    border-bottom: 1px dashed var(--line);
    font-size: 0.87rem;
}
.sos-list-item:last-child { border-bottom: none; }

.sos-chip {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 999px;
    background: var(--tint);
    color: var(--red-dark);
    font-size: 0.72rem;
    font-weight: 600;
    white-space: nowrap;
}
.sos-chip.green { background: #E7F6EC; color: #1B7F3B; }
.sos-chip.amber { background: #FFF3DC; color: #9A6200; }
.sos-chip.red   { background: #FBE0E1; color: #A31F24; }
.sos-chip.grey  { background: #F1EEEE; color: #5C5050; }
.sos-chips { display: flex; flex-wrap: wrap; gap: 6px; margin: 8px 0; }

/* Progress bar */
.sos-bar {
    height: 8px;
    border-radius: 999px;
    background: var(--tint);
    overflow: hidden;
    margin-top: 6px;
}
.sos-bar > i {
    display: block;
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, var(--red-bright), var(--red-dark));
}
.sos-bar-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.78rem;
    color: var(--muted);
    margin-top: 10px;
}

/* Avatar */
.sos-person { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
.sos-avatar {
    width: 46px;
    height: 46px;
    flex: 0 0 46px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--red-bright), var(--red-dark));
    color: #FFFFFF;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    font-size: 0.95rem;
    box-shadow: 0 4px 10px rgba(163, 31, 36, 0.3);
}

/* Info tiles (institution page) */
.sos-info {
    display: flex;
    align-items: center;
    gap: 14px;
    background: #FFFFFF;
    border: 1px solid var(--line);
    border-radius: 16px;
    padding: 16px 18px;
    box-shadow: var(--shadow);
}
.sos-info-icon {
    width: 46px;
    height: 46px;
    flex: 0 0 46px;
    border-radius: 13px;
    background: var(--tint);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
}
.sos-info-label {
    font-size: 0.7rem;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: var(--muted);
    font-weight: 600;
}
.sos-info-value { font-weight: 600; color: var(--text); word-break: break-word; }

/* Certificate preview */
.sos-cert {
    text-align: center;
    border: 8px double var(--red);
    border-radius: 6px;
    padding: 26px 22px;
    background: #FFFFFF;
    box-shadow: var(--shadow);
    margin: 6px 0 14px;
}
.sos-cert img { height: 62px; margin-bottom: 6px; }
.sos-cert-title {
    font-family: 'Poppins', sans-serif;
    color: var(--red);
    font-size: 1.4rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    margin-bottom: 6px;
}
.sos-cert-name {
    font-family: 'Poppins', sans-serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: var(--text);
    display: inline-block;
    border-bottom: 2px solid var(--red);
    padding: 0 22px 4px;
    margin: 8px 0;
}
.sos-cert-course {
    font-family: 'Poppins', sans-serif;
    font-size: 1.35rem;
    font-weight: 600;
    color: var(--red-dark);
    margin: 6px 0 10px;
}
.sos-cert-meta {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 8px 26px;
    font-size: 0.88rem;
    color: var(--muted);
}
.sos-cert-meta b { color: var(--text); }
.sos-cert-no {
    margin-top: 12px;
    font-size: 0.78rem;
    letter-spacing: 0.05em;
    color: var(--muted);
}

/* Verify result */
.sos-verify {
    border-radius: 18px;
    padding: 20px 24px;
    margin-top: 14px;
    border: 1px solid;
}
.sos-verify.ok  { background: #F1FAF4; border-color: #BFE3CC; }
.sos-verify.bad { background: var(--tint-2); border-color: var(--line); }
.sos-verify-head {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    font-size: 1.1rem;
    margin-bottom: 8px;
}
.sos-verify.ok .sos-verify-head { color: #1B7F3B; }
.sos-verify.bad .sos-verify-head { color: var(--red); }

/* Empty state & footer */
.sos-empty {
    text-align: center;
    padding: 38px 20px;
    border: 2px dashed var(--line);
    border-radius: 18px;
    color: var(--muted);
    background: var(--tint-2);
}
.sos-empty .big { font-size: 2.2rem; margin-bottom: 6px; }
.sos-footer {
    text-align: center;
    color: var(--muted);
    font-size: 0.78rem;
    margin-top: 44px;
    padding-top: 16px;
    border-top: 1px solid var(--line);
}

/* ---------- Small screens ---------- */
@media (max-width: 760px) {
    .sos-hero { flex-direction: column; align-items: flex-start; padding: 22px; }
    .sos-hero-title { font-size: 1.45rem; }
    .sos-ph { flex-direction: column; align-items: flex-start; }
}
"""


# ============================================================
#                    HTML COMPONENT BUILDERS
# ============================================================

def hero_html(logo_uri, title, subtitle, tags):
    tag_html = "".join(f"<span>{esc(t)}</span>" for t in tags)

    return (
        '<div class="sos-hero">'
        f'<div class="sos-hero-logo"><img src="{logo_uri}" alt="SOS logo"></div>'
        '<div class="sos-hero-text">'
        f'<div class="sos-hero-title">{esc(title)}</div>'
        f'<div class="sos-hero-sub">{esc(subtitle)}</div>'
        f'<div class="sos-hero-tags">{tag_html}</div>'
        '</div></div>'
    )


def page_header_html(icon, title, subtitle=""):
    today = date.today().strftime("%a, %d %b %Y")
    sub = f'<div class="sos-ph-sub">{esc(subtitle)}</div>' if subtitle else ""

    return (
        '<div class="sos-ph"><div class="sos-ph-left">'
        f'<div class="sos-ph-icon">{icon}</div>'
        f'<div><div class="sos-ph-title">{esc(title)}</div>{sub}</div>'
        '</div>'
        f'<div class="sos-date">📅 {today}</div></div>'
    )


def section_html(title):
    return f'<div class="sos-section">{esc(title)}</div>'


def kpi_grid_html(items):
    """items: [(icon, label, value, sub), ...] - sub is optional."""

    cards = ""

    for item in items:
        icon, label, value = item[0], item[1], item[2]
        sub = item[3] if len(item) > 3 else ""
        sub_html = f'<div class="sos-kpi-sub">{esc(sub)}</div>' if sub else ""

        cards += (
            '<div class="sos-kpi">'
            f'<div class="sos-kpi-icon">{icon}</div>'
            f'<div><div class="sos-kpi-label">{esc(label)}</div>'
            f'<div class="sos-kpi-value">{esc(value)}</div>{sub_html}</div>'
            '</div>'
        )

    return f'<div class="sos-kpi-grid">{cards}</div>'


def grid_html(cards):
    return f'<div class="sos-grid">{"".join(cards)}</div>'


def empty_state_html(icon, text):
    return (
        f'<div class="sos-empty"><div class="big">{icon}</div>'
        f'<div>{esc(text)}</div></div>'
    )


def info_grid_html(pairs):
    """pairs: [(icon, label, value), ...]"""

    tiles = "".join(
        '<div class="sos-info">'
        f'<div class="sos-info-icon">{icon}</div>'
        f'<div><div class="sos-info-label">{esc(label)}</div>'
        f'<div class="sos-info-value">{esc(value)}</div></div></div>'
        for icon, label, value in pairs
    )

    return f'<div class="sos-grid">{tiles}</div>'


def bar_row_html(title, sub, percent):
    percent = max(0, min(100, percent))

    return (
        '<div style="margin:4px 0 16px">'
        '<div class="sos-bar-label" style="margin-top:0">'
        f'<span><b style="color:#241414">{esc(title)}</b> · {esc(sub)}</span>'
        f'<span><b style="color:#241414">{percent}%</b></span></div>'
        f'<div class="sos-bar"><i style="width:{percent}%"></i></div></div>'
    )


def course_card_html(course):
    filled = course.max_seats - course.available_seats

    if course.max_seats:
        percent = round(filled / course.max_seats * 100)
    else:
        percent = 0

    if course.assigned_faculty:
        faculty = esc(course.assigned_faculty.name)
    else:
        faculty = "Faculty not assigned"

    if course.is_active and course.available_seats > 0:
        status = chip("Open", "green")
    else:
        status = chip("Full", "red")

    return (
        '<div class="sos-card">'
        '<div class="sos-card-head"><div>'
        f'<div class="sos-card-title">{esc(course.title)}</div>'
        f'<div class="sos-card-sub">{esc(course.course_id)} · '
        f'{esc(course.category)}</div></div>{status}</div>'
        '<div class="sos-meta">'
        f'<span>⏱ <b>{course.duration_weeks}</b> weeks</span>'
        f'<span>💰 <b>{money(course.fee)}</b></span>'
        f'<span>📚 <b>{course.total_lessons()}</b> lessons</span></div>'
        f'<div class="sos-meta"><span>🧑‍🏫 {faculty}</span></div>'
        '<div class="sos-bar-label"><span>Seats filled</span>'
        f'<span><b style="color:#241414">{filled}/{course.max_seats}</b></span></div>'
        f'<div class="sos-bar"><i style="width:{percent}%"></i></div>'
        '</div>'
    )


def student_card_html(student):
    rows = ""

    for entry in student.get_enrolled_courses():
        course_id = entry["id"]
        attendance = student.get_attendance_percentage(course_id)
        grade = student.get_grade(course_id)
        fee_status = student.get_fee_status(course_id)

        rows += (
            '<div class="sos-list-item"><span>'
            f'<b>{esc(entry["title"])}</b><br>'
            f'<span class="sos-card-sub">Attendance {attendance}% · '
            f'Grade {esc(grade)}</span></span>'
            f'{chip(fee_status, FEE_CHIP_KIND.get(fee_status, ""))}</div>'
        )

    if not rows:
        rows = '<div class="sos-card-sub">Not enrolled in any courses.</div>'

    balance = student.get_total_balance()
    balance_kind = "red" if balance > 0 else "green"

    return (
        '<div class="sos-card">'
        '<div class="sos-person">'
        f'<div class="sos-avatar">{esc(initials(student.name))}</div>'
        f'<div><div class="sos-card-title">{esc(student.name)}</div>'
        f'<div class="sos-card-sub">{esc(student.student_id)} · '
        f'📞 {esc(student.phone)} · Age {esc(student.age)}</div></div></div>'
        '<div class="sos-chips">'
        f'{chip(str(len(student.get_enrolled_courses())) + " / 3 courses")}'
        f'{chip("Paid " + money(student.get_fees_paid()), "green")}'
        f'{chip("Balance " + money(balance), balance_kind)}</div>'
        f'<div class="sos-divider"></div>{rows}</div>'
    )


def faculty_card_html(faculty):
    attendance = faculty.get_attendance_percentage()
    assigned = faculty.get_assigned_courses()

    if assigned:
        courses = "".join(
            chip(f"{c['id']} · {c['title']}") for c in assigned
        )
    else:
        courses = chip("No courses assigned", "grey")

    return (
        '<div class="sos-card">'
        '<div class="sos-person">'
        f'<div class="sos-avatar">{esc(initials(faculty.name))}</div>'
        f'<div><div class="sos-card-title">{esc(faculty.name)}</div>'
        f'<div class="sos-card-sub">{esc(faculty.faculty_id)} · '
        f'{esc(faculty.department)}</div></div></div>'
        '<div class="sos-meta">'
        f'<span>🎓 <b>{esc(faculty.qualification)}</b></span>'
        f'<span>🕒 <b>{esc(faculty.experience_years)}</b> yrs experience</span>'
        '</div>'
        '<div class="sos-bar-label"><span>Work attendance</span>'
        f'<span><b style="color:#241414">{attendance}%</b></span></div>'
        f'<div class="sos-bar"><i style="width:{attendance}%"></i></div>'
        f'<div class="sos-chips" style="margin-top:12px">{courses}</div>'
        '</div>'
    )


def list_card_html(title, rows_html, empty_text="Nothing to show yet."):
    body = rows_html or f'<div class="sos-card-sub">{esc(empty_text)}</div>'

    return (
        '<div class="sos-card static">'
        f'<div class="sos-card-title">{title}</div>'
        f'<div style="margin-top:8px">{body}</div></div>'
    )


def certificate_preview_html(cert, logo_uri):
    return (
        '<div class="sos-cert">'
        f'<img src="{logo_uri}" alt="SOS logo">'
        '<div class="sos-cert-title">CERTIFICATE OF COMPLETION</div>'
        '<div class="sos-card-sub">This is to certify that</div>'
        f'<div class="sos-cert-name">{esc(cert.student_name)}</div>'
        '<div class="sos-card-sub">has successfully completed the course</div>'
        f'<div class="sos-cert-course">{esc(cert.course_title)}</div>'
        '<div class="sos-cert-meta">'
        f'<span>Grade <b>{esc(cert.grade)}</b></span>'
        f'<span>Attendance <b>{esc(cert.attendance)}%</b></span>'
        f'<span>Issued <b>{esc(cert.issue_date)}</b></span></div>'
        f'<div class="sos-cert-no">Certificate No. {esc(cert.cert_number)}</div>'
        '</div>'
    )


def verify_result_html(cert):
    """Result card for the Verify Certificate page (cert may be None)."""

    if cert is None:
        return (
            '<div class="sos-verify bad">'
            '<div class="sos-verify-head">❌ Certificate not found</div>'
            '<div class="sos-card-sub">No certificate has been issued with '
            'this number. Please check it and try again.</div></div>'
        )

    details = "".join(
        '<div class="sos-list-item">'
        f'<span class="sos-card-sub">{esc(key)}</span>'
        f'<b>{esc(value)}</b></div>'
        for key, value in cert.certificate_details().items()
    )

    return (
        '<div class="sos-verify ok">'
        '<div class="sos-verify-head">✅ Valid certificate — issued by '
        'SOS - School of Skills</div>'
        f'{details}</div>'
    )


def footer_html(institution_name, location):
    return (
        '<div class="sos-footer">'
        f'© {date.today().year} {esc(institution_name)} · {esc(location)} · '
        'Learning Management System</div>'
    )
