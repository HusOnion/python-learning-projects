# News Fetcher Project

A Python project that fetches top news headlines based on user-selected categories using the News API and Google API. The project demonstrates API usage, environment variable management, and sending email updates.

---

## Features

* Fetch top headlines from News API based on category.
* Use Google API for additional features (e.g., search, analytics).
* Send news summaries via email.
* User-friendly interface for selecting categories.

---

## Getting Started

### Prerequisites

* Python 3.10+ installed
* pip (Python package manager)

### Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Setup environment variables:

   * Copy the example `.env.example` file:

     ```bash
     cp .env.example .env   # Linux/Mac
     copy .env.example .env # Windows
     ```
   * Fill in your API keys in the `.env` file:

     ```env
     GOOGLE_API_KEY=your_gemini_api_key_here
     NEWS_API_KEY=your_news_api_key_here
     GMAIL_APP_PASSWORD=your_gmail_app_password_here
     ```

---

## Usage

Run the main script:

```bash
python main.py
```

Follow the prompts to select a news category and receive top headlines. Emails will be sent if configured.

---


## Dependencies

* `requests`
* `python-dotenv`
* `langchain` (for chat model interaction)
* `send_email` (custom module)
* Any other dependencies listed in `requirements.txt`

---

