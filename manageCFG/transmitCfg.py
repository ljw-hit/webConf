import paramiko
from scp import SCPClient
from config import *
remotePath = "/etc/haproxy/haproxy.cfg"
filePath = FilePath+"\commonMess\haproxy-text.cfg"
def uploadCfg(filePath,remotePath,SSH):
    host = SSH["host"]
    port = SSH["port"]
    username = SSH["username"]
    password = SSH["password"]
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    print(SSH)
    ssh_client.connect(host, port, username, password)
    scpclient = SCPClient(ssh_client.get_transport(), socket_timeout=15.0)

    try:
        scpclient.put(filePath, remotePath)
    except FileNotFoundError as e:
        print(e)
        print("系统找不到指定文件" + filePath)
    else:
        print("文件上传成功")


def getSSH(host,user,pwd):
    SSH = {}
    SSH["host"] = host
    SSH["port"] = 22
    SSH["username"] = user
    SSH["password"] = pwd
    return SSH

if __name__ == '__main__':
    SSH = getSSH("62.234.165.112","root","QGTiJ5vV6nJT6")
    uploadCfg(filePath,remotePath,SSH)
