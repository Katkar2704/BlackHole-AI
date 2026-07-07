import asyncio
import json
import re
from app.search.google_executor import perform_search
from app.llm.gemini_client import call_gemini
from app.llm.llm_registry import get_routing_logic

async def analyze_query_batch(query: str):
    prompt = f"Analyze: '{query}'. Return ONLY JSON: {{\"complexity\": 0-100, \"domain\": \"Healthcare/Legal/Finance/Code/General\", \"search_query\": \"...\"}}"
    try:
        raw = await call_gemini(prompt, "You are a JSON logic analyzer.")
        json_str = re.search(r'\{.*\}', raw, re.DOTALL).group()
        return json.loads(json_str)
    except:
        return {"complexity": 75, "domain": "General", "search_query": query}

async def route_and_execute(query, user_selected_llm, history):
    analysis = await analyze_query_batch(query)
    urls, web_context = await perform_search(analysis['search_query'])

    if user_selected_llm == "Auto-Select":
        display_model = get_routing_logic(analysis['domain'], analysis['complexity'])
    else:
        display_model = user_selected_llm

    final_instruction = (
        f"Act as {display_model}. Use the WEB DATA to provide a professional report. "
        f"Complexity: {analysis['complexity']}. Use Markdown tables and '---' lines."
    )

    memory = "\n".join([f"{m['role']}: {m['content']}" for m in history[-3:]])
    final_prompt = f"WEB DATA:\n{web_context}\n\nHISTORY:\n{memory}\n\nUSER: {query}"
    
    response = await call_gemini(final_prompt, final_instruction)

    return {
        "response": response,
        "metadata": {
            "llm": display_model,
            "domain": analysis['domain'],
            "sources": urls
        }
    }