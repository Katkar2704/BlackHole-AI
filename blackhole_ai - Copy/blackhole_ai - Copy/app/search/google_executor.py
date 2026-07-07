import aiohttp
from config.settings import Config

async def perform_search(query: str):
    if not Config.TAVILY_API_KEY:
        return [], ""
        
    try:
        url = "https://api.tavily.com/search"
        payload = {
            "api_key": Config.TAVILY_API_KEY,
            "query": query,
            "search_depth": "advanced",
            "max_results": 5
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    results = data.get('results', [])
                    urls = [r['url'] for r in results]
                    # We create a context summary from the snippets Tavily found
                    context = "\n".join([f"Source [{r['url']}]: {r['content']}" for r in results])
                    return urls, context
                return [], ""
    except Exception as e:
        print(f"Tavily Error: {e}")
        return [], ""