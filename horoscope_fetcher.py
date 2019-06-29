import requests
from datetime import date
from bs4 import BeautifulSoup


BASE_URL = 'https://www.bhaskar.com/religion/rashifal/'
URL_CONST = 'daily-horoscope/'


def add_name_in_url(h_name):
    par_url = BASE_URL + h_name + '/'
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


def get_horoscope(soup):
    context = {
        'class': 'rashifal-text-data'
    }
    div = soup.find('div', attrs=context)
    div_children = div.contents
    p = div_children[1]
    p_children = p.contents
    horoscope = p_children[1]
    return horoscope


def get_header(soup, h_name):
    context = {
        'class': 'rashi_heading {}_Big'.format(h_name)
    }
    div = soup.find('div', attrs=context)
    div_children = div.contents
    header = div_children[3]
    return header.text


def get_message(header, horoscope):
    return '*{} ->* {}'.format(header, horoscope)
