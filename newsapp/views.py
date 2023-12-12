import requests
from django.shortcuts import render


def index(request):
    url = 'https://newsapi.org/v2/everything?q=football&from=2023-12-11&sortBy=popularity&apiKey=c3c864ba9bcc4d8e96c3c7171f61f374'
    
    response = requests.get(url)

    if response.status_code == 200:
        news_data = response.json()  # Parse the response as JSON
        articles = news_data.get('articles', [])
        news_list = []

        for article in articles:
            title = article.get('title', '')
            description = article.get('description', '')
            image_url = article.get('urlToImage', '')
            news_list.append({'title': title, 'description': description, 'image_url': image_url})

        return render(request, 'index.html', context={'news_list': news_list})
    else:
        error_message = f"Failed to fetch news. Status Code: {response.status_code}"
        return render(request, 'error.html', context={'error_message': error_message})
