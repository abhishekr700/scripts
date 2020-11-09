import subprocess as sp
from subprocess import PIPE

import sys
sys.path.append('../')

from utils.process import runCommandInShell
from utils.mac import brewInstall, npmInstall

from install.mac.packages.installer import MacInstaller

from colorama import init
init()
from colorama import Fore, Back, Style


def setupForEtherBlockchain():
    MacInstaller.installGanache()
    MacInstaller.installGanacheCLI()
    MacInstaller.installTruffleSuite()
    MacInstaller.installOtherCryptoPackages()

