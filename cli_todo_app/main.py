from app import App
from handler import Handler
from json_manager import JsonManager

def main() -> None:
    '''
    Main point of the to-do cli application.

    Creates App class instance and calls run method to initialize app navigation.

    Returns:
    --------
    - None, this function does not return anything, it just calls the program flow manager.
    '''
    database = JsonManager()
    app_handler = Handler(database)
    app = App(app_handler)
    app.run()

if __name__ == "__main__":
    main()
