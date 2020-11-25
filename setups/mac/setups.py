import sys,os
sys.path.append('/Users/abhishekranjan/scripts')

import json

from install.mac.packages.installer import MacInstaller
from utils.sshConfigManager import SSHConfigManager
from utils.git import Github
from utils.process import runCommandInShell, runCommandAndGetOutput
from utils.display import Printer

printer = Printer()

from colorama import init
init()
from colorama import Fore, Back, Style

from gitSetup import gitSetup as gs
from setups.config import Config


class MacSetups:
    def setupShell(self):
        print("Shell Setup")
        MacInstaller.installZsh()
        MacInstaller.installOhMyZsh()
        MacInstaller.installIterm2()    
    
    def setupGit(self):
        gs()

    def setupConfig(self):
        config = Config()
        config.setupConfig()


    def setupSSHKey(self):
        config = Config()
        configData = config.readConfig()
        # Personal Access Token
        PAT = configData["github"]["PAT"]
        github = Github(PAT)
        ssh = SSHConfigManager("/Users/abhishekranjan/.ssh/config")
        a = ssh.addSSHKey(configData['git']['email'])
        print(a)
        ssh.addSSHConfig("github.com", {
            "HostName": "github.com",
            "User": "git",
            "IdentityFile": a['filePath']
        })
        addRes = github.addSSHKey(a['publicKey'])
        if addRes:
            printer.success("» SSH Key added successfully")
        else:
            printer.fail("SSH Key Addition Failed")
        printer.info("» Testing SSH Access")
        cmdRes = runCommandAndGetOutput("ssh -T github.com", [1,255])
        # print(cmdRes)
        out = cmdRes.stderr.decode()
        if "successfully" in out:
            printer.success("» SSH Key Test Successful")
        else:
            printer.fail("» SSH Key Test Failed")

