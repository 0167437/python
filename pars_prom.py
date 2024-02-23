from bs4 import BeautifulSoup
import requests
import lxml
import time


strn = 1

for i in range(1, 20):
    url = (f'https://prom.ua/ua/Krasota-i-zdorove;{
    i}')
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')


    for link in soup.find_all('div', class_='l-GwW js-productad'):
        try:
          name = link.find('span', class_='_3Trjq htldP '
                                         '_7NHpZ '
                                          'h97_n').text
          naim = link.find('span',
                            class_='_3Trjq aXB7S '
                                    'NSmdF').text
          img = link.find('picture',
                            class_='DucV3 _0-uxM '
                                           'Zd5Aq').find('img').get('src')
          cent = link.find('div',
                           class_='M3v0L Qa-Dw '
                                  '_0-YBE mpcTk '
                                  '_0Jq1n').text
        except:
            print('Товар пропущен')



        time.sleep(2)
        print('\n', 'Name: ', name, "\n", 'Naim: ', naim,
             '\n', 'IMG: ', img, '\n', 'Cent: ', cent)