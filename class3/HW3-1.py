# 引入 tkinter module
from tkinter import *
# 引入 tkscrolledframe module
from tkscrolledframe import ScrolledFrame
#引入 tkinter module
from tkinter import *
#從tkinter中引入ttk加強模組
from tkinter import ttk
import tkinter.ttk as ttk

# 建立主視窗 Frame
root = Tk()
# 設定視窗標題
root.title("Car Rental System")
# 設定視窗大小為 300x100,視窗(左上角)在螢幕上的座標位置為(500,150)
root.geometry("500x300")

# 建立list BMW
BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3Series","4 Series","5 Series","6 Series","7 Series","8Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3(G28)","i4","i7","iX1","iX3","iX"]
Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]
def choose_brand():
    # 建立標題 Label
    titleVar.set("廠牌: "+ str(box.current()+1)+". "+box.get())
    title1label2 = Label(root, text="請選擇型號: ")
    title1label2.grid(row=3,column=0, columnspan=2, sticky=W)
    #宣告用於ListBox的文字變數
    listVar = StringVar()
    if box.get() == "BMW":
        # 將多個選項內容存入listVar
        listVar.set(BMW)
        # 建立清單列表 ListBox
        listbox = Listbox(root,selectmode="extended", listvariable=listVar)
        listbox.grid(row=4,column=0, columnspan=3,sticky=W)
    elif box.get() == "Mercedes Benz":
        # 將多個選項內容存入listVar
        listVar.set(Mercedes)
    # 建立清單列表 ListBox
        listbox = Listbox(root,selectmode="extended", listvariable=listVar)
        listbox.grid(row=4,column=0, columnspan=3,sticky=W)
    
    elif box.get() == "Audi":
        # 將多個選項內容存入listVar
        listVar.set(Audi)
    # 建立清單列表 ListBox
    listbox = Listbox(root,selectmode="extended", listvariable=listVar)
    listbox.grid(row=4,column=0, columnspan=3,sticky=W)

# 建立字串變數
titleVar = StringVar()
titleVar.set("廠牌:")
# 建立標題 Label
title1label1 = Label(root, textvariable=titleVar)
title1label1.grid(row=0,column=0, columnspan=2, sticky=W)
# 建立下拉式選單 Combobox
box = ttk.Combobox(root, values=["BMW", "Mercedes Benz", "Audi"])
box.grid(row=1, column=0, sticky=W)
box.current(1)
# 建立按鈕 Button
Choose = Button(text="OK", command=choose_brand)
Choose.grid(row=2, column=0, sticky=W)

root.mainloop()