import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/2024_Indian_general_election'

r = requests.get(url)

print(f"Status Code: {r.status_code}")

if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')
    
    pretty_html = soup.prettify()

    with open('wikipedia_page_pretty.txt', 'w', encoding='utf-8') as file:
        file.write(pretty_html)

    print("The prettified HTML content has been saved to wikipedia_page_pretty.txt")
else:
    print("Failed to retrieve the webpage.")

