from api_operations import set_date_limit, get_dollar_value
from mail_operations import set_email, send_email

def main() -> None:
    # Set date limit and pass the value to build API request
    date_limit = set_date_limit()
    dollar_value = get_dollar_value(date_limit)

    # Check type (if float API request was successful), then send email, otherwise print error message
    if isinstance(dollar_value, float):
        email_data = set_email(dollar_value)
        send_email(email_data)
    else:
        print('Error, no se pudo retornar valor del dolar')

if __name__ == "__main__":
    main()

    

