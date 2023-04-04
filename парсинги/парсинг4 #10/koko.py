import requests
from bs4 import BeautifulSoup
import time


def test_request(url, retry=5):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"

    }
    try:
        response = requests.get(url=url, headers=headers)
        print(f"[+] {url} {response.status_code}")
    except Exception as ex:
        time.sleep(3)
        if retry:
            print(f"[INFO]retry={retry}=>{url}")
            return test_request(url, retry=(retry - 1))
        else:
            raise
    else:
        return response


def main():
    with open("парсинг4 #10/books_urls.txt",encoding="utf-8") as file:
        books_urls = file.read().splitlines()

    for book_url in books_urls:
        try:
            r = test_request(url=book_url)
            soup = BeautifulSoup(r.text, "lxml")
            print(f"{soup.title.text}\n{'-' * 20}")
        except Exception as ex:
            continue

if __name__ == "__main__":
    main()