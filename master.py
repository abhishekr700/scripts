import sys,os
sys.path.append('/Users/abhishekranjan/scripts')
sys.path.append('../')

from colorama import init
init()
from colorama import Fore, Back, Style

# import setups

from setups.mac.gitSetup import gitSetup
from setups.mac.ethereumBlockchainSetup import setupForEtherBlockchain
from setups.mac.setups import MacSetups

# print(setups)

from install.mac.packages.installer import MacInstaller


#
#  GENERIC FUNCTIONS
# 
def printSetupMenu():
    # printSetupMenuHeader()
    printMacSetupMenu()

def printPackageInstallerMenu():
    # printInstallMenuHeader()
    printMacPackageInstallerMenu()

def printMacPackageInstallerMenu():
    myDict = MacInstaller.__dict__
    allKeys = list(myDict.keys())
    keys = []
    displayKeys = []
    for i in allKeys:
        if i.find("__") == -1:
            keys.append(i)
            displayKeys.append(i.split("install")[1])
    # print(keys)
    while(1):
        printInstallMenuHeader()
        print("MacOS Package Installer Menu:\n")
        for i in range(len(keys)):
            print("{} - {}".format(i+1,displayKeys[i]))

        choice = input("Selection: ")
        if choice == 'q':
            break
        choice = int(choice)
        func = myDict[keys[choice-1]]
        # print(func)
        func()


def printMacSetupMenu():
    # print(setups.keys())
    # print(setups.values())
    myDict = MacSetups.__dict__
    allKeys = list(myDict.keys())
    keys = []
    displayKeys = []
    for i in allKeys:
        if i.find("__") == -1:
            keys.append(i)
            displayKeys.append(i.split("setup")[1])
    while(1):
        printSetupMenuHeader()
        # keys = list(setups.keys())
        for i in range(len(keys)):
            print("{} - {}".format(i+1,displayKeys[i]))
            # print(i+1, keys[i])
        
        choice = input("Selection:")
        if choice == 'q':
            break
        choice = int(choice)
        func = myDict[keys[choice-1]]
        # print(func)
        func()

# printSetupMenu()

def printMainHeader():
    print(Fore.LIGHTCYAN_EX)
    print(""" 
                  _     _     _     _          _      ______ ___   ___  
    ____         | |   | |   (_)   | |        | |    |____  / _ \ / _ \ 
   / __ \    __ _| |__ | |__  _ ___| |__   ___| | ___ __ / / | | | | | |
  / / _` |  / _` | '_ \| '_ \| / __| '_ \ / _ \ |/ / '__/ /| | | | | | |
 | | (_| | | (_| | |_) | | | | \__ \ | | |  __/   <| | / / | |_| | |_| |
  \ \__,_|  \__,_|_.__/|_| |_|_|___/_| |_|\___|_|\_\_|/_/   \___/ \___/ 
   \____/                                                               
                                                                        
 """)
    print(Style.RESET_ALL)

def printSetupMenuHeader():
    print(Fore.LIGHTCYAN_EX)
    s = """

   _____      _                 __  __                  
  / ____|    | |               |  \/  |                 
 | (___   ___| |_ _   _ _ __   | \  / | ___ _ __  _   _ 
  \___ \ / _ \ __| | | | '_ \  | |\/| |/ _ \ '_ \| | | |
  ____) |  __/ |_| |_| | |_) | | |  | |  __/ | | | |_| |
 |_____/ \___|\__|\__,_| .__/  |_|  |_|\___|_| |_|\__,_|
                       | |                              
                       |_|                              

    """
    print(s, Style.RESET_ALL)

def printInstallMenuHeader():
    s = """

  _____           _        _ _   __  __                  
 |_   _|         | |      | | | |  \/  |                 
   | |  _ __  ___| |_ __ _| | | | \  / | ___ _ __  _   _ 
   | | | '_ \/ __| __/ _` | | | | |\/| |/ _ \ '_ \| | | |
  _| |_| | | \__ \ || (_| | | | | |  | |  __/ | | | |_| |
 |_____|_| |_|___/\__\__,_|_|_| |_|  |_|\___|_| |_|\__,_|
                                                         
                                                         

    """
    print(Fore.LIGHTCYAN_EX)
    print(s, Style.RESET_ALL)

def showMasterMenu():
    while(1):
        printMainHeader()
        print("Master Menu")
        print("1. Setups")
        print("2. Package Install")
        inp = input("Select option:")
        if inp == 'q':
            return
        if(inp == '1'):
            printSetupMenu()
        if(inp == '2'):
            printPackageInstallerMenu()
        
        print()
        print()
        print()

showMasterMenu()
