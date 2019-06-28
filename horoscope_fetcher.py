import requests 
from datetime import date
from bs4 import BeautifulSoup
  

BASE_URL = 'https://www.bhaskar.com/religion/rashifal/'
URL_CONST = 'daily-horoscope/'
HOROSCOPE_1 = 'aquarius'
HOROSCOPE_2 = 'gemini'


def add_name_in_url(horoscope_name):
    par_url = BASE_URL + horoscope_name + '/'
    par_url = par_url + URL_CONST
    return par_url  


def add_date_in_url(par_url):
    date_ = date.today()
    date_str = date_.strftime('%d%m%Y')
    url = par_url + date_str
    return url


def get_soup(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    return soup


def get_horoscope(response):
    context = {
        'class': 'rashifal-text-data'
    }
    div = soup.find('div', attrs=context)
    div_children = div.contents
    p = div_children[1]
    p_children = p.contents
    horoscope = p_children[1]
    return horoscope


def get_header(soup):
    context = {
        'class': 'rashi_heading aquarius_Big'
    }
    div = soup.find('div', attrs=context)
    div_children = div.contents
    header = div_children[3]
    return header.text


def get_message(header, horoscope):
    return '{} \n {}'.format(header, horoscope)


if __name__ == '__main__':
    par_url = add_name_in_url(HOROSCOPE_1)
    url = add_date_in_url(par_url)
    soup = get_soup(url)
    horoscope = get_horoscope(soup)
    header = get_header(soup)
    message = get_message(header, horoscope)
    print(message)
