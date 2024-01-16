from bs4 import BeautifulSoup
import requests

website = 'https://test-scraping-three.vercel.app/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_="main-article")

# title = box.find('h1').get_text()
# print(title)

if box:
    title_element = box.find('h1')
    if title_element:
        title = title_element.get_text()
        transcript = box.find('div', class_="test3").get_text(strip=True, separator=' ')
        with open(f'{title}.txt', 'w') as file:
            file.write(transcript)
        print(transcript)
    else:
        print("No 'h1' element found within the specified 'article' element.")
else:
    print("No 'article' element with class 'main-articel' found.")