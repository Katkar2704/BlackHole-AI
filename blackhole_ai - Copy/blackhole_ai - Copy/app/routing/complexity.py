import google.generativeai as genai
from config.settings import Config

async def calculate_complexity(query: str) -> int:
    try:
        genai.configure(api_key=Config.GEMINI_API_KEY)
        # Force a generic stable model name
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Return only a number (0-100) for query complexity: {query}"
        response = await model.generate_content_async(prompt)
        score = "".join(filter(str.isdigit, response.text))
        return int(score) if score else 50
    except:
        return 50