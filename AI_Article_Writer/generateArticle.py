from langchain.chat_models import init_chat_model

def generate_article(results,queries):

    prompt = f'''
    Act as an academic research writer and subject-matter expert.

    Task:
    write a professional, well-structured, research-based article on the following topic:

    {queries}

    and the search results are:
    {results}

    Requirements:
    1. Use formal academic tone.
    2. Structure the article with:
    - Title
    - Abstract (150–200 words)
    - Introduction
    - Literature Review
    - Main Analysis / Discussion
    - Conclusion
    - References

    3. Support all major claims with in-text citations in APA 7 format.
    4. Include a properly formatted reference list at the end (APA 7)
    7. Ensure logical flow, critical analysis (not just summary), and comparison of viewpoints where relevant.

    Output:
    Produce a polished, publication-ready academic article.
    '''

    model = init_chat_model(
            model="gemini-3-flash-preview", 
            model_provider="google_genai", 
            temperature=0.5
        )

    response = model.invoke(prompt)

    if isinstance(response.content, list):
        return response.content[0]['text']
    return response.content




