# 📰 AI Academic Newsletter Generator

An AI-powered Python application that searches for recent news articles
on a given topic and generates a structured, publication-ready academic
research article. The user can then either send the article via email or
save it locally.

------------------------------------------------------------------------

## 🚀 Features

-   🔎 Search recent news by topic and time range\
-   🤖 Generate structured academic articles using Google Gemini\
-   📚 APA 7 formatted citations and references\
-   📧 Send generated article via email\
-   💾 Save article locally as a `.txt` file\
-   🖥️ Simple CLI interaction

------------------------------------------------------------------------

## 🏗️ Project Structure

    .
    ├── main.py
    ├── searchArticles.py
    ├── generateNewsletter.py
    ├── send_email.py
    ├── user_display.py
    ├── .env
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/yourusername/ai-academic-newsletter.git
cd ai-academic-newsletter
```

### 2️⃣ Create virtual environment

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

``` bash
pip install langchain langchain-tavily google-generativeai python-dotenv
```

------------------------------------------------------------------------

## 🔐 Environment Variables

Create a `.env` file in the root directory:

    TAVILY_API_KEY=your_tavily_api_key
    GOOGLE_API_KEY=your_google_api_key
    EMAIL_ADDRESS=your_email
    EMAIL_PASSWORD=your_app_password

⚠️ Do NOT upload your `.env` file to GitHub.

Add this to `.gitignore`:

    .env

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
python main.py
```

Follow the prompts to: 1. Enter research topic 2. Select time range 3.
Choose to send via email or save locally

------------------------------------------------------------------------

## 🧠 How It Works

1.  User inputs research topic\
2.  Tavily API searches recent news articles\
3.  Results are passed to Gemini via LangChain\
4.  Gemini generates a structured academic article\
5.  User selects output method

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python 3.11+
-   LangChain
-   Google Gemini API
-   Tavily Search API
-   SMTP (Email)
-   python-dotenv

------------------------------------------------------------------------

## 📜 License

Educational & portfolio purposes only.
