from manageCFG import genhaProxyCfg
from manageCFG import transmitCfg
from manageCFG import ModifySSCfg
from remoteControl import reHaproxy
import sys


remotePath = "/etc/haproxy/haproxy.cfg"
filePath = "F:\\beijing\多级代理\haproxy-text.cfg"

def choiceLink(proxyIp,vpsIp,vpsPort):

    bindIp = ModifySSCfg.manageCfg(proxyIp)
    genhaProxyCfg.manageCfg(bindIp,vpsIp,vpsPort)
    SSH = transmitCfg.getSSH(proxyIp,"root","QGTiJ5vV6nJT6")
    transmitCfg.uploadCfg(filePath,remotePath,SSH)
    reHaproxy.reStartHaproxy(SSH)

def main():
    proxyIp = sys.argv[1]
    vpsIp = sys.argv[2]
    vpsPort = sys.argv[3]
    choiceLink(proxyIp,vpsIp,vpsPort)

if __name__ == '__main__':
    choiceLink("62.234.165.112","107.173.251.191","12306")