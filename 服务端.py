import socket
import threading
import time

# 数据接收
def JieShou(new_s, socket_list):
    try:
        nikename = new_s.recv(1024).decode('utf-8').strip()
    except:
        new_s.close()
        socket_list.remove(new_s)
        for i in socket_list:
            i.send('\n公告: 一个未知的人离开了聊天室......'.encode('utf-8'))
        return None
    for i in socket_list:
        i.send(f'\n公告: 欢迎 {nikename} 进入在线聊天室........\n'.encode('utf-8'))
    while 1:
        try:
            recv_data = new_s.recv(1024).decode('utf-8')
            print(recv_data)
            send_time = time.strftime('%Y-%m-%d %H:%M:%S\n', time.localtime(time.time()))
            for i in socket_list:
                i.send(f'\n {nikename} {send_time}'.encode('utf-8'))
                i.send(f'\n · {recv_data}\n'.encode('utf-8'))
        except:
            new_s.close()
            socket_list.remove(new_s)
            for i in socket_list:
                i.send(f'\n公告: {nikename} 离开了聊天室......\n'.encode('utf-8'))
            break

# 数据发送
def fa(new_s):
    while 1:
        msg = input('')
        new_s.send(msg.encode('utf-8'))

# 创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定
s.bind(("", 5678))
# 监听
s.listen(5)
print('服务端处于监听状态，等待客户端接入..........')
socket_list = []
while 1:
    # 接入
    new_s, addr = s.accept()
    print('客户端已接入')
    socket_list.append(new_s)
    new_s.send('请输入昵称:'.encode('utf-8'))
    t1 = threading.Thread(target=JieShou, args=(new_s, socket_list))
    t2 = threading.Thread(target=fa, args=(new_s,))
    t1.start()
    t2.start()
# new_s.close()
# s.close()
