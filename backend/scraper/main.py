from fastapi import FastAPI, HTTPException
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape/")
async def scrape(url: str):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find("title").text if soup.find("title") else "N/A"
        description = soup.find("meta", attrs={"name": "description"})
        description = description["content"] if description else "N/A"

        keywords = soup.find("meta", attrs={"name": "keywords"})
        keywords = keywords["content"] if keywords else "N/A"

        return {"url": url, "title": title, "description": description, "keywords": keywords}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
