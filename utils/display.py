from colorama import init
init()
from colorama import Fore, Back, Style

def printInstallInfo(package):
    print(Fore.GREEN)
    print("» Installing {}".format(package))
    print(Style.RESET_ALL)

class Printer:
    def warn(self, str):
        print(Fore.YELLOW, str, Style.RESET_ALL)

    def success(self, str):
        print(Fore.GREEN, str, Style.RESET_ALL)

    def fail(self, str):
        print(Fore.RED, str, Style.RESET_ALL)