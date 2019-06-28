import requests 
from datetime import date
from bs4 import BeautifulSoup
  

BASE_URL = 'https://www.bhaskar.com/religion/rashifal/'
URL_CONST = 'daily-horoscope/'
HOROSCOPE_1 = 'aquarius'
HOROSCOPE_2 = 'gemini'
HOROSCOPE_HINDI = {
    'aquarius': 'कुंभ',
    'gemini': 'मिथुन', 
}

def add_name_in_url(horoscope_name):
    par_url = BASE_URL + horoscope_name + '/'
    par_url = par_url + URL_CONST
    return par_url  


def add_date_in_url(par_url):
    date_ = date.today()
    date_str = date_.strftime('%d%m%Y')
    url = par_url + date_str
    return url


def get_response(url):
    response = requests.get(url).text
    return response


def get_horoscope(response):
    soup = BeautifulSoup(response, 'html.parser')
    context = {
        'class': 'rashifal-text-data'
    }
    div = soup.find('div', attrs=context)
    div_children = div.contents
    p = div_children[1]
    p_children = p.contents
    horoscope = p_children[1]
    return horoscope


if __name__ == '__main__':
    par_url = add_name_in_url(HOROSCOPE_1)
    url = add_date_in_url(par_url)
    response = get_response(url)
    horoscope = get_horoscope(response)
    heading = HOROSCOPE_HINDI[HOROSCOPE_1]
    message = '{} - {}'.format(heading, horoscope)
    print(message)
