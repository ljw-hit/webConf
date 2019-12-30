import json

inFilePath = "F:\\beijing\多级代理\ShadowSock-4.0.10\gui-config-total.json"
outFilePath = "F:\\beijing\多级代理\ShadowSock-4.0.10\gui-config.json"

def readCfg(filePath):
  cfgFile = open(filePath,"r")
  cfgStr = cfgFile.read()
  cfgJson = json.loads(cfgStr)
  cfgFile.close()
  return cfgJson


def writeCfg(FilePath,cfgJson,ip):
    outCfgFile = open(FilePath,"w")
    bindPort = 0
    for dic in cfgJson['configs']:
        if ip in dic['server']:
            bindPort = dic['server_port']
            cfgJson['configs'] = [dic]
            break
    else:
        print("没有对应配置")
    cfgStr = json.dumps(cfgJson)
    outCfgFile.write(cfgStr)
    outCfgFile.close()
    return bindPort


def manageCfg(ip):
    cfgJson = readCfg(inFilePath)
    bindIp = writeCfg(outFilePath,cfgJson,ip)
    return bindIp

if __name__ == '__main__':
    bindIp = manageCfg("tw.0bad.com")
    print(bindIp)

