import requests
from typing import List


def fetch_data(urls: List) -> List:
    """fetching data from urls"""

    data = []
    for url in urls:
        res = requests.get(url)
        data.append(res.json())

    return data


if __name__ == "__main__":
    result = ["https://swapi.dev/api/people/1/"]
    output = fetch_data(result)
    print(output)
