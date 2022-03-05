import colorama
from colorama import Fore as f
colorama.init(autoreset=True)

class IO:
    # dictionary of available colours
    colors = {"black": f.BLACK, "red": f.RED, "green": f.GREEN, "yellow": f.YELLOW, "blue": f.BLUE, "magenta": f.MAGENTA, "cyan": f.CYAN, "white": f.WHITE}
    def __init__(self, program_name):
        self.program_name = program_name

    def get_text(self, text):
        # gets standard text format
        return f"({self.program_name}) >> " + text

    def output(self, text, color="white"):
        # look colour up in dictionary
        color = IO.colors[color]
        print(self.get_text(color + text))

    def input(self, prompt="", color="white"):
        # look colour up in dictionary`1`
        color = IO.colors[color]
        return input(self.get_text(color + prompt))
