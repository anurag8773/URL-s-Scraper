from celery import shared_task
import requests
from bs4 import BeautifulSoup
from django.contrib.auth import get_user_model
from api.models import Metadata

User = get_user_model()

@shared_task
def scrape_url_task(user_id, url):
    """Scrapes a URL and stores metadata asynchronously using Celery + Redis."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.title.string if soup.title else "No Title"
        description = (
            soup.find("meta", attrs={"name": "description"}) or {}
        ).get("content", "No Description")
        keywords = (
            soup.find("meta", attrs={"name": "keywords"}) or {}
        ).get("content", "No Keywords")

        user = User.objects.get(id=user_id)
        Metadata.objects.create(user=user, url=url, title=title, description=description, keywords=keywords)
        
        return {"status": "success", "url": url}

    except Exception as e:
        return {"status": "error", "url": url, "message": str(e)}
