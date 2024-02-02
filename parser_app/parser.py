import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

URL = "http://www.manascinema.com/"

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

# start
@csrf_exempt
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


# get data
@csrf_exempt
def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')
    items = bs.find_all('div', class_='short_movie_info')
    manas_lst = []
    for item in items:
        manas_lst.append({
            'title': item.find('div', class_='m_title').get_text(),
            'time': item.find('div', class_='m_time').get_text(),
            'image': URL + item.find('div', class_='m_thumb').find('img').get('src'),
        })
    return manas_lst

#parsing
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        manas_lst_all_films = []
        for page in range(0,1):
            html = get_html(f'http://www.manascinema.com/movies', params=page)
            manas_lst_all_films.extend(get_data(html.text))
            return manas_lst_all_films
    else:
        raise Exception('error in parse')

print(parser())