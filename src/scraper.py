try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    exit()


##Note: Scrapes words from wordfinder.yourdictionary
def build_url(letters: int) -> str:
    page_num = 1
    url = f"https://wordfinder.yourdictionary.com/letter-words/{letters}/?page={page_num}"
    return url

def scrape_words(letters: int) -> str:
    url = build_url(letters)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        words = []

        #pulls the table with words
        table = soup.find('table', class_='table')
        
        #pulls the rows
        rows = table.find_all('tr')

        #pulls the data from the rows
        for row in rows:
            row_data = row.find_all('td')
            indiv_data = [data.text.strip() for data in row_data]
            if len(indiv_data[0]) > 0:
                words.append(indiv_data[0])
        
        return words
    else:
        print(f"Failed to retrieve data from {url}")
        return []