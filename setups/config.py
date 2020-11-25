# class Config:
#     def setupConfig(self):
#         pass
import json
from pathlib import Path
from colorama import init
init()
from colorama import Fore, Back, Style

class Config:
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

    def readConfig(self):
        f = open("config.json", 'r')
        configJson = f.readlines()[0]
        # print(configJson)
        configDict = json.loads(configJson)
        # print(configDict)
        return configDict

    def checkConfigExists(self):
        configExists = Path("config.json").exists()
        return configExists

