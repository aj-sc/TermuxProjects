import requests
from datetime import date, datetime

BASE_URL = 'https://www.datos.gov.co/resource/ceyp-9c7c.json'

def set_date_limit() -> str:
    date_limit = datetime.now()
    formatted_date_limit = date_limit.strftime('%Y-%m-%dT00:00:00.000')

    return formatted_date_limit

def get_dollar_value(date_limit: str) -> float | str:
    params = {
        'vigenciahasta' : date_limit
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    if not data:
        return 'No data returned from API'
    
    dollar_value = float(data[0].get('valor', ''))

    return dollar_value

def main() -> None:
    date_limit = set_date_limit()
    dollar_value = get_dollar_value(date_limit)

    if isinstance(dollar_value, float):
        print(f'Dollar value on {date.today()} is: ${dollar_value:,.2f}')
    else:
        print(dollar_value)

if __name__ == "__main__":
    main()

    

