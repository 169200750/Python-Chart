import tkinter as tk

def send():
    msg = input_text.get('0.0', tk.END)
    print(msg)

app = tk.Tk()
app.title('在线聊天室')

# 显示消息框
mag_frame = tk.Frame(app, width=480, height=300)
mag_frame.grid(row=0, column=0)
mag_frame.grid_propagate(0)  # 固定Frame的大小
mag_text = tk.Text(mag_frame, bg='skyblue')
mag_text.grid()
mag_text.insert('0.0', '请输入姓名')

# 输入
input_frame = tk.Frame(app, width=480, height=100)
input_frame.grid(row=1, column=0)
input_frame.grid_propagate(0)
input_text = tk.Text(input_frame, bg='yellow')
input_text.grid()

# 发送按钮
btn_frame = tk.Frame(app, width=480, height=20)
btn_frame.grid(row=2, column=0, sticky='E')
button = tk.Button(btn_frame, text='单机发送', command=send, bg='skyblue', width=69)
button.grid()
app.mainloop()
