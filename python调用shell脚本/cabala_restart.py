#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
def ssh(sys_ip,username,password,cmds):
    try:      
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(sys_ip, 22, username=username, password=password, timeout=20)
        
        #key_file = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
        #ssh.connect(sys_ip, 22, username=username, pkey=key_file, timeout=20)      
        #stdin, stdout, stderr = client.exec_command(cmds[key])

        stdin, stdout, stderr = client.exec_command(cmds)
        result = stdout.readlines()
        return result
    except Exception as e:
        print(e)
    finally:
        client.close()
 
if __name__=="__main__":
    sys_ip = "10.12.4.132"
    username = "root"
    password = "v8ugU3l25fG4"
    cmds = "/usr/bin/sh /home/shell_file/cabala_restart.sh"
    ssh(sys_ip,username,password,cmds) 
    print("正常启动")
