import os

class Utils:

    # We don't need to create object with this Utils class to use
    # this clear_screen() method because it's static method...
    # You can import "from utils import Utils" and use "Utils.clear_screen()" in any other files/classes
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')