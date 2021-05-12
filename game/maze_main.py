from tkinter import *
import tkinter as tk
from tkinter import messagebox

import maze_game
import maze_graphics
import time
from datetime import datetime

# 设置迷宫规模


x = 10  # 初始化迷宫的高
y = 10  # 初始化迷宫的宽
counter = 66600
running = False
minute = -1
display = '0'


class Application(tk.Frame):
    start = 0  # 记录游戏开始的时间戳
    end = 0  # 记录游戏结束的时间戳

    def __init__(self, master=None):
        # 构造函数

        tk.Frame.__init__(self, master)
        self.x = x
        self.y = y
        self.grid()
        self.field = self.createWidgets(x, y)
        self.game = maze_game.MazeGame(self.field, self.x - 2, self.y - 2)
        self.playGame()

    def createWidgets(self, x, y):
        # 创建图形化界面的一部分
        # 设置迷宫宽高
        yy = y * maze_graphics.ROOM_WIDTH_IN_PIX
        xx = x * maze_graphics.ROOM_HEIGHT_IN_PIX

        # 先设置整个 窗口 为白色背景 maze_graphics.BGC
        # Label(app,text="First").grid(row=0,sticky=E)#靠右
        self.start = time.time()
        now = round(time.time() - self.start, 0)
        # canva = tk.Canvas(self, width=100, height=40, background=maze_graphics.BGC)
        # canva.create_text(50,22,text = now)
        # print(now)
        # canva.grid()

        # tk.Button(self, text='start', command=bbb.start)
        # Button(window, text='start', command=ttt.start).pack(side=LEFT)

        # self.quitButton = tk.Button(self, text='skip', command=self.quit)
        # self.quitButton.grid()
        global label
        label = tk.Label(self, font=("Times New Roman", 22), fg='blue', text=now)
        label.grid()
        # label1 = tk.Label(self, font=("微软雅黑", 22), fg='blue', text=now).pack(side='right')
        # label1.grid()
        # label = Label(self.master, text="Welcome!", fg="black", font="Verdana 30 bold")
        # label.pack()

        field = tk.Canvas(self, width=yy, height=xx, background=maze_graphics.BGC)
        field.grid()
        # print("Canvas: xx=", xx, " yy=", yy, " w=", field.winfo_reqwidth(), " h=", field.winfo_reqheight())

        # 迷宫界面中间的 “游戏规则” 标签 Label
        self.textLabel = tk.Label(self, font=("Times New Roman", 11), fg='blue', text="Rules：１．The blue dot is the entrance, the red dot is the exit")
        self.textLabel.grid()
        self.textLabel = tk.Label(self, font=("Times New Roman", 11), fg='blue', text="         ２．Use direction '↑' '↓' '←' '→'　")
        self.textLabel.grid()

        # self.textLabel = tk.Label(self, font=("微软雅黑", 11), fg='blue', text=time.time())
        # self.textLabel.grid()

        # 功能按钮 Button，通过Frame开辟一个空间，再往里面打包（.pack）放进去 ，再设置 side='left'
        fm = Frame(height=30, width=180)
        Button(fm, text='', width=0, command=self.Start(label))
        fm1 = Frame(fm, height=30, width=60)
        # fm2 = Frame(fm, height=30, width=60)
        # fm3 = Frame(fm, height=30, width=60)
        fm4 = Frame(fm, height=30, width=60)
        fm.grid(row=2)
        fm1.pack(side='left')
        # fm2.pack(side='left')
        # fm3.pack(side='left')
        fm4.pack(side='right')

        now = round(time.time() - self.start, 0)
        print(now)

        Button(fm1, text="View Answer", width=10, command=self.answer).pack(side='left')
        # Button(fm2, text="time："+str(now), width=10).pack(side='left')
        # Button(fm2, text='start', width=10, command=sw.start).pack(side=LEFT)

        # Button(fm3, text="再来一次", width=10, command=self.playGame).pack(side='left')
        Button(fm4, text="Exit", width=10, command=self.stopGame).pack(side='right')
        return field  # 返回整个界面上的内容，整个领域

    def addHandler(self, field):
        # 添加一个按键处理
        seq = '<Any-KeyPress>'
        field.bind_all(sequence=seq, func=self.handleKey, add=None)
        field.bind("<Button-1>", self.xFunc1)
        # messagebox.showinfo("小提示！", "请在30秒内完成游戏！")

    def initGame(self):
        # 设置游戏初始化
        self.game.clearGame()
        self.game.drawGame()

    def answer(self):
        #  “答案”部分
        self.game.auto(x, y)
        self.stopGame()

    def xFunc1(self, event):
        global running

        if self.start == 0:
            self.start = time.time()
        ty = int((event.x - 20) / 35)
        tx = 9 - int((370 - event.y) / 35)
        print(f"鼠标左键点击了一次坐标是:x={event.x}y={event.y}")
        print(f"鼠标左键点击了一次坐标是:x={tx} y={ty}")
        # self.game.auto2(x, y, tx, ty)
        strs = self.game.location(tx, ty)
        if strs == "no":
            running = False
            messagebox.showinfo("Hints！", "you win!!！")

    def Start(self, label):
        global running
        global display

        running = True
        self.counter_label(label)
        # start['state'] = 'disabled'

    def counter_label(self, label):
        def count():
            if running:
                global counter
                global minute

                # To manage the intial delay.
                if counter == 66600:
                    display = "0"
                else:
                    tt = datetime.fromtimestamp(counter)
                    string = tt.strftime("%S")
                    display = string

                if minute == -1:
                    label['text'] = "0" + ":" + display
                else:
                    label['text'] = str(minute) + ":" + display  # Or label.config(text=display)

                label.after(1000, count)
                counter += 1
                # print("mod:" + str(int(display) % 60))
                if int(display) % 60 == 0:
                    minute += 1

        # Triggering the start of the counter.
        count()

    def stopGame(self):
        # 杀死这个应用
        self.done = True
        app.destroy()
        self.quit()

    def handleKey(self, event):
        # 按键处理程序，获取上下左右
        if False:
            print("handleKey: ", event.keysym, event.keycode, event.keysym_num)
        mv = None

        if event.keycode == 104:  # Down
            mv = 'D'
        elif event.keycode == 100:  # Left
            mv = 'L'
        elif event.keycode == 102:  # Right
            mv = 'R'
        elif event.keycode == 98:  # Up
            mv = 'U'
        elif event.keycode == 88:  # KP_Down
            mv = 'D'
        elif event.keycode == 80:  # KP_Up
            mv = 'U'
        elif event.keycode == 83:  # KP_Left
            mv = 'L'
        elif event.keycode == 85:  # KP_Right
            mv = 'R'
        elif event.keysym == 'Down':  # ??_Down
            mv = 'D'
        elif event.keysym == 'Up':  # ??_Up
            mv = 'U'
        elif event.keysym == 'Left':  # ??_Left
            mv = 'L'
        elif event.keysym == 'Right':  # ??_Right
            mv = 'R'
        else:
            return
        # Player's move
        if self.game.move(mv):
            # Solved - exit the program
            self.stopGame()

    def playGame(self):
        # 开始游戏
        self.initGame()
        self.addHandler(self.field)
        # self.start = time.time()
        # now = round(time.time() - self.start, 0)
        # label = tk.Label(self, font=("微软雅黑", 22), fg='blue', text=now)
        # label.grid()
        # ret = 66600
        # self.Start(label, ret)

    def protocol(self, param, closeWindow):
        # 添加此函数跳到一个空函数（closeWindow）后解决关闭窗口报错问题
        pass

    # def tick(self):
    #     global time1
    #     # 从运行程序的计算机上面获取当前的系统时间
    #     time2 = time.strftime('%H:%M:%S')
    #     # 如果时间发生变化，代码自动更新显示的系统时间
    #     if time2 != time1:
    #         time1 = time2
    #         clock.config(text=time2)
    #         # calls itself every 200 milliseconds
    #         # to update the time display as needed
    #         # could use >200 ms, but display gets jerky
    #     clock.after(200, tick)


def generateMaze():
    # 产生迷宫
    global x, y
    if width.get() == '' or height.get() == '':  # 规模框里不输入任何东西则执行默认规模10*10
        y, x = 12, 12
    else:
        y = int(width.get()) + 2
        x = int(height.get()) + 2
    window.destroy()  # 产生完成迷宫窗口后关闭 第一个设置迷宫规模的窗口window 对象


# 设置规模时 使输入框只能输入“数字”的模块相关的
def test(content):  # 如果不加上==""的话，会发现删不完。总会剩下一个数字
    if content.isdigit() or (content == ""):
        return True
    else:
        return False


# def xFunc1(event,self):
#     print(f"鼠标左键点击了一次坐标是:x={event.x}y={event.y}")
#     Application.answer(self)


# 设置规模窗口的部分
window = tk.Tk()
# window.title('DIY Maze！')
# window.geometry('450x255')
v1 = StringVar()
v2 = StringVar()
v1.set('10')
v2.set('10')

# time1 = ''
# status = Label(window, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
# status.grid(row=0, column=0)
# clock = Label(window, font=('times', 20, 'bold'), bg='green')
# clock.grid(row=0, column=1)
# tick()


# start = Button(Frame(window), text='Start', width=6, command=lambda: Start(window.title))
# Button(window, text = 'start', command = sw.start).pack(side = LEFT)

# sw = StopWatch(window)
# sw.pack(side=TOP)
# Button(window, text='start', command=sw.start).pack(side=LEFT)

testCMD = window.register(test)  # 需要将函数包装一下，必要的
widthLabel = tk.Label(text="设置迷宫高:").pack()
width = tk.Entry(window, show=None, textvariable=v1,
                 validate='key',  # 发生任何变动的时候，就会调用validatecommand
                 validatecommand=(testCMD, '%P')
                 )  # %P代表输入框的实时内容
# 当validate为key的时候，获取输入框内容就不可以用get（）
# 因为只有当validatecommand判断正确后，返回true。才会改变.get()返回的值.所以要用%P
width.pack()
heightLabel = tk.Label(text="设置迷宫宽:").pack()
height = tk.Entry(window, show=None, textvariable=v2, validate='key', validatecommand=(testCMD, '%P'))
height.pack()

# tk.Label(text="  ").pack()
# generate = tk.Button(window,text='生 成 迷 宫',width=11,height=1,command=generateMaze).pack()
generateMaze()
# tk.Label(text="  ").pack()
# tk.Label(fg='blue',font=("微软雅黑",10),text="推荐迷宫 10*10 ").pack()
# tk.Label(fg='blue',font=("微软雅黑",10),text="最大宽高最好不要超过12以免显示超出显示屏  ").pack()
window.mainloop()


# 正式运行整个迷宫窗口的部分
def closeWindow():
    return


app = Application()
app.master.title('MAZE')
app.protocol('WM_DELETE_WINDOW', closeWindow)  # 添加此句跳到一个空函数（closeWindow）后解决关闭窗口报错问题
app.mainloop()

# window.destroy() # IDEs 需要这个
# app.destroy()
