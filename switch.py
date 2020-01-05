from manageCFG import genhaProxyCfg
from manageCFG import transmitCfg
from manageCFG import ModifySSCfg
from remoteControl import reHaproxy
from dataFromFile.getIp import *
from remoteControl.reHaproxy import *
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
    print("choiceLink")
    bindPort = 0

    ssList= getSshList(links)
    for i in range(len(links)-1):
        if i==0:
            bindPort = ModifySSCfg.manageCfg(links[i],links[len(links)-1])
            serverPort = "11000"
            #只经过一层代理
            if i+1 == len(links)-1:
                serverPort = ipBindPort(links[i+1])
            genhaProxyCfg.manageCfg(bindPort,links[i+1],serverPort)
            transmitCfg.uploadCfg(filePath,remotePath,ssList[i])
            reHaproxy.reStartHaproxy(ssList[i])
            print(bindPort,serverPort)
            bindPort = serverPort
            continue
        if i == len(links)-2:
            serverPort = ipBindPort(links[i + 1])
            genhaProxyCfg.manageCfg(bindPort, links[i + 1], serverPort)
            transmitCfg.uploadCfg(filePath, remotePath, ssList[i])
            reHaproxy.reStartHaproxy(ssList[i])
            print(bindPort,serverPort)
            bindPort = serverPort
            continue
        #代理服务端口
        serverPort = "11000"
        genhaProxyCfg.manageCfg(bindPort, links[i + 1], serverPort)
        transmitCfg.uploadCfg(filePath, remotePath, ssList[i])
        reHaproxy.reStartHaproxy(ssList[i])
        print(bindPort, serverPort)
        bindPort = serverPort

    linkMessage = "localhost"
    for i in range(len(links)):
         ip = links[i]

         linkMessage+="-->"+ip
    return linkMessage

def delay(links):
    ssList= getSshList(links)
    delayList = []
    for i in range(len(links)-1):
        if i == 0:
            delay = getLocalDelay(links[0])
            delayList.append(delay)
            delay = getDelay(ssList[i],links[i+1])
            delayList.append(delay)
            continue
        delay = getDelay(ssList[i], links[i + 1])
        delayList.append(delay)
    linkMessage = "localhost"
    for i in range(len(links)):
        ip = links[i]
        delay = delayList[i]
        linkMessage+="-->"+str(delay)+"-->"+ip
    print(linkMessage)
    return linkMessage


def main():
    proxyIp = sys.argv[1]
    vpsIp = sys.argv[2]
    vpsPort = sys.argv[3]
    choiceLink(proxyIp,vpsIp,vpsPort)

if __name__ == '__main__':
    links = ["62.234.165.112","107.173.251.191","66.42.107.179"]
   # choiceLink(links)
    delay(links)