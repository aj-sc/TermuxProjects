import requests
import smtplib
import os
from dotenv import load_dotenv
from datetime import date, datetime
from email.mime.text import MIMEText

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('APP_PASSWORD')

BASE_URL = 'https://www.datos.gov.co/resource/ceyp-9c7c.json'

def set_date_limit() -> str:
    date_limit = datetime.now()
    formatted_date_limit = date_limit.strftime('%Y-%m-%dT00:00:00.000')

    return formatted_date_limit

def get_dollar_value(date_limit: str) -> float | None:
    params = {
        'vigenciahasta' : date_limit
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    if not data:
        return None
    
    dollar_value = float(data[0].get('valor', ''))

    return dollar_value

def set_email(dollar_value: float) -> dict:
    today_date = date.today()

    email_data = {
        'subject' :  f'Recordatorio: Valor TRM {today_date}',
        'body' : f'Buenos dias, el valor de la TRM para el dia {today_date} es de ${dollar_value:,.2f} pesos.',
        'sender' : EMAIL,
        'recipients' : EMAIL,
        'password' : PASSWORD
        }

    return email_data

def send_email(email_data: dict) -> str:
    msg = MIMEText(email_data['body'])
    msg['Subject'] = email_data['subject']
    msg['From'] = email_data['sender']
    msg['To'] = email_data['recipients']

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(email_data['sender'], email_data['password'])
        smtp_server.sendmail(email_data['sender'], email_data['recipients'], msg.as_string())

    print('Message sent!')

def main() -> None:
    date_limit = set_date_limit()
    dollar_value = get_dollar_value(date_limit)

    if isinstance(dollar_value, float):
        email_data = set_email(dollar_value)
        send_email(email_data)
    else:
        print('Error, no se pudo retornar valor del dolar')

if __name__ == "__main__":
    main()

    

