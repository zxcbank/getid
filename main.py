import requests
from bs4 import BeautifulSoup
import lxml

link = 'https://2ip.ru/'
response = requests.get(link).text
coup = BeautifulSoup(response, 'lxml')
block = coup.find('div', id = 'd_clip_button')

check_id = block.find('span').text

if __name__ == '__main__':
    print(check_id)

