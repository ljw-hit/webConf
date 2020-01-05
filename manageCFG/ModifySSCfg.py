import json
from config import FilePath,ShadowSockPath
from dataFromFile.getIp import ipCaEnc,ipBindPort
inFilePath = FilePath+"\commonMess\gui-config-total.json"
outFilePath = ShadowSockPath + "\gui-config.json"

def readCfg(filePath):
  cfgFile = open(filePath,"r")
  cfgStr = cfgFile.read()
  cfgJson = json.loads(cfgStr)
  cfgFile.close()
  return cfgJson


def writeCfg(FilePath,cfgJson,nextIp,lastIp):
        outCfgFile = open(FilePath,"w")
        bindPort = ipBindPort(nextIp)
        ca,enc = ipCaEnc(lastIp)

        dic = {}
        dic["server"] = nextIp
        dic["server_port"] = bindPort
        dic["password"] = ca
        dic["method"] = enc
        dic["plugin"] = ""
        dic["plugin_opts"] = ""
        dic["plugin_args"] = ""
        dic["remarks"] = ""
        dic["timeout"] = 5
        cfgJson['configs'] = [dic]

        cfgStr = json.dumps(cfgJson)
        outCfgFile.write(cfgStr)
        outCfgFile.close()
        return bindPort


def manageCfg(nextIp,lastIp):
    cfgJson = readCfg(inFilePath)
    bindIp = writeCfg(outFilePath,cfgJson,nextIp,lastIp)
    return bindIp

if __name__ == '__main__':
    bindIp = manageCfg("66.42.107.179","66.42.107.179")
    print(bindIp)

