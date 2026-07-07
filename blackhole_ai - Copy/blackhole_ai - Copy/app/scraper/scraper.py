import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetch_content(session, url):
    # Professional Headers to bypass bot detection
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/"
    }
    try:
        async with session.get(url, headers=headers, timeout=15) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                
                # Remove unwanted tags
                for s in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']): 
                    s.decompose()
                
                # Extract clean text
                text = soup.get_text(separator=' ')
                clean_text = " ".join(text.split())
                return clean_text[:2500] # Limit per page for context window
            return ""
    except Exception as e:
        print(f"Scraping error for {url}: {e}")
        return ""

async def scrape_urls(urls):
    if not urls:
        return "No live web data found."
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_content(session, url) for url in urls]
        contents = await asyncio.gather(*tasks)
        
        # Filter out empty results
        valid_contents = [c for c in contents if len(c) > 100]
        
        if not valid_contents:
            return "No live web data found."
            
        return "\n---\n".join(valid_contents)