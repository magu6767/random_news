from typing import Any

import requests


def get_article_data(selected_category: str) -> dict[str, Any] | None:
    headers = {"X-Api-Key": "9a6727a7ce2f4abe95ffdd2d9f441dd6"}

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "jp",
        "category": selected_category,
        "pageSize": 10,
    }
    response = requests.get(url, headers=headers, params=params)

    if response.ok:
        response_data = response.json()
        return response_data["articles"]
