from celery import shared_task
import requests
from ray.easy.models import News

@shared_task
def fetch_and_save_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "ru",
        "apiKey": "e5117856dc12485687b2071f109a5cff"
    }

    response = requests.get(url, params=params)
    data = response.json()
    for article in data['articles']:
        News.objects.get_or_create(
            author=article['author'],
            title=article['title'],
            source=article['source']['name']
        )

