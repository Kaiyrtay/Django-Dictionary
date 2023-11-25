from django.shortcuts import render
import requests
# Create your views here.


def homeView(request):
    return render(request, 'dictionary/index.html')


def searchView(request):
    is_found = False
    # word is found
    word = None
    phonetic = None
    origin = None
    meanings = []
    license_url = None
    source_url = None
    # word is not found
    title = None
    message = None
    # result
    result = {}

    word = request.GET['search']
    response = requests.get(
        f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
    response = response.json()
    try:
        word = response[0]["word"]
        if "phonetics" in response[0]:
            phonetics = response[0]["phonetics"]
            for item in phonetics:
                if "text" in item:
                    phonetic = item["text"]
                    break
        else:
            phonetic = response[0]["phonetic"]

        if "origin" in response[0]:
            origin = response[0]["origin"]

        meanings = response[0]["meanings"]
        license_url = response[0]["license"]["url"]
        source_url = str(response[0]["sourceUrls"][0])

        results = {
            "is_found": True,
            "word": word,
            "phonetic": phonetic,
            "origin": origin,
            "meanings": meanings,
            "license_url": license_url,
            "source_url": source_url,
        }
    except:
        results = {
            "is_found": False,
            "word": request.GET['search'],
            "title": response["title"],
            "message": response["message"],
        }
    return render(request, 'dictionary/search.html', results)
