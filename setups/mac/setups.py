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


class MacSetups:
    def setupShell():
        print("Shell Setup")
        MacInstaller.installZsh()
        MacInstaller.installOhMyZsh()
        MacInstaller.installIterm2()    
    
    def setupGit():
        gs()

    def setupConfig(self):
        print(Fore.LIGHTCYAN_EX)
        githubPAT = input("Enter Github PersonalAccessToken(PAT):")
        gitEmail = input("Enter Email to use with Git:")
        gitName = input("Enter Name to use with Git:")
        configDict = {
            "git": {
                "name": gitName,
                "email": gitEmail
            },
            "github": {
                "PAT": githubPAT
            }
        }
        configStr = json.dumps(configDict)

        print(configStr)
        f = open("config.json", 'w')
        f.write(configStr)

    def setupReadConfig(self):
        f = open("config.json", 'r')
        configJson = f.readlines()[0]
        # print(configJson)
        configDict = json.loads(configJson)
        # print(configDict)
        return configDict

    def setupSSHKey(self):
        config = self.setupReadConfig()
        # Personal Access Token
        PAT = config["github"]["PAT"]
        github = Github(PAT)
        ssh = SSHConfigManager("/Users/abhishekranjan/.ssh/config")
        a = ssh.addSSHKey(config['git']['email'])
        print(a)
        ssh.addSSHConfig("github.com", {
            "HostName": "github.com",
            "User": "git",
            "IdentityFile": a['filePath']
        })
        addRes = github.addSSHKey(a['publicKey'])
        if addRes:
            print(Fore.GREEN,"» SSH Key added successfully")
        else:
            print(Fore.RED,"SSH Key Addition Failed", Style.RESET_ALL)
        print("Testing SSH Access")
        cmdRes = runCommandAndGetOutput("ssh -T github.com", [1,255])
        # print(cmdRes)
        out = cmdRes.stderr.decode()
        if "successfully" in out:
            printer.success("» SSH Key Test Successful")
        else:
            printer.fail("» SSH Key Test Failed")

