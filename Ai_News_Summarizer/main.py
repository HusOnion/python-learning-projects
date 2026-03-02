import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import user_display
import os

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#here to get the category
category = user_display.category()

url = (
    "https://newsapi.org/v2/top-headlines?"
    f"category={category}&"
    "language=en&"
    "pageSize=8&"
    "sortBy=publishedAt&"
    "apiKey=" + NEWS_API_KEY
)

request = requests.get(url)

content = request.json()
articles = content["articles"]


model = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    api_key=GOOGLE_API_KEY
)

content = user_display.content()

# 1 for the full article 
if content == 1: 
    prompt = f"""
    You're a professional newsletter writer.
    Write the full content of the news articles without summarizing.
    Include the full text (or main content) of each article in a clear, readable format.
    Add a highlighted section at the top for the top news of the day.
    Include a footer paragraph listing all sources for the articles.
    Make it look professional, structured, and ready to send as an email.
    make it without a sender or dear , just plain text that is structured.
    Here are the news articles:
    {articles}
    """
# 2 for the summarized articles
else:
    prompt = f"""
    You're a news summarizer.
    Write a bullet pointed summarized paragraph analyzing those news.
    Add another second paragraph to tell me the top 1 news.
    Add a small paragraph with the sources.
    Make everything look proffisinal, layouted and email like.
    make it without a sender or dear , just plain text that is structured.
    Here are the news articles:
    {articles}
    """

response = model.invoke(prompt)
response_str = response.content


body = "Subject: Today's News Summary\n\n" + response_str + " \n\n Thats it for today"
body = body.encode("utf-8")
emails_list = user_display.get_emails()
send_email(body, emails_list)

print("DONE")
