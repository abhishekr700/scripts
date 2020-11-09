#!/bin/zsh

echo "Welcome to script"


#echo -e "Getting Homebrew - The GodFather - The Servant - He Shall Serve You Well M A S T E R \n"
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

echo -e "===> Checking homebrew install"
BREW_STAT=$(brew doctor)
echo Out:$BREW_STAT

echo -e "===> Installing ZSH Shell"
brew install zsh

echo -e "===> Installing ZSH Completions - Here, Have a Beer "
brew install zsh-completions

echo "==> Installing iTerm2"
brew cask install iterm2

echo -e "===> Installing Oh-My-Zsh"
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo -e "===> Installing Visual Studio Code"
brew cask install visual-studio-code

echo -e "===> Installing Google Chrome"
brew cask install google-chrome

echo -e "===> Installing Brave Browser"
brew cask install brave-browser

echo -e "===> Installing Node JS v12"
brew install node
#brew postinstall node

echo -e "===> Installing Zoom for video meetings"
brew cask install zoomus

echo -e "===> Installing VSCodium - VSCode w/o MS Telemetry :)"
brew cask install vscodium

echo -e "===> Installing Discord"
brew cask install discord

echo -e "===> Installing VLC - Because why the fuck not ?"
brew cask install vlc

echo -e "===> Installing Telegram - Security Pro Max"
brew cask install telegram

echo -e "===> Installing GitKraken - Git CLI ij sloooow !"
brew cask install gitkraken

echo -e "===> Installing MySQL Workbench"
brew cask install mysqlworkbench


