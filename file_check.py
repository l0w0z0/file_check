import os
import tkinter.filedialog


# 增加选择文件夹按钮
def select_dir():
    # 调用tkinter.filedialog模块的askdirectory()函数
    # 返回值为选择的文件夹路径
    dir_path = tkinter.filedialog.askdirectory()
    # 将选择的文件夹路径赋值给变量
    global path
    path = dir_path
    # 设置文本框显示选择的文件夹路径
    text_path.delete(0.0, tkinter.END)
    text_path.insert(0.0, path)


# 定义保存用户配置文件的函数
def save_config():
    # 获取text_path文本框内容
    input_value = text_path.get(0.0, tkinter.END)
    # 保存用户配置文件
    with open(os.path.expanduser('~') + '\\Documents\\' + '文件名称统计配置.ini', 'w') as f:
        f.write(input_value)


def count_file():
    # 清空文本框
    text_result.delete(0.0, tkinter.END)
    save_config()
    # 获取文件夹下的所有文件
    file_path = tkinter.filedialog.askdirectory()
    files = os.walk(file_path)
    # print(files)
    all_data = {}
    # 将text_path文本框内容转换为字符串打印
    input_value = text_path.get(0.0, tkinter.END)
    # 将input_value字符串转换为字典，字典值为0，并赋值给all_data
    for kkk in input_value.split():
        all_data[kkk] = 0
    for curDir, dirs, files in os.walk(file_path):
        # print(files)
        for file in files:
            for data in all_data.keys():
                # print('**',data)
                if file.find(data) > -1:
                    all_data[data] = 1
                    break
    for data, value in all_data.items():
        if value == 0:
            # 将data值赋值给text_result文本框
            text_result.insert(0.0, "没找包含此名称的文件：" + data + '\n')
    # 判断text_result文本框内容是否为空，如果为空，则显示“所有文件都存在”
    if text_result.get(0.0, tkinter.END).find('没找包含此名称的文件') == -1:
        # 设置text_result文本框文字大小为4倍
        text_result.tag_config('big', font=('微软雅黑', 20, 'bold'))
        # 将“所有文件都存在”赋值给text_result文本框
        text_result.insert(0.0, '恭喜！所有文件都存在')


# 开启一个600*800的窗口
root = tkinter.Tk()
root.geometry('600x800')
root.title('文件名称统计')
# 设置全局字体大小
root.option_add('*Font', '微软雅黑,18')
# 设置窗口中心位置在屏幕中间
root.update_idletasks()
x = (root.winfo_screenwidth() - root.winfo_reqwidth() - 600) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight() - 800) / 2
root.wm_geometry("+%d+%d" % (x, y))

# 输入文本框标题
label_path = tkinter.Label(root, text='请输入需要查找的文件夹中文件所包含的名称，回车换行：')
label_path.grid(row=20, column=10)
label_path.place(x=10, y=20)

# 增加检查内容多行文本框
text_path = tkinter.Text(root, width=60, height=15)
text_path.place(x=40, y=60)
# 设置文本框内容
text_path.insert(0.0, '')
# 设置文本框内容
# text_path.insert(0.0,'国调\n冀北\n天津\n内蒙\n河北\n华中\n湖南\n青海\n四川\n西南\n福建\n东北\n辽宁\n龙江')


# 判断用户配置文件是否存在
if os.path.exists(os.path.expanduser('~') + '\\Documents\\' + '文件名称统计配置.ini'):
    # 读取用户配置文件
    with open(os.path.expanduser('~') + '\\Documents\\' + '文件名称统计配置.ini', 'r') as f:
        # 将path值赋值给text_path文本框
        text_path.delete(0.0, tkinter.END)
        text_path.insert(0.0, f.read())

# 判断text_path文本框内容是否为空，如果为空，则显示“请输入文件夹中文件所包含的名称”
if text_path.get(0.0, tkinter.END).isspace() == True:
    # 设置text_path文本框文字大小为4倍
    text_path.tag_config('big', font=('微软雅黑', 20, 'bold'))
    # 将“请输入文件夹中文件所包含的名称”赋值给text_path文本框
    text_path.insert(0.0, '请输入文件夹中文件所包含的名称')

# 增加开始检查按钮
button_start = tkinter.Button(root, text='开始检查', command=count_file)
button_start.place(x=40, y=330)
# 设置按钮字体大小
button_start.config(font=('微软雅黑', 16, 'bold'))

# 增加检查结果文本框
text_result = tkinter.Text(root, width=60, height=15)
text_result.place(x=40, y=400)
# 清空text_result文本框内容
text_result.delete(0.0, tkinter.END)

# 增加退出按钮
button_exit = tkinter.Button(root, text='退出', command=root.quit)
button_exit.place(x=500, y=700)
button_exit.config(font=('微软雅黑', 16, 'bold'))

# 设置主窗口循环显示
root.mainloop()
