import requests
from bs4 import BeautifulSoup

def fetch_fear_and_greed_index(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    historical_values_section = soup.find('h2', string='Historical Values')

    if not historical_values_section:
        print('Unable to find Historical Values section.')
        return None

    values_div = historical_values_section.find_next('div', class_='block')
    fng_values = values_div.select('div.fng-value')

    index_data = []
    for fng_value in fng_values:
        value_name = fng_value.select_one('div.gray').text.strip()
        status = fng_value.select_one('div.status').text.strip()
        fng_circle = fng_value.select_one('div.fng-circle').text.strip()
        index_data.append({
            'Date': value_name,
            'Status': status,
            'Value': fng_circle
        })

    return index_data

def display_index_data(index_data):
    if not index_data:
        return

    for data in index_data:
        print(f"Date: {data['Date']}")
        print(f"Status: {data['Status']}")
        print(f"Value: {data['Value']}")
        print()

if __name__ == "__main__":
    url = 'https://alternative.me/crypto/fear-and-greed-index/'
    index_data = fetch_fear_and_greed_index(url)
    display_index_data(index_data)
