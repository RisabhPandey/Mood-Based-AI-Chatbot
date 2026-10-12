<div align="center">

# 🙃 Mood-Based AI Chatbot

**One chatbot. Three personalities. A different vibe for every conversation.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Try_the_Chatbot-FF4B4B?style=for-the-badge)](https://mood-based-ai-chatbot-1.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Integration-1C3C3C?style=flat-square)](https://www.langchain.com/)
[![Mistral AI](https://img.shields.io/badge/Powered%20by-Mistral%20AI-7C3AED?style=flat-square)](https://mistral.ai/)

**🔴 Live App:** https://mood-based-ai-chatbot-1.streamlit.app/  
**💻 GitHub Repository:** https://github.com/RisabhPandey/Mood-Based-AI-Chatbot

</div>

---

## 📌 Overview

Mood-Based AI Chatbot is a conversational AI web application built with **Python, Streamlit, LangChain, and Mistral AI**. It lets users choose an assistant personality and chat with an AI that responds according to the selected tone.

Whether you want a dramatic angry response, a humorous reply, or a sad and thoughtful tone, you can switch between three modes through a simple interactive interface.

> **Note:** The selected mood controls the assistant's response style through a system prompt. The application does not detect the user's actual emotional state.

## ✨ Features

| Feature | Description |
|---|---|
| 😡 **Angry Mode** | An aggressive, impatient response style. |
| 😂 **Funny Mode** | Humorous responses and jokes. |
| 😢 **Sad Mode** | A sad, deep response style. |
| 💬 **Interactive chat** | Chat through Streamlit's chat interface. |
| 🧠 **Conversation context** | Earlier messages are included in the current conversation. |
| 🔄 **Reset Chat** | Clear the conversation and start again. |
| 🎭 **Mood-based prompts** | The selected personality determines the system prompt and assistant avatar. |
| ☁️ **Live deployment** | Access the app online through Streamlit Community Cloud. |

## 🖥️ Try the Live Demo

👉 **[Launch Mood-Based AI Chatbot](https://mood-based-ai-chatbot-1.streamlit.app/)**

1. Open the live app.
2. Select **Angry**, **Funny**, or **Sad**.
3. Enter a message in the chat box.
4. Continue the conversation and compare the different response styles.
5. Select **Reset Chat** to clear the current conversation.

Enter `0` to stop the current chat interaction.

## 🛠️ Tech Stack

- **Python** — application logic
- **Streamlit** — web UI and chat interface
- **LangChain Core** — message types and conversation handling
- **LangChain Mistral AI** — integration with the Mistral chat model
- **Mistral AI API** — AI-generated responses
- **python-dotenv** — local environment variable loading
- **Streamlit Community Cloud** — deployment and hosting

## 🏗️ How It Works

```text
User opens the chatbot
        |
        v
Selects a personality
(Angry / Funny / Sad)
        |
        v
App selects the matching system prompt
        |
        v
User enters a message
        |
        v
Conversation messages are sent through LangChain
        |
        v
Mistral AI generates a response
        |
        v
Response appears in the Streamlit chat
```

### Conversation flow

1. The user chooses a personality.
2. The application maps that choice to a corresponding system prompt.
3. Streamlit session state stores the conversation messages.
4. LangChain sends the messages to the configured Mistral chat model.
5. The generated response is displayed and added to the conversation history.
6. Changing the personality starts a new conversation for that mode.

## 📂 Project Structure

```text
Mood-Based-AI-Chatbot/
├── Projects/
│   └── UI_chatbot.py       # Main Streamlit chatbot application
├── requirements.txt        # Python dependencies
├── .env                    # Local API key (create locally; do not commit)
├── .gitignore              # Excludes secrets and generated files
└── README.md               # Project documentation
```

*Adjust the file paths above if your repository structure differs.*

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/RisabhPandey/Mood-Based-AI-Chatbot.git
cd Mood-Based-AI-Chatbot
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If your repository includes `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the packages used by the application:

```bash
python -m pip install streamlit python-dotenv langchain-core langchain-mistralai
```

### 4. Configure your Mistral API key

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

Replace the placeholder with your own API key from the [Mistral AI console](https://console.mistral.ai/).

The application uses `python-dotenv` to load local environment variables. Ensure your code reads the key using the configuration supported by your current implementation.

### 5. Start the app

If the main file is inside `Projects/`:

```bash
streamlit run Projects/UI_chatbot.py
```

If it is in the repository root:

```bash
streamlit run UI_chatbot.py
```

Open the local URL shown in the terminal.

## ☁️ Deployment

This project is deployed using **Streamlit Community Cloud**.

To deploy your own copy:

1. Push the project to a GitHub repository.
2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Create an app and select the repository, branch, and main Python file.
4. Open the app's **Settings → Secrets**.
5. Add your API key in TOML format:

   ```toml
   MISTRAL_API_KEY = "your_actual_api_key_here"
   ```

6. Save the settings and wait for the app to restart.

The application code must read the secret (for example, through `st.secrets["MISTRAL_API_KEY"]`) or otherwise access the configured environment variable. The secret name in the dashboard and the name used in code must match.

## 🔐 Security

- **Never commit API keys** to GitHub.
- Keep `.env` out of version control.
- Use Streamlit Cloud Secrets for deployed applications.
- If a key is exposed, revoke it and create a new one.
- Do not paste API keys into screenshots, issues, or public messages.

Recommended `.gitignore` entries:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
```

## ⚠️ Notes

- AI responses depend on the configured Mistral model, API access, and service availability.
- API usage may be subject to account limits or charges.
- Conversation history is maintained in Streamlit session state; this project does not implement a permanent database for chat history.
- The chatbot changes response tone based on a selected prompt; it is not a mental-health diagnostic tool.

## 🚀 Potential Improvements

Ideas for future versions (not necessarily implemented yet):

- Add more personalities and customizable system prompts.
- Add response streaming.
- Add persistent chat history and conversation export.
- Add more robust API error handling and configuration checks.
- Add unit tests and deployment health checks.
- Improve accessibility and mobile layout.

## 👨‍💻 Author

**Risabh Pandey**

- GitHub: [@RisabhPandey](https://github.com/RisabhPandey)
- Repository: [Mood-Based-AI-Chatbot](https://github.com/RisabhPandey/Mood-Based-AI-Chatbot)
- Live Demo: [Try the chatbot](https://mood-based-ai-chatbot-1.streamlit.app/)

## 📄 License

No license is specified in this README. Add a `LICENSE` file to your repository if you want to define the terms under which others may use, modify, or distribute the project.
