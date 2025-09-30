import smtplib
import os
from datetime import date
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('APP_PASSWORD')

def set_email(dollar_value: float) -> dict:
    '''
    Define the parts of the email.

    Parameters:
    -----------
    - dollar_vallue (float): The value of a single US dollar in colombian pesos.

    Returns:
    --------
    email_data (dict): A dictionary containing all the email details.
    '''

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
    '''
    Send a email using Gmail's SMTP server

    Parameters:
    -----------
    - email_data (dict): A dictionary containing a    ll the email details.

    Returns:
    --------
    A confirmation message that indicates that the email was sent successfully.
    '''

    msg = MIMEText(email_data['body'])
    msg['Subject'] = email_data['subject']
    msg['From'] = email_data['sender']
    msg['To'] = email_data['recipients']

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(email_data['sender'], email_data['password'])
            smtp_server.sendmail(email_data['sender'], email_data['recipients'], msg.as_string())

        print('Message sent!')
    except smtplib.SMTPConnectError:
        print('Error, Unable to connect to SMTP server.')
    except smtplib.SMTPException as e:
        print(f'SMTP error ocurred: {e}')

    

