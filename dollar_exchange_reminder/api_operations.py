import requests
from datetime import datetime, timedelta

BASE_URL = 'https://www.datos.gov.co/resource/ceyp-9c7c.json'

def set_date_limit() -> str:
    ''' 
    Set the date limit for our API request.

    Returns:
    --------
    formatted_date_limit (str): Date formatted in ISO 8601 date-time format.
    '''
    date_limit = datetime.now()
    day_number = date_limit.isoweekday()

    if day_number == 7:
        date_limit += timedelta(days=1)
    elif day_number == 6:
        date_limit += timedelta(days=2)

    formatted_date_limit = date_limit.strftime('%Y-%m-%dT00:00:00.000')

    return formatted_date_limit

def get_dollar_value(date_limit: str) -> float | None:
    ''' 
    Get the current official USD to COP exchange rate.

    Parameters:
    -----------
    - date_limit (str): The date until which the exchange value is valid, usually is the current day.

    Returns:
    --------
    dollar_value (float or none): The value of a single dollar in colombian pesos (COP), or none if the API requests fails or no data is available.
    '''

    params = {
        'vigenciahasta' : date_limit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            return None

        dollar_value = float(data[0].get('valor', ''))
        return dollar_value
    except requests.exceptions.HTTPError as e:
        print(f'HTTP error: {e}')
        return None

    

