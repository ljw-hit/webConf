import os
import paramiko
from manageCFG import transmitCfg
def reStartHaproxy(SSH):
    cmd = "systemctl restart haproxy"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    host = SSH["host"]
    port = SSH["port"]
    username = SSH["username"]
    password = SSH["password"]
    client.connect(host, port, username, password)
    try:
        stdin, stdout, stderr = client.exec_command(cmd,timeout=1000)
        result = stdout.readlines().decode('utf-8')
        print(result)
        print(stderr.read())
        print(stdin.read())
    except :
        print("重启Haproxy失败")

    client.close()

#测试远程服务器到vps的延时
def getDelay(SSH,ip):
    cmd = "ping -c 5 "+ip
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    host = SSH["host"]
    port = SSH["port"]
    username = SSH["username"]
    password = SSH["password"]
    client.connect(host, port, username, password)
    try:
        stdin, stdout, stderr = client.exec_command(cmd,timeout=4000)
        result = stdout.read().decode('utf-8')
        lines = result.splitlines()
        delay = lines[-1].split("=")[1]
        delay = delay.split("/")[1]
        print(delay+"ms")
        return delay+"ms"
    except Exception as e:
        print(e)
        print("getDelay cmd error")

    client.close()

#测试本机到远程服务器的延迟
def getLocalDelay(ip):
   cmd = "ping -n 5 "+ip
   try:
     result = os.popen(cmd)
     resultStr = result.readlines()
     mess = resultStr[-1].split("，")
     delay = mess[-1].strip()
     delay = delay.split("=")[1].strip()
     print(delay)
     return delay
   except:
     print("getDelay cmd error")




if __name__ == '__main__':
    SSH = transmitCfg.getSSH("47.75.200.81","root","hitcs2019!")
    #reStartHaproxy(SSH)
    getDelay(SSH,"107.173.251.191")
    getLocalDelay("47.75.200.81")
    getLocalDelay("107.173.251.191")