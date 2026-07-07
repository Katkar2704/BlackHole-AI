import google.generativeai as genai
from config.settings import Config

async def classify_domain(query: str) -> str:
    try:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Return only one word domain (Coding, Medical, Legal, Finance, Science, General): {query}"
        response = await model.generate_content_async(prompt)
        return response.text.strip()
    except:
        return "General"