# 引入 tkinter module
from tkinter import *
# 引入 tkscrolledframe module
from tkscrolledframe import ScrolledFrame

# 建立主視窗 Frame
root = Tk()
# 設定視窗標題
root.title("Sign Up")
# 設定視窗大小為 300x100,視窗(左上角)在螢幕上的座標位置為(500,150)
root.geometry("500x375")


# def getValue(e):
#     value.set("年齡: "+str(year_scale.get()))



# # 建立 Scale 元件
# year_scale = Scale(root, from_=0, to=100, orient="horizontal", resolution=1, length=300, showvalue=True, command=getValue)
# year_scale.grid(row=1, column=0, columnspan=3)

# # 建立字串變數
# value = StringVar()
# value.set("身高: 0")

# # 簡例 Label
# statusBar1 = Label(root, textvariable=value, fg="black", bg="white", anchor=W, relief="sunken",bd=2)
# # 加入視窗
# statusBar1.grid(row=2,column=0, columnspan=3, sticky=W+E+S)

# # 建立標題 Label
# title1label1 = Label(root, text="身高: ")
# title1label1.grid(row=3, column=0, columnspan=2, sticky=W)

# # 建立標題 Label
# title1label2 = Label(root, textvariable=value)
# title1label2.grid(row=3, column=1, columnspan=2, sticky=W)


#建立字串變數
value = StringVar()

# # 建立標題 Spinbox
# height = Spinbox(root, from_=99, to=250, textvariable=value)
# height.grid(row=4, column=0, columnspan=3, sticky=W+E+S)

# 建立標題 Label
titlelabel = Label(root, text="選擇顏色(R,G,B)")
titlelabel.grid(row=0, column=0, columnspan=2, sticky=W)

def getValue(e):
    value.set("年齡: "+str(tall_scale.get()))

# 建立 Scale 元件
tall_scale = Scale(root, from_=0, to=255, orient="horizontal", resolution=1, length=300, showvalue=True, command=getValue)
tall_scale.grid(row=1, column=0, columnspan=3)


root.mainloop()