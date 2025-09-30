from navigation import navigation

def main() -> None:
    '''
    Main point of the to-do cli application.

    Calls navigation loop, which displays main menu and handles user input until the application is exited.

    Returns:
    --------
    - None, this function does not return anything, it just calls the program flow manager.
    '''
    navigation()

if __name__ == "__main__":
    main()
