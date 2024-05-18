from datetime import datetime
from colorama import Fore

black = Fore.LIGHTBLACK_EX
red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
cyan = Fore.LIGHTCYAN_EX
white = Fore.LIGHTWHITE_EX
reset = Fore.RESET


class logging:
    def time():
        return datetime.now().strftime("%I:%M:%S %p")
    
    def success(mmessage):
        print(f"{black}[ {logging.time()} ] {green}(+){reset} ~/ {mmessage}")
        
    def error(message):
        print(f"{black}[ {logging.time()} ] {reset + red}(!){reset} ~/ {message}")
        
    def info(message):
        print(f"{black}[ {logging.time()} ] {reset + blue}(i){reset} ~/ {message}")