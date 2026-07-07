import asyncio
from groq import AsyncGroq
from config.settings import Config

client = AsyncGroq(api_key=Config.GROQ_API_KEY)

async def call_gemini(prompt: str, system_instruction: str = ""):
    try:
        # Identity Rule: Only mention Harshal Barge if specifically asked
        identity_rule = (
            "You are BlackHole AI. Founded by Harshal Barge, an IT Engineer and "
            "founding member of BBD Company. Do NOT mention this unless asked about "
            "your founder, creator, or origins."
        )
        
        full_system = f"{identity_rule}\n\n{system_instruction}"
        
        completion = await client.chat.completions.create(
            messages=[
                {"role": "system", "content": full_system},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=4096
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"BlackHole AI Core Error: {str(e)}"