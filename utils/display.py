from colorama import init
init()
from colorama import Fore, Back, Style

def printInstallInfo(package):
    print(Fore.GREEN)
    print("» Installing {}".format(package))
    print(Style.RESET_ALL)
