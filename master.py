import sys,os
sys.path.append('/Users/abhishekranjan/scripts')
sys.path.append('../')

# import setups

from setups.mac.gitSetup import gitSetup
from setups.mac.ethereumBlockchainSetup import setupForEtherBlockchain
from setups.mac.setups import MacSetups

# print(setups)

from install.mac.packages.installer import MacInstaller

# setups = {
#     "Git Setup": gitSetup,
#     "Smart Contract Dev Setup (Ethereum)": setupForEtherBlockchain
# }

#
#  GENERIC FUNCTIONS
# 
def printSetupMenu():
    printMacSetupMenu()

def printPackageInstallerMenu():
    printMacPackageInstallerMenu()

def printMacPackageInstallerMenu():
    myDict = MacInstaller.__dict__
    allKeys = list(myDict.keys())
    keys = []
    for i in allKeys:
        if i.find("__") == -1:
            keys.append(i)
    # print(keys)
    while(1):
        print("MacOS Package Installer Menu:\n")
        for i in range(len(keys)):
            print(i+1, keys[i])

        choice = input("Selection: ")
        if choice == 'q':
            break
        choice = int(choice)
        func = myDict[keys[choice-1]]
        # print(func)
        func()


# printMacPackageInstallerMenu()



def printMacSetupMenu():
    # print(setups.keys())
    # print(setups.values())
    myDict = MacSetups.__dict__
    allKeys = list(myDict.keys())
    keys = []
    for i in allKeys:
        if i.find("__") == -1:
            keys.append(i)
    while(1):
        # keys = list(setups.keys())
        for i in range(len(keys)):
            print(i+1, keys[i])
        
        choice = input("Selection:")
        if choice == 'q':
            break
        choice = int(choice)
        func = myDict[keys[choice-1]]
        # print(func)
        func()

# printSetupMenu()

def showMasterMenu():
    while(1):
        print("Master Menu")
        print("1. Setups")
        print("2. Mac Package Installer")
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
