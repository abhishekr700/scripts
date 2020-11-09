from utils.mac import brewInstall, npmInstall
from utils.display import printInstallInfo
from utils.process import runCommandInShell

class MacInstaller:
    # 
    # Shell Related
    # 
    def installZsh():
        printInstallInfo("ZSH")
        brewInstall("zsh")

    def installIterm2():
        printInstallInfo("iTerm2")
        brewInstall("iterm2", cask=True)

    def installOhMyZsh():
        printInstallInfo("Oh-My-Zsh")
        runCommandInShell('sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    

    # 
    # Browsers
    # 
    def installChrome():
        printInstallInfo("Google Chrome")
        brewInstall("google-chrome", cask=True)
    
    def installBraveBrowser():
        printInstallInfo("Brave Browser")
        brewInstall("brave-browser", cask=True)

    # 
    # Programmer's Hackbox
    # 
    def installVSCode():
        printInstallInfo("Visual Studio Code")
        brewInstall("visual-studio-code", cask=True)

    # 
    # Version Control
    # 
    def installGitKraken():
        printInstallInfo("GitKraken")
        brewInstall("gitkraken", cask=True)

    # 
    # Connectivity Tools
    # 
    def installDiscord():
        printInstallInfo("Discord")
        brewInstall("discord", cask=True)
    
    def installZoom():
        printInstallInfo("Zoom Video Meetings")
        brewInstall("zoomus", cask=True)
    
    def installTelegram():
        printInstallInfo("Telegram")
        brewInstall("telegram", cask=True)
    
    
    # 
    # BlockChain Related
    # 
    def installGanache():
        printInstallInfo("Ganache")
        brewInstall("ganache", cask=True)

    def installGanacheCLI():
        printInstallInfo("Ganache CLI")
        npmInstall("ganache-cli")

    def installTruffleSuite():
        printInstallInfo("Truffle Suite")
        npmInstall("truffle")

    def installOtherCryptoPackages():
        printInstallInfo("web3 | keccak | truffle-assertions")
        npmInstall("keccak")
        npmInstall("web3")
        npmInstall("truffle-assertions")

