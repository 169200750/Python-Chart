import socket
import threading
import tkinter as tk

# 创建套接字
a = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5678))
print('已链接服务端,通讯加密中')

# 数据接收
def shou(s, msg_texe):
    recv_data = s.recv(1024).decode('utf-8')
    msg_text.insert(tk.END, recv_data)
    while 1:
        recv_data = s.recv(1024).decode('utf-8')
        msg_text.insert(tk.END, recv_data)

# 数据发送
def send():
    global a
    if a == 0:
        msg = input_text.get('0.0', tk.END)
        s.send(msg.encode('utf-8'))
        input_text.delete('0.0', tk.END)
    else:
        msg = input_text.get('0.0', tk.END)
        s.send(msg.encode('utf-8'))
        input_text.delete('0.0', tk.END)
        msg_text.delete('0.0', tk.END)
        a = 0

app = tk.Tk()
app.title('在线聊天室')

# 显示消息框
msg_frame = tk.Frame(app, width=490, height=300)
msg_frame.grid(row=0, column=0, padx=6, pady=6)
msg_frame.grid_propagate(0)  # 固定Frame的大小
msg_text = tk.Text(msg_frame, bg='white')
msg_text.grid()

# 输入
input_frame = tk.Frame(app, width=490, height=100)
input_frame.grid(row=1, column=0)
input_frame.grid_propagate(0)
input_text = tk.Text(input_frame, bg='white')
input_text.grid()

# 发送按钮
btn_frame = tk.Frame(app, width=490, height=30)
btn_frame.grid(row=2, column=0)
button = tk.Button(btn_frame, text='单 击 发 送', command=send, bg='skyblue', width=69)
button.grid()

# 线程
t1 = threading.Thread(target=shou, args=(s, msg_text))
t1.daemon = True
t1.start()
app.mainloop()
# s.close()
