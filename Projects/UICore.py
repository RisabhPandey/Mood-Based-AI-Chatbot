from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Page Config
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="centered"
)

# Text area internal padding for better readability
st.markdown(
    """<style>
    textarea[aria-label="Enter the movie paragraph:"] {
        padding: 16px !important;
    }
    </style>""", 
    unsafe_allow_html=True
)

# Flexbox for vertical alignment of the icon and heading text
st.markdown(
    "<h1 style='display: flex; align-items: center; gap: 10px;'>🎬 Movie Information Extractor</h1>", 
    unsafe_allow_html=True
)

# Standardized bottom margin to maintain vertical rhythm
st.markdown(
    "<p style='margin-bottom: 24px;'>Extract structured information from a movie paragraph</p>", 
    unsafe_allow_html=True
)

# Model
model = ChatMistralAI(model="open-mistral-7b")

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it in a clean format.

Rules:
- Do NOT add explanations
- Do NOT add extra commentary
- Follow the exact format
- If information is missing → write NULL
- Keep summary short (2-3 lines max)
- Do NOT guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:
Language:

Short Summary: [Write the 2-3 line summary here on the same line]
"""),
    ("human", """Extract information from this paragraph:

{paragraph}
""")
])

# Input
para = st.text_area(
    "Enter the movie paragraph:",
    height=200,
    placeholder="Paste your movie description or review here..."
)

# Centered button layout with neutral default color
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    extract_clicked = st.button("Extract Information", use_container_width=True)

if extract_clicked:
    if para.strip() == "":
        st.warning("Please enter a movie paragraph.")
    else:
        with st.spinner("Extracting information..."):
            final_prompt = prompt.invoke({"paragraph": para})
            response = model.invoke(final_prompt)

            # Left-aligned h2 for consistent visual axis
            st.markdown(
                "<h2 style='text-align: left; margin-bottom: 25px;'>Extracted Information</h2>",
                unsafe_allow_html=True
            )

            # Robust Parsing Logic: 
            # Accumulate keys and values so they always render on the same line, 
            # even if the LLM output spills onto a new line.
            lines = response.content.strip().split("\n")
            extracted_data = {}
            current_key = None

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # If a new key is found
                if ":" in line:
                    key, value = line.split(":", 1)
                    key = key.replace("**", "").strip()
                    value = value.replace("**", "").strip()
                    current_key = key
                    extracted_data[current_key] = value
                # If it's continuation text for the previous key
                elif current_key:
                    clean_line = line.replace("**", "").strip()
                    if extracted_data[current_key]:
                        extracted_data[current_key] += " " + clean_line
                    else:
                        extracted_data[current_key] = clean_line

            # Render the accumulated data into uniform, single-line boxes
            for key, value in extracted_data.items():
                st.markdown(
                    f"""
                    <div style="
                        background-color: #1e1e1e;
                        padding: 12px 16px;
                        border-radius: 8px;
                        margin-bottom: 10px;
                        border-left: 4px solid #4CAF50;
                    ">
                        <strong style="color: #4CAF50;">{key}:</strong>
                        <span style="color: #e0e0e0; margin-left: 8px;">{value}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )