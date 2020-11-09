#!/bin/bash

echo -e "Installing Ganache"
brew cask install ganache

echo -e "Installing Ganache CLI"
npm install -g ganache-cli

echo -e "Installing Truffle Suite"
npm install -g truffle

echo -e "Install VS Code Solidity Extension"
code --install-extension juanblanco.solidity


