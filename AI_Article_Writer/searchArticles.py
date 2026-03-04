from langchain_tavily import TavilySearch
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()


def search_for_articles(queries,time_range):
    tavily_search = TavilySearch(
        max_results=5,
        topic="news",
        search_depth="advanced",
        time_range=f"{time_range}",
        include_raw_content=False,
        include_answer=False
    )
    results = []

    for query in queries:
        result = tavily_search.invoke(query)
        results.append(result)
    
    return results

