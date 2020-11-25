from utils.mac import brewInstall, npmInstall
from utils.display import printInstallInfo
from utils.display import Printer
from utils.process import runCommandInShell

printer = Printer()

class MacInstaller:
    # 
    # Shell Related
    # 
    def installZsh(self):
        printInstallInfo("ZSH")
        brewInstall("zsh")

    def installIterm2(self):
        printInstallInfo("iTerm2")
        brewInstall("iterm2", cask=True)
        printer.info("» Setting Iterm2 to persist windows on exit")
        runCommandInShell('defaults write "com.googlecode.iterm2" "NSQuitAlwaysKeepsWindows" 1')

    def installOhMyZsh(self):
        printInstallInfo("Oh-My-Zsh")
        runCommandInShell('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    

    # 
    # Browsers
    # 
    def installChrome(self):
        printInstallInfo("Google Chrome")
        brewInstall("google-chrome", cask=True)
    
    def installBraveBrowser(self):
        printInstallInfo("Brave Browser")
        brewInstall("brave-browser", cask=True)

    # 
    # Programmer's Hackbox
    # 
    def installVSCode(self):
        printInstallInfo("Visual Studio Code")
        brewInstall("visual-studio-code", cask=True)

    # 
    # Version Control
    # 
    def installGitKraken(self):
        printInstallInfo("GitKraken")
        brewInstall("gitkraken", cask=True)

    # 
    # Connectivity Tools
    # 
    def installDiscord(self):
        printInstallInfo("Discord")
        brewInstall("discord", cask=True)
    
    def installZoom(self):
        printInstallInfo("Zoom Video Meetings")
        brewInstall("zoomus", cask=True)
    
    def installTelegram(self):
        printInstallInfo("Telegram")
        brewInstall("telegram", cask=True)
    
    
    # 
    # BlockChain Related
    # 
    def installGanache(self):
        printInstallInfo("Ganache")
        brewInstall("ganache", cask=True)

    def installGanacheCLI(self):
        printInstallInfo("Ganache CLI")
        npmInstall("ganache-cli")

    def installTruffleSuite(self):
        printInstallInfo("Truffle Suite")
        npmInstall("truffle")

    def installOtherCryptoPackages(self):
        printInstallInfo("web3 | keccak | truffle-assertions")
        npmInstall("keccak")
        npmInstall("web3")
        npmInstall("truffle-assertions")

