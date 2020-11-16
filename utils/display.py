from colorama import init
init()
from colorama import Fore, Back, Style

class Printer:
    def warn(self, str):
        print(Fore.YELLOW, str, Style.RESET_ALL)

    def success(self, str):
        print(Fore.GREEN, str, Style.RESET_ALL)
        # print(Fore.LIGHTGREEN_EX, str, Style.RESET_ALL)

    def fail(self, str):
        print(Fore.RED, str, Style.RESET_ALL)

    def info(self, str):
        print(Fore.LIGHTCYAN_EX, str, Style.RESET_ALL)

    def cyan(self, str):
        print(Fore.CYAN, str, Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX, str, Style.RESET_ALL)
        print(Fore.MAGENTA, str, Style.RESET_ALL)

printer = Printer()

def printInstallInfo(package):
    # print(Fore.GREEN)
    # print("» Installing {}".format(package))
    # print(Style.RESET_ALL)
    printer.info("» Installing {}".format(package))

