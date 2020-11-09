import sys,os
sys.path.append('/Users/abhishekranjan/scripts')
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from colorama import init
init()
from colorama import Fore, Back, Style

from configs.git import GIT_EMAIL,GIT_NAME
from utils.process import runCommandAndGetOutput,runCommandInShell

def setGitNameEmail():
    runCommandInShell("git config --global user.name '{}'".format(GIT_NAME))
    runCommandInShell("git config --global user.email '{}'".format(GIT_EMAIL))

def gitSetup():
    outName = runCommandAndGetOutput("git config --global user.name")
    outEmail = runCommandAndGetOutput("git config --global user.email")
    name = outName.stdout.decode().strip()
    email = outEmail.stdout.decode().strip()
    if(name == "" and email == ""):
        setGitNameEmail()
        return
    print(Fore.GREEN)
    print("» Current Git Configuration is", Fore.CYAN ,"{} <{}>".format(name, email), Style.RESET_ALL)
    if name == GIT_NAME and email == GIT_EMAIL:
        # print(Style.DIM, Fore.YELLOW)
        print(Style.DIM, Fore.YELLOW, "Git Configs are already set as needed !", Style.RESET_ALL)
        return

    print(Fore.GREEN)
    print("» Do you want to replace the current configuration with", Fore.CYAN, "{} <{}>".format(GIT_NAME, GIT_EMAIL), Style.RESET_ALL)
    resp = input("y/n: ")
    resp = resp.lower()
    # print(resp)
    if resp == 'y':
        setGitNameEmail()
        print(Fore.GREEN)
        print("» Git Name & Email Set !", Style.RESET_ALL)

    # print({name, email})


# gitSetup()