# CLI AI ChatBot

## Overview

This is a simple yet interactive command-line chatbot that uses OpenRouter to access different models and generate responses. The chatbot allows users to chat with AI, view chat history, export conversations, and clear stored messages. It provides a smooth and visually appealing experience using `colorama` and `rich` for styled console output.

## Features

- Chat with any model AI available on openrouter.ai in real-time.
- View saved chat history.
- Export chat history to a text file.
- Clear chat history.
- Interactive CLI with markdown support and a typing animation effect.

## Requirements

- Python 3.x
- `pip` installed

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/EXxZAM/CLI-AI-ChatBot.git
   cd CLI-AI-ChatBot
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenRouter API key:
   ```
   API_KEY=your_openrouter_api_key_here
   ```

## Usage

Run the chatbot using:

```bash
python main.py
```

### **Menu Options**

1. **Chat with AI** – Start a conversation.
2. **View chat history** – Display past chat messages.
3. **Export chat history** – Save conversations to a text file.
4. **Clear chat history** – Delete stored chat logs.
5. **Exit** – Quit the chatbot.

## Dependencies

The chatbot relies on the following Python packages:

- `colorama` – For colored text in CLI.
- `rich` – For enhanced CLI styling and markdown rendering.
- `requests` – For sending API requests.
- `python-dotenv` – To manage environment variables.

Install them using:

```bash
pip install colorama rich requests python-dotenv
```

or using the `requirements.txt` file.

## Notes

- The chatbot interacts with OpenRouter AI, so an active internet connection is required.
- Ensure your `.env` file contains a valid API key before running the program.
- The chatbot stores history in `chat_history.json`.

## Author

Created by **Mahdi Olamaei**. You can contact me on Telegram: **@exxzam**.
