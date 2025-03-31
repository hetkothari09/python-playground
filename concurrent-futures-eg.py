import concurrent.futures
import time
import requests

def download_url(url):
    response = requests.get(url)
    return f"{url} - {len(response.content)}"

start_time = time.time()

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com",
]

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(download_url, url) for url in urls]
    for future in concurrent.futures.as_completed(futures):
        print(future.result())

end_time = time.time()

print(f"Downloaded in {end_time-start_time:.2f} seconds")