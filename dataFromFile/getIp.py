import json
import config

filePath = config.FilePath+"/commonMess/"

def ipSshDic():
    jsonFile = open(filePath + "IpJson.json")
    ipStr = jsonFile.read()
    ipJson = json.loads(ipStr)
    return ipJson


def ipData():
    ipJson = ipSshDic()
    ipData = {}
    for k in ipJson:

        ipData[k] = ipJson[k]["type"]
    return ipData

def ipSSH(ip):
    ipJson = ipSshDic()
    SSH = {}
    if ipJson[ip]!=None:
        SSH["host"] = ip
        SSH["port"] = 22
        SSH["username"] = ipJson[ip]['usr']
        SSH["password"] = ipJson[ip]['pwd']
    return SSH

def ipCaEnc(ip):
    ipJson = ipSshDic()
    ca = ipJson[ip]['ca']
    enc = ipJson[ip]['enc']
    return ca,enc


def ipBindPort(ip):
    ipJson = ipSshDic()
    bindPort = "11000"
    if ipJson[ip]!=None and ipJson[ip]["bindport"]!="-1":
        bindPort = ipJson[ip]["bindport"]
    return bindPort







if __name__ == '__main__':
    ipData()