import subprocess as sp
from colorama import init
init()
from colorama import Fore, Back, Style

from utils.display import Printer

printer = Printer()


def runCommandInShell(cmd):
    # print(Fore.GREEN)
    # print("Exec > ", cmd, Style.RESET_ALL)
    printer.info("Exec > " + cmd)
    # print(Style.RESET_ALL)
    res = sp.run(cmd, shell=True)
    # print(res)
    if res.returncode != 0:
        raise RuntimeError("Command Execution failed")
    return res

def runCommandAndGetOutput(cmd, returnCodes = [0]):
    res = sp.run(cmd, shell=True, capture_output=True)
    # print(res)
    if res.returncode not in returnCodes:
        raise RuntimeError("Command Execution failed")
    # if res.returncode != 0:
        # raise RuntimeError("Command Execution failed")
    return res

# runCommandAndGetOutput("brew list -1")