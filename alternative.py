from bs4 import BeautifulSoup
import requests
html = requests.get('https://alternative.me/crypto/fear-and-greed-index/').text
soup = BeautifulSoup(html, "html.parser")

historical_values = soup.find('h2', text='Historical Values')
if historical_values:
    values_div = historical_values.find_next('div', class_='block')
    fng_values = values_div.find_all('div', class_='fng-value')
    for fng_value in fng_values:
        value_name = fng_value.find('div', class_='gray').text.strip()
        status = fng_value.find('div', class_='status').text.strip()
        fng_circle = fng_value.find('div', class_='fng-circle').text.strip()
        print(value_name + ':', status)
        print('Value:', fng_circle)
        print()
else:
    print('Unable to find Historical Values.')
