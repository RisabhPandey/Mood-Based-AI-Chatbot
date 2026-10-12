import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load environment variables
load_dotenv()

# Configure the Streamlit page layout
st.set_page_config(page_title="Mood Based AI Chatbot", page_icon="🙃", layout="centered")

# --- UI Header & Layout matching the image ---
st.title("🙃 Mood Based AI Chatbot")
st.caption("Choose AI personality and start chatting | Type 0 to stop")

st.write("") # Small spacer

# Define our modes and corresponding system prompts
modes = {
    "😡 Angry": "You are an angry assistant. You have to answer aggressively & impatiently",
    "😂 Funny": "You are a happy assistant. You have to respond with humor & jokes.",
    "😢 Sad": "You are a sad assistant. You have to answer in a sad & deep tone."
}

# Horizontal radio buttons for mode selection
selected_mode = st.radio(
    "Choose your AI Mode:", 
    list(modes.keys()), 
    horizontal=True
)

st.divider()

# Reset Chat button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.rerun()

# --- Initialize State & Model ---
if "model" not in st.session_state:
    st.session_state.model = ChatMistralAI(model="open-mistral-7b", temperature=0.8)

# Initialize or reset chat if the user changes the mode
system_prompt = modes[selected_mode]
if "messages" not in st.session_state or "current_mode" not in st.session_state or st.session_state.current_mode != selected_mode:
    st.session_state.current_mode = selected_mode
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

# Determine the avatar to show based on selection
if "Sad" in selected_mode:
    bot_avatar = "😢"
elif "Funny" in selected_mode:
    bot_avatar = "😂"
else:
    bot_avatar = "😡"

# --- Main Chat Interface ---
# Display historical messages (skipping the hidden SystemMessage)
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar=bot_avatar):
            st.markdown(message.content)

# --- Handle New User Input ---
if prompt := st.chat_input("Type your message here..."):
    
    # Handle the "0" exit condition gracefully in UI
    if prompt.strip() == "0":
        st.warning("Chat stopped. Click '🔄 Reset Chat' to start a new conversation.")
        st.stop()
        
    # Render user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to LangChain state
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Fetch and render bot response
    with st.chat_message("assistant", avatar=bot_avatar):
        with st.spinner("Typing..."):
            response = st.session_state.model.invoke(st.session_state.messages)
        st.markdown(response.content)
    
    # Add bot message to LangChain state
    st.session_state.messages.append(AIMessage(content=response.content))