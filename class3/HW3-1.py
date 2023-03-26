# 引入 tkinter module
from tkinter import *
# 引入 tkscrolledframe module
from tkscrolledframe import ScrolledFrame

# 建立主視窗 Frame
root = Tk()
# 設定視窗標題
root.title("午餐系統")
# 設定視窗大小為 300x100,視窗(左上角)在螢幕上的座標位置為(500,150)
root.geometry("300x100+500+150")

def choose_brand():
# 建立標題 label
titleVar.set("廠牌: "+ str(box.current()+1)+" "+box.get())
titlelabel2 = Label(root, text="請選擇型號: ")
titlelabel2.grid(row=3, column=0, columnspan=2, sticky=W)

listVar = StringVar()

if box.get() == "BMW":

listVar.set(BMW)

listbox = Listbox(root, selectmode="extended", listvariable=listVar)
listbox.grid(row=4, column=0, columnspan=3, sticky=W)
elif 