
import requests as requests
import csv
import requests
from bs4 import BeautifulSoup
import json


def google_search(query, num_results):
    results = []
    url = f"https://www.google.com/search?q={query}&num={num_results}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', {'class': 'kCrYT'})

    for result in search_results:
        link_element = result.find('a')
        if link_element and 'youtube.com/channel/' in link_element['href']:
            link = link_element['href']
            channel_name = link_element.get_text()
            results.append({'Channel Name': channel_name, 'URL': link})

    return results

search_query = "site:youtube.com openinapp.co"
num_results = 10000

search_results = google_search(search_query, num_results)

with open('youtube_channel_links.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Channel Name', 'URL'])
    writer.writeheader()
    writer.writerows(search_results)

print("Results saved in 'youtube_channel_links.csv' file.")

links = {'YouTube channel links': search_results}

with open('youtube_channel_links.json', 'w') as file:
    json.dump(links, file, indent=4)

print("Results saved in 'youtube_channel_links.json' file.")