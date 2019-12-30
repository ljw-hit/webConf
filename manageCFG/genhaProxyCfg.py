import json
import config
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


def ipJsonMess():
    filePath = config.FilePath+"/commonMess/"
    messJsonFile = open(filePath+"IpJson.json","w")
    ipfile = open(filePath+"proxy.txt","r",encoding='UTF-8')
    ipMess = ipfile.readlines()
    type = "in"
    ipJson = {}
    for line in ipMess:
        if "china" in line:
            type = "in"
            continue
        if "overseas" in line:
            type = "out"
            continue
        lines = line.split(" ")
        ssh = {}
        ssh["type"] = type
        ssh["usr"] = lines[1].strip()
        ssh["pwd"] = lines[2].strip()
        ssh["bindport"] = lines[3].strip()
        ipJson[lines[0].strip()] = ssh
    jsonStr = json.dumps(ipJson)
    messJsonFile.write(jsonStr)
    messJsonFile.close()
    ipfile.close()



if __name__ == '__main__':
    #manageCfg("1234","127.3.1.1","888")
    ipJsonMess()