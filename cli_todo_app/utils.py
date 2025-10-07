import sys
import os

class ConsoleUtils:
    
    @staticmethod
    def clear_console():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    
    @staticmethod
    def exit_app():
        print('-' * 30)
        sys.exit('Goodbye !!')