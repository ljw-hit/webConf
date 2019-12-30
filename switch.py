from manageCFG import genhaProxyCfg
from manageCFG import transmitCfg
from manageCFG import ModifySSCfg
from remoteControl import reHaproxy
from dataFromFile.getIp import *
import sys

remotePath = "/etc/haproxy/haproxy.cfg"
filePath = "F:\\beijing\多级代理\haproxy-text.cfg"

def getSshList(links):
    sshList = []
    print(links)
    for ip in links:
        sshList.append(ipSSH(ip))
    return sshList


def choiceLink(links):
    bindPort = 0
    serverPort = 0
    ssList= getSshList(links)
    for i in range(len(links)-1):
        if i==0:
            bindPort = ModifySSCfg.manageCfg(links[i])
            serverPort = ipBindPort(links[i+1])
            genhaProxyCfg.manageCfg(bindPort,links[i+1],serverPort)
            transmitCfg.uploadCfg(filePath,remotePath,ssList[i])
            reHaproxy.reStartHaproxy(ssList[i])
            print(bindPort,serverPort)
            bindPort = serverPort
            continue

        serverPort = ipBindPort(links[i + 1])
        genhaProxyCfg.manageCfg(bindPort, links[i + 1], serverPort)
        transmitCfg.uploadCfg(filePath, remotePath, ssList[i])
        reHaproxy.reStartHaproxy(ssList[i])
        print(bindPort,serverPort)
        bindPort = serverPort







def main():
    proxyIp = sys.argv[1]
    vpsIp = sys.argv[2]
    vpsPort = sys.argv[3]
    choiceLink(proxyIp,vpsIp,vpsPort)

if __name__ == '__main__':
    links = ["62.234.165.112","107.173.251.191","66.42.107.179"]
    choiceLink(links)