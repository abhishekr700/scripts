import sys,os
sys.path.append('/Users/abhishekranjan/scripts')

from install.mac.packages.installer import MacInstaller

from gitSetup import gitSetup as gs

class MacSetups:
    def setupShell():
        print("Shell Setup")
        MacInstaller.installZsh()
        MacInstaller.installOhMyZsh()
        MacInstaller.installIterm2()    
    
    def setupGit():
        gs()
