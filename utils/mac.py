from utils.process import runCommandAndGetOutput, runCommandInShell
from colorama import init
init()
from colorama import Fore, Back, Style

def brewInstall(formula, cask = False):
    if cask == False:
        out = runCommandAndGetOutput("brew list --formula -1")
    else:
        out = runCommandAndGetOutput("brew list --cask -1")
    
    packages = out.stdout.decode().split("\n")
    if formula in packages:
        print(Style.DIM, Fore.YELLOW, end="")
        print("Brew Package : {} is already installed".format(formula) + Style.RESET_ALL)
    else:
        cmd = ""
        if cask == True:
            cmd = "brew cask install {}".format(formula)
        else:
            cmd = "brew install {}".format(formula)
        print("Installing Package")
        runCommandInShell(cmd)

def npmInstall(package):
    out = runCommandAndGetOutput("ls `npm root -g`")
    packages = out.stdout.decode().split("\n")
    if package in packages:
        print(Style.DIM, Fore.YELLOW, end="")
        print("NPM Package : {} is already installed".format(package) + Style.RESET_ALL)
    else:
        cmd = "npm install --global {}".format(package)
        runCommandInShell(cmd)
    # print(out)