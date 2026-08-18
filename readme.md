# AI Code Review Assistant

A desktop application that reviews source code using Google's Gemini AI and provides structured, actionable feedback on bugs, readability, performance, and best practices.

---

## Why I Built This

This is my first project and I built this to learn how to integrate a large language model into a real, working application — not just experiment with an API in isolation. Through building it, I gained hands-on experience with API integration, prompt design, error handling, desktop GUI development with CustomTkinter, and using SQLite to persist data locally. It also taught me how to debug real-world issues, from deprecated libraries to API key format changes, that don't show up in tutorials.

---

## Features

- Paste code directly or upload a code file
- Select the programming language from a dropdown (Python, Java, C++, JavaScript, C#)
- AI-powered code review covering:
  - Bugs
  - Readability
  - Performance
  - Best Practices
- Clear loading indicator while waiting for a response
- Every review automatically saved to a local database
- Graceful error handling for empty input and API failures

---

## Tech Stack

- **Language:** Python
- **GUI:** CustomTkinter
- **AI Model:** Google Gemini API
- **Database:** SQLite
- **File Handling:** Built-in Python (`tkinter.filedialog`)
- **Environment Variables:** python-dotenv

---

## Project Structure

ai-code-review-assistant/
│
├── main.py          # Entry point
├── frontend.py      # GUI and app logic
├── backend.py       # Gemini API integration
├── database.py      # SQLite storage
├── config.py        # Environment variable / API key setup
├── requirements.txt
└── README.md

---

## Installation

Clone the repository:

git clone https://github.com/BhuvaneshHK/AI-Code-Assistant.git
cd AI-Code-Assistant

Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a `.env` file in the project root and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here

You can get a free API key at aistudio.google.com.

---

## Running the App

python main.py

*Currently run via the command line; packaging as a standalone executable is a planned improvement.*

---

## How It Works

1. The user pastes code or uploads a file.
2. The user selects the programming language.
3. The code is sent to Gemini along with a structured prompt asking for feedback on bugs, readability, performance, and best practices.
4. The AI's response is cleaned of Markdown/LaTeX formatting and displayed in the app.
5. The review is automatically saved to a local SQLite database for future reference.

---

## Future Improvements

- Render Markdown formatting properly instead of stripping it
- Add a way to view past reviews from the database within the app
- Package the app as a standalone executable (via PyInstaller)
- Add copy/clear buttons for convenience
- Support reviewing multiple files at once

---

## License

MIT License