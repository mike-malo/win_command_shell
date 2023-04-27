# coding=utf-8
import json
import os
import socket
import time
from socket import *
import sys

HOST = '192.168.50.97'
PORT = 8003
BUF_SIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)


def doConnect():
    # socket连接服务器

    # 握手
    dic = "aaaaaaaaaaaaaaaaa"
    woshou = json.dumps(dic)
    tcpCliSock.sendall(woshou.encode('utf-8'))
    woshou = tcpCliSock.recv(BUF_SIZE)
    print(woshou)

    # print(sys.argv[1])

    # 发送设备编号
    dic = {'task': "terminal_machine", 'mid': 1}
    data1 = json.dumps(dic)
    tcpCliSock.sendall(data1.encode('utf-8'))
    data1 = tcpCliSock.recv(BUF_SIZE)  # 接收
    recv_data = data1.decode('utf-8', errors='ignore')  # 解码
    recv_data = recv_data[1:]  # 去掉前缀
    recv_data = json.loads(recv_data)  # 转换成JSON格式
    print(recv_data)


doConnect()


# 循环接收服务器信息
while True:
    # if not data1:
    #     break
    # data1 = input('>')

    try:
        data1 = tcpCliSock.recv(BUF_SIZE)  # 接收
        recv_data = data1.decode('utf-8', errors='ignore')  # 解码
        recv_data = recv_data[1:]  # 去掉前缀
        recv_data = json.loads(recv_data)  # 转换成JSON格式

        # 判断接收的数据类型

        print(recv_data)
        # 类型1: 打开文件
        if recv_data['type'] == 'program':
            print(recv_data['name'])
            print("D:\\files" + "\\")
            # print("start " + sys.argv[2] + recv_data['name'])
            command = "start " + sys.argv[2] + "\\" + recv_data['name']
            try:
                os.system(command)
            except OSError:
                pass
                continue

        # 类型2： 打开网页
        elif recv_data['type'] == 'drawing':
            print(recv_data['url'])
            os.system("start " + recv_data['url'])

    except error:
        pass
        try:
            tcpCliSock = socket(AF_INET, SOCK_STREAM)
            tcpCliSock.connect(ADDR)
            doConnect()
        except error:
            pass
        continue
        # time.sleep(1)
        # print("error 1")
        # while True:
        #     try:
        #         doConnect()
        #     except error:
        #         time.sleep(1)
        #         print("error 2")
        #         pass

