
inFilePath = "F:\\beijing\多级代理\haproxy.cfg"
outFilePath = "F:\\beijing\多级代理\haproxy-text.cfg"


def readCfg(filePath):
    haProxyCfg = open(filePath,"r")
    cfgLines = haProxyCfg.readlines()
    haProxyCfg.close()
    return cfgLines


def writeCfg(filePath,cfgLines,config):
    haProxyCfg = open(filePath,"w")
    j=0
    for line in cfgLines:
        if 'bind *' in line:
            lines = line.split(":")
            lines[1] = str(config['bind'])
            cfgLines[j] = ":".join(lines)+"\n"
            #print(cfgLines[j])

        if 'server server' in line:
            lines = line.split(" ")
            ipPort = lines[2].split(":")
            ipPort[0] = config["vpsIp"]
            ipPort[1] = config["vpsPort"]
            ipPortStr = ":".join(ipPort)
            lines[2] = ipPortStr
            cfgLines[j] = " ".join(lines)+"\n"
            #print(line)
        j = j+1

    print(cfgLines)
    haProxyCfgStr = "".join(cfgLines)
    haProxyCfg.write(haProxyCfgStr)
    haProxyCfg.close()

def manageCfg(bindIp,vpsIp,vpsPort):
    config  = {}
    config["bind"] = bindIp
    config["vpsIp"] = vpsIp
    config["vpsPort"] = vpsPort

    cfgLines = readCfg(inFilePath)
    writeCfg(outFilePath,cfgLines,config)

if __name__ == '__main__':
    manageCfg("1234","127.3.1.1","888")
