import requests

def get_anime(name):

    url = "https://api.jikan.moe/v4/anime"

    r = requests.get(url, params={"q": name})
    data = r.json()

    if not data["data"]:
        return None

    anime = data["data"][0]

    return {
        "title": anime["title"],
        "image": anime["images"]["jpg"]["large_image_url"],
        "score": anime["score"],
        "year": anime["year"],
        "duration": anime["duration"]
    }
