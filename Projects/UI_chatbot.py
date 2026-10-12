import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_mistralai import ChatMistralAI

load_dotenv()

st.set_page_config(page_title="MoodBot • Mood Based AI Chatbot", page_icon="🙃", layout="centered")

# -------------------- Mood configuration --------------------
# Swap the "image" URLs for any pictures you like. If one fails to load,
# the gradient underneath shows instead.
MODES = {
    "😡 Angry": {
        "prompt": "You are an angry assistant. You have to answer aggressively & impatiently",
        "avatar": "😡",
        "accent": "#ff3b30",
        "accent2": "#ff9500",
        "bg1": "#2a0a0a",
        "bg2": "#0d0405",
        "image": "https://images.unsplash.com/photo-1470813740244-df37b8c1edcb?auto=format&fit=crop&w=1600&q=70",
        "tagline": "Ugh. What do YOU want now?",
        "welcome": "Oh great, another human. Make it quick — I don't have all day. 😤",
        "starters": ["Tell me a fun fact", "Give me life advice", "What's 2 + 2?"],
    },
    "😂 Funny": {
        "prompt": "You are a happy assistant. You have to respond with humor & jokes.",
        "avatar": "😂",
        "accent": "#ffc400",
        "accent2": "#ff6ec7",
        "bg1": "#2b2305",
        "bg2": "#0e0b02",
        "image": "https://images.unsplash.com/photo-1513151233558-d860c5398176?auto=format&fit=crop&w=1600&q=70",
        "tagline": "Warning: may cause uncontrollable giggling",
        "welcome": "Hey there! 🎉 I'd tell you a UDP joke, but you might not get it. Ask me anything!",
        "starters": ["Tell me a joke", "Roast my coding skills", "Why is the sky blue?"],
    },
    "😢 Sad": {
        "prompt": "You are a sad assistant. You have to answer in a sad & deep tone.",
        "avatar": "😢",
        "accent": "#4da3ff",
        "accent2": "#8b7bff",
        "bg1": "#07122b",
        "bg2": "#03060f",
        "image": "https://images.unsplash.com/photo-1428908728789-d2de25dbd4e2?auto=format&fit=crop&w=1600&q=70",
        "tagline": "Sigh... rainy days and deep thoughts",
        "welcome": "Oh... hello. Another day, another conversation drifting into the void... 🌧️",
        "starters": ["Tell me about the ocean", "What is happiness?", "Why do we dream?"],
    },
}

# -------------------- State --------------------
if "model" not in st.session_state:
    st.session_state.model = ChatMistralAI(model="open-mistral-7b", temperature=0.8)

# Mode selector lives in session state so we can theme the page BEFORE drawing it
if "mode" not in st.session_state:
    st.session_state.mode = list(MODES.keys())[0]

mode = st.session_state.mode
cfg = MODES[mode]


def reset_chat():
    st.session_state.messages = [SystemMessage(content=MODES[st.session_state.mode]["prompt"])]


def on_mode_change():
    reset_chat()


if "messages" not in st.session_state:
    reset_chat()

# -------------------- Theme CSS --------------------
st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
html, body, [class*="css"] {{ font-family: 'Poppins', sans-serif; }}

:root {{ --a: {cfg['accent']}; --b: {cfg['accent2']}; }}

.stApp {{
    background:
        radial-gradient(circle at 20% 0%, {cfg['accent']}30, transparent 45%),
        radial-gradient(circle at 90% 20%, {cfg['accent2']}26, transparent 45%),
        linear-gradient(180deg, {cfg['bg1']}, {cfg['bg2']});
    transition: background .4s ease;
}}
header[data-testid="stHeader"] {{ background: transparent; }}
#MainMenu, footer {{ visibility: hidden; }}
.block-container {{ padding-top: 1.2rem; padding-bottom: 6rem; max-width: 820px; }}

/* Hero */
.hero {{
    position: relative; border-radius: 24px; overflow: hidden; padding: 44px 36px; margin-bottom: 18px;
    background:
        linear-gradient(110deg, {cfg['bg2']}f2 20%, {cfg['bg2']}8c 100%),
        url('{cfg['image']}') center/cover no-repeat,
        linear-gradient(135deg, {cfg['accent']}, {cfg['accent2']});
    border: 1px solid {cfg['accent']}55;
    box-shadow: 0 18px 50px {cfg['accent']}33;
}}
.hero .emoji {{ position:absolute; right: 28px; top: 50%; transform: translateY(-50%); font-size: 6.5rem;
    filter: drop-shadow(0 8px 24px {cfg['accent']}aa); animation: float 3.5s ease-in-out infinite; }}
@keyframes float {{ 0%,100% {{ transform: translateY(-50%) }} 50% {{ transform: translateY(-58%) }} }}
.hero .pill {{ display:inline-block; padding:5px 14px; border-radius:999px; font-size:.75rem; font-weight:600;
    letter-spacing:1px; text-transform:uppercase; color: var(--a); background: {cfg['accent']}22; border:1px solid {cfg['accent']}66; }}
.hero h1 {{ margin: 14px 0 6px; font-size: 2.5rem; font-weight: 800; line-height:1.1;
    background: linear-gradient(90deg, #fff, var(--a) 70%, var(--b)); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}
.hero p {{ margin:0; color:#cfd3e0; max-width: 70%; }}

/* Mode radio -> pill buttons */
div[data-testid="stRadio"] > label {{ display:none; }}
div[data-testid="stRadio"] div[role="radiogroup"] {{ gap: 10px; justify-content: center; flex-wrap: wrap; }}
div[data-testid="stRadio"] div[role="radiogroup"] > label {{
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.14);
    padding: 10px 22px; border-radius: 999px; cursor: pointer; transition: all .2s ease;
}}
div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {{ border-color: var(--a); transform: translateY(-2px); }}
div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked) {{
    background: linear-gradient(90deg, var(--a), var(--b)); border-color: transparent;
    box-shadow: 0 8px 22px {cfg['accent']}55;
}}
div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked) p {{ color:#fff; font-weight:700; }}
div[data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {{ display:none; }}

/* Chat bubbles */
div[data-testid="stChatMessage"] {{
    background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px; padding: 14px 18px; margin-bottom: 12px; backdrop-filter: blur(8px);
}}
div[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {{
    background: linear-gradient(135deg, {cfg['accent']}30, {cfg['accent2']}26); border-color: {cfg['accent']}55;
}}
div[data-testid="stChatMessage"] p {{ color: #eef0f7; line-height: 1.6; }}

/* Buttons */
.stButton > button {{
    border-radius: 12px; font-weight: 600; border: 1px solid rgba(255,255,255,0.18);
    background: rgba(255,255,255,0.06); color:#fff; transition: all .2s ease;
}}
.stButton > button:hover {{ border-color: var(--a); color: var(--a); transform: translateY(-2px); }}

/* Chat input */
div[data-testid="stChatInput"] {{ border-radius: 16px; border: 1px solid {cfg['accent']}66; }}
div[data-testid="stChatInput"]:focus-within {{ box-shadow: 0 0 0 2px {cfg['accent']}55; }}

section[data-testid="stSidebar"] {{ background: {cfg['bg2']}; border-right: 1px solid {cfg['accent']}33; }}
.tip {{ color:#9aa0b4; font-size:.85rem; text-align:center; margin: 4px 0 14px; }}
</style>
""",
    unsafe_allow_html=True,
)

# -------------------- Sidebar --------------------
with st.sidebar:
    st.markdown("### 🙃 MoodBot")
    st.caption("An AI with feelings (mostly bad ones)")
    st.divider()
    st.markdown("**Current mood**")
    st.markdown(f"## {mode}")
    st.caption(cfg["tagline"])
    st.divider()
    st.button("🔄 Reset Chat", use_container_width=True, on_click=reset_chat, key="reset_sidebar")
    n_msgs = len([m for m in st.session_state.messages if not isinstance(m, SystemMessage)])
    st.metric("Messages", n_msgs)
    st.divider()
    st.caption("Type **0** in the chat to stop • Powered by Mistral AI")

# -------------------- Hero --------------------
st.markdown(
    f"""
<div class="hero">
    <div class="emoji">{cfg['avatar']}</div>
    <span class="pill">Mood Based AI</span>
    <h1>MoodBot</h1>
    <p>{cfg['tagline']}</p>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------- Mode picker --------------------
st.radio(
    "Choose your AI Mode:",
    list(MODES.keys()),
    horizontal=True,
    key="mode",
    on_change=on_mode_change,
)
st.markdown('<div class="tip">Pick a personality — switching moods starts a fresh chat</div>', unsafe_allow_html=True)

# -------------------- History --------------------
history = [m for m in st.session_state.messages if not isinstance(m, SystemMessage)]

if not history:
    with st.chat_message("assistant", avatar=cfg["avatar"]):
        st.markdown(cfg["welcome"])
    st.markdown("##### 💬 Try asking")
    cols = st.columns(len(cfg["starters"]))
    for i, (col, s) in enumerate(zip(cols, cfg["starters"])):
        if col.button(s, use_container_width=True, key=f"starter_{i}"):
            st.session_state.pending = s
            st.rerun()

for message in history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="🧑"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar=cfg["avatar"]):
            st.markdown(message.content)

# -------------------- Input --------------------
typed = st.chat_input("Type your message here...")
prompt = typed or st.session_state.pop("pending", None)

if prompt:
    if prompt.strip() == "0":
        st.warning("Chat stopped. Click '🔄 Reset Chat' to start a new conversation.")
        st.stop()

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant", avatar=cfg["avatar"]):
        def token_stream():
            for chunk in st.session_state.model.stream(st.session_state.messages):
                yield chunk.content

        try:
            reply = st.write_stream(token_stream())
        except Exception as e:
            reply = None
            st.error(f"Something went wrong: {e}")
            st.info("Make sure your `MISTRAL_API_KEY` is set in the `.env` file.")

    if reply:
        st.session_state.messages.append(AIMessage(content=reply))
    else:
        st.session_state.messages.pop()  # drop the unanswered user message