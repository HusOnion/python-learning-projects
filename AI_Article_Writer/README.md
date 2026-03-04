# AI Research Article Generator

A Python project that generates professional, research-based articles on user-specified topics using search results and a generative AI model. The project demonstrates API usage, email sending, and file handling.

## Features
- Search for articles on a given topic using the TavilySearch API.
- Generate a well-structured, academic-style article using a generative AI model.
- Send generated articles via email to Gmail addresses.
- Save articles locally on your PC.
- Interactive user interface for topic selection, time range, and email input.

## Getting Started

### Prerequisites
- Python 3.10+ installed
- pip (Python package manager)

## Usage

Follow the prompts to:

1. Enter your topic.
2. Select a time range for search results (day, week, month, year).
3. Choose whether to save the article to your PC or send it via email.
4. Enter recipient emails if sending via email.

Generated articles are fully structured with:

- Title
- Abstract
- Introduction
- Literature Review
- Main Analysis / Discussion
- Conclusion
- References (APA 7)

## Dependencies

- `langchain_tavily` (for TavilySearch API)
- `langchain` (for generative AI model)
- `python-dotenv` (for 
