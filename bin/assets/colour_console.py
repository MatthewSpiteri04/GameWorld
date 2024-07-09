import time as t
import os
import colorama
from colorama import Fore, Style

class ColourConsole:
    def __init__(self):
        self.red = Fore.RED
        self.green = Fore.GREEN
        self.yellow = Fore.YELLOW
        self.blue = Fore.BLUE
        self.magenta = Fore.MAGENTA
        self.cyan = Fore.CYAN
        self.white = Fore.WHITE
        self.reset = Style.RESET_ALL

    def print_title(self, text, colour = Style.RESET_ALL):
        length = len(text) + 10
        space = " " * 5
        print('┉'*length)
        print(f"{space}{colour}{text}{self.reset}")
        print('┉'*length)

    def print_new_line(self, text, colour = Style.RESET_ALL, time=0.12):
        for character in text:
            print(f"{colour}{character}{self.reset}", end = "", flush=True)
            t.sleep(time)
        t.sleep(time*2)
        print()

    def print_space(self, text, colour = Style.RESET_ALL, time=0.12):
        for character in text:
            print(f"{colour}{character}{self.reset}", end = "", flush=True)
            t.sleep(time)
        t.sleep(time*2)
        print(end=" ")

    def print(self, text, colour = Style.RESET_ALL, time=0.12):
        for character in text:
            print(f"{colour}{character}{self.reset}", end = "", flush=True)
            t.sleep(time)
        t.sleep(time*2)

    def get_input(self, prompt):
        response = input(f"{self.white}{prompt}{self.yellow}")
        print(self.reset, end="")
        return response
    
    def server_says(self, msg):
        print(f"{self.yellow}[Server]: {Style.RESET_ALL}", end="")
        print(msg)
        print()

    def error_message(self, msg):
        self.line()
        self.print_new_line(msg, self.red, 0.05)
        self.line()
        
    def line(self):
        print()
    
    def clear(self):
        os.system('cls')

    def small_pause(self):
        t.sleep(0.6)
