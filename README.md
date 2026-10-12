# 🙃 Mood-Based AI Chatbot

A mood-based conversational AI chatbot built with **Python, Streamlit, LangChain, and Mistral AI**. Choose an AI personality and chat with an assistant that responds in a matching tone.

## ✨ Features

- **Three AI personalities**
  - 😡 **Angry:** Responds aggressively and impatiently.
  - 😂 **Funny:** Responds with humor and jokes.
  - 😢 **Sad:** Responds in a sad and deep tone.
- **Interactive chat interface** built with Streamlit.
- **Conversation context** maintained during the current chat session.
- **Personality-based system prompts** that guide the assistant's response style.
- **Reset Chat** button to clear the conversation and start again.
- **Stop input:** Enter `0` to stop the current chat interaction.

## 🧰 Tech Stack

- **Python** — application logic
- **Streamlit** — web-based user interface
- **LangChain** — message management and model integration
- **Mistral AI** — language model used to generate responses
- **python-dotenv** — loads environment variables from a `.env` file

## 📁 Project Structure

```text
Mood-Based-AI-Chatbot/
├── UI_chatbot.py       # Streamlit application
├── .env                # API key configuration (create locally)
├── .gitignore          # Recommended: exclude secrets and virtual environments
├── requirements.txt    # Python dependencies (create as described below)
└── README.md           # Project documentation
```

## ⚙️ Prerequisites

- Python 3.10 or a compatible Python version supported by the dependencies
- A Mistral AI API key
- Internet access for API requests

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/RisabhPandey/Mood-Based-AI-Chatbot.git
cd Mood-Based-AI-Chatbot
```

### 2. Create and activate a virtual environment

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

Install the packages used by the application:

```bash
pip install streamlit python-dotenv langchain-mistralai langchain-core
```

Optionally, save your installed dependencies to a file:

```bash
pip freeze > requirements.txt
```

### 4. Configure your Mistral AI API key

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

Replace the placeholder with your own API key. Keep this file private and **never commit API keys or other secrets to GitHub**.

The application calls `load_dotenv()` to load values from `.env`. The Mistral LangChain integration uses the configured Mistral credentials to authenticate API requests.

### 5. Run the application

```bash
streamlit run UI_chatbot.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the chatbot.

## 💬 How to Use

1. Launch the application.
2. Select **😡 Angry**, **😂 Funny**, or **😢 Sad**.
3. Type a message in the chat input.
4. Read the response generated in the selected personality.
5. Continue chatting; previous messages in the current session are included as context.
6. Click **🔄 Reset Chat** to clear the conversation.
7. Enter `0` in the chat input to stop the current interaction. Reset the chat to start again.

**Note:** Changing the selected personality initializes a new conversation for that mode.

## 🧠 How It Works

1. **Personality selection:** Streamlit displays three personality options.
2. **System prompt:** The selected option maps to a system prompt describing the assistant's tone.
3. **Session state:** Streamlit session state stores the model and conversation messages.
4. **Message handling:** User messages are added to the conversation as `HumanMessage` objects.
5. **Model invocation:** LangChain sends the conversation to the configured Mistral chat model.
6. **Response display:** The generated answer is displayed in the chat interface and saved as an `AIMessage` for subsequent turns.

The application configures the model as `open-mistral-7b` with a temperature of `0.8`. Model availability may depend on Mistral AI's current service offerings and your account access.

## 🔐 Security Notes

- Store API keys in `.env` or a secure secrets manager.
- Add `.env` and `.venv/` to `.gitignore`.
- If an API key has been committed or exposed, revoke it and create a replacement.
- Do not commit credentials, tokens, or other sensitive information to the repository.

Recommended `.gitignore` entries:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
```

## 🛠️ Troubleshooting

### Missing Mistral API key or authentication error
Check that your `.env` file is in the project root, that the variable is correctly configured, and that your API key is valid.

### `streamlit` command not found
Activate your virtual environment and install Streamlit:

```bash
python -m pip install streamlit
```

### Dependency or import errors
Ensure the virtual environment is active, then install the packages listed in the installation section.

### Model unavailable or API request fails
Check your internet connection, Mistral AI account access, API status, and whether `open-mistral-7b` is available to your account. Update the model name in `UI_chatbot.py` if required by the current Mistral API.

## 🔮 Possible Future Improvements

- Add more personalities and allow users to customize a tone.
- Add streaming responses for a more responsive chat experience.
- Add conversation export and persistent chat history.
- Improve error handling for API and network failures.
- Add tests and configuration validation.
- Deploy the application to a hosting platform.

These are potential improvements and are **not currently implemented**.

## 👨‍💻 Author

**Risabh Pandey**

- GitHub: [@RisabhPandey](https://github.com/RisabhPandey)
- Project: [Mood-Based-AI-Chatbot](https://github.com/RisabhPandey/Mood-Based-AI-Chatbot)

## 📄 License

No license is specified here. Add a `LICENSE` file if you want to define how others may use, modify, and distribute this project.
