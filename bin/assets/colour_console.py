import time as t
import os

class ColourConsole:
    def __init__(self):
        self.red = "\033[31m"
        self.green = "\033[32m"
        self.yellow = "\033[33m"
        self.blue = "\033[34m"
        self.magenta = "\033[35m"
        self.cyan = "\033[36m"
        self.white = "\033[0m"

    def print_title(self, text, colour = "\033[0m"):
        length = len(text) + 10
        space = " " * 5
        print('┉'*length)
        print(f"{space}{colour}{text}{self.white}")
        print('┉'*length)

    def print_new_line(self, text, colour = "\033[0m", time=0.12):
        for character in text:
            print(f"{colour}{character}{self.white}", end = "", flush=True)
            t.sleep(time)
        t.sleep(time*2)
        print()

    def print_space(self, text, colour = "\033[0m", time=0.15):
        for character in text:
            print(f"{colour}{character}{self.white}", end = "", flush=True)
            t.sleep(time)
        t.sleep(time*2)
        print(end=" ")

    def print(self, text, colour = "\033[0m", time=0.15):
        for character in text:
            print(f"{colour}{character}{self.white}", end = "", flush=True)
            t.sleep(time)
        t.sleep(time*2)

    def get_input(self, prompt):
        response = input(f"{self.white}{prompt}{self.red}")
        print(self.white, end="")
        return response

    def line(self):
        print()
    
    def clear(self):
        os.system('cls')

    def small_pause(self):
        t.sleep(0.6)
