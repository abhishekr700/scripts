import subprocess as sp
from colorama import init
init()
from colorama import Fore, Back, Style


def runCommandInShell(cmd):
    print(Fore.GREEN)
    print("Exec > ", cmd, Style.RESET_ALL)
    # print(Style.RESET_ALL)
    res = sp.run(cmd, shell=True)
    if res.returncode != 0:
        raise RuntimeError("Command Execution failed")
    return res
    # print(res)

def runCommandAndGetOutput(cmd):
    res = sp.run(cmd, shell=True, capture_output=True)
    # print(res)
    if res.returncode != 0:
        raise RuntimeError("Command Execution failed")
    return res

# runCommandAndGetOutput("brew list -1")