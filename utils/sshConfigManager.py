import pprint
import pathlib
from pathlib import Path
from time import gmtime, strftime
import time
from utils.process import runCommandInShell
# print(time.localtime())
# print(strftime("%d-%m-%Y-%H:%M:%S"))

pp = pprint.PrettyPrinter(indent=4)



class SSHConfigManager:
    configFile = ""
    configDict = {}

    def __init__(self, fileName):
        self.configFile = fileName
        self.parseConfig()
        self.checkConfigExists()
        pass

    def checkConfigExists(self):
        configPath = Path(self.configFile)
        # print( "",configPath.exists())
        # print(configPath.resolve().parent)
        # print(configPath.parents[0])
        pass

    def parseConfig(self):
        self.configDict = {}
        f = open(self.configFile, 'r')
        readingConfig = False
        configName = ""
        for line in f:
            lineOrig = line
            line = line.strip()
            if len(line) == 0:
                # print("Empty:", line)
                continue
            if line[0] == '#':
                # print("Comment:", line)
                continue
            
            lineSplit = line.split(" ")
            attr = lineSplit[0]
            value = lineSplit[1]

            # If we've reached the next config
            if readingConfig and attr == "Host":
                readingConfig = True
                self.configDict[value] = {}
                configName = value
                continue

            # If we're reading a particular config
            if readingConfig and attr != "Host":
                self.configDict[configName][attr] = value
                continue

            if lineSplit[0] != "Host":
                raise RuntimeError("Expected Host to be encountered")
            
            if lineSplit[0] == "Host":
                readingConfig = True
                self.configDict[lineSplit[1]] = {}
                configName = lineSplit[1]
                
        # pp.pprint(configDict)
        return self.configDict

    def writeConfig(self):
        finalConfig = ""
        for key in self.configDict.keys():
            singleConfig = "Host {}\n".format(key)
            # print(key, configDict[key])
            for intKey in self.configDict[key].keys():
                singleConfig += "    {} {}\n".format(intKey, self.configDict[key][intKey])
            # print(singleConfig)
            finalConfig += singleConfig
        # print(finalConfig)
        configPath = Path(self.configFile)
        configFileTempPath = Path.joinpath(configPath.resolve().parent, "config-backup-{}".format(strftime("%d-%m-%Y-%H-%M-%S")))
        # configFileTempPath = Path(configPath.resolve().paren).joinpath

        Path(self.configFile).rename(configFileTempPath)
        f = open(self.configFile, 'w')
        f.write(finalConfig)
    
    def addSSHKey(self, email):
        sshFolder = Path.home().joinpath(".ssh")
        # Iterate to find a file name which is not already existing
        i = 1
        fileName = "id_ed25519_{}".format(i)
        while sshFolder.joinpath(fileName).exists() == True:
            i+=1
            fileName = "id_ed25519_{}".format(i)
            
        runCommandInShell("ssh-keygen -t ed25519 -C '{}' -f ~/.ssh/{} -N ''".format(email, fileName))
        publicKeyFile = "{}.pub".format(fileName)
        privateKeyPath = sshFolder.joinpath(fileName)
        publicKeyPath = sshFolder.joinpath(publicKeyFile)
        f = open(publicKeyPath, 'r')
        publicKey = f.readlines()
        return {
            "fileName": fileName,
            "filePath": privateKeyPath.resolve(),
            "publicKey": publicKey[0]
        }

    def addSSHConfig(self, host, config):
        self.configDict[host] = config
        self.writeConfig()

# configFile = "/Users/abhishekranjan/.ssh/config"

# ssh = SSHConfigManager(configFile)
# c = ssh.parseConfig()
# ssh.writeConfig()