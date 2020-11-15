import pprint
pp = pprint.PrettyPrinter(indent=4)

configFile = "/Users/abhishekranjan/.ssh/config"
configFileTemp = "/Users/abhishekranjan/.ssh/config2"

def parseConfig():
    configDict = {}
    f = open(configFile, 'r')
    readingConfig = False
    configName = ""
    for line in f:
        lineOrig = line
        line = line.strip()
        if len(line) == 0:
            print("Empty:", line)
            continue
        if line[0] == '#':
            print("Comment:", line)
            continue
        
        lineSplit = line.split(" ")
        attr = lineSplit[0]
        value = lineSplit[1]

        # If we've reached the next config
        if readingConfig and attr == "Host":
            readingConfig = True
            configDict[value] = {}
            configName = value
            continue

        # If we're reading a particular config
        if readingConfig and attr != "Host":
            configDict[configName][attr] = value
            continue

        if lineSplit[0] != "Host":
            raise RuntimeError("Expected Host to be encountered")
        
        if lineSplit[0] == "Host":
            readingConfig = True
            configDict[lineSplit[1]] = {}
            configName = lineSplit[1]
            
    pp.pprint(configDict)
    return configDict

def writeConfig(configFileTemp, configDict):
    finalConfig = ""
    for key in configDict.keys():
        singleConfig = "Host {}\n".format(key)
        # print(key, configDict[key])
        for intKey in configDict[key].keys():
            singleConfig += "    {} {}\n".format(intKey, configDict[key][intKey])
        # print(singleConfig)
        finalConfig += singleConfig
    print(finalConfig)
    f = open(configFileTemp, 'w')
    f.write(finalConfig)


c = parseConfig()
writeConfig(configFileTemp, c)