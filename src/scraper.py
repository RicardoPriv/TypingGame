try:
    import requests
    import random
    from bs4 import BeautifulSoup
except ImportError:
    exit()


##Note: Scrapes words from wordfinder.yourdictionary
def build_url(letters: int) -> str:
    dict_pages = {
        3: 12,
        4: 46,
        5: 101,
        6: 176,
        7: 262,
        8: 322,
        9: 298,
        10: 253,
        11: 195,
        12: 143,
        13: 99,
        14: 64,
        15: 40
    }
    
    return f"https://wordfinder.yourdictionary.com/letter-words/{letters}/?page={random.randint(1, dict_pages[letters])}"

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