#引入 tkinter module
from tkinter import *
#從tkinter中引入ttk加強模組
from tkinter import ttk
#引入 Pillow module
from PIL import Image, ImageTk
#引入ttk module, 並取名為ttk
import tkinter.ttk as ttk
# 引入 tkscrolledframe module
from tkscrolledframe import ScrolledFrame
#從tkinter種引從tkinter種引入filedialog
from tkinter import filedialog

#單選檔案，並以String回傳路徑
filePath = filedialog.askopenfilename(title="選取照片", initialdir="C:/Users/SP513-52N/Documents/Python_2023Spring/class3", multiple = True)

print(filePath)
# root = Tk()
# root.title("20230305")
# root.geometry("880x650")

# # Create a ScrolledFrame widget
# sframe1 = ScrolledFrame(root, width=300, height=300, bg="blue")
# sframe1.pack()

# #Bind the arrow keys and scroll wheel
# sframe1.bind_arrow_keys(root)
# sframe1.bind_scroll_wheel(root)

# #Create a frame within the ScrolledFrame
# inner_frame = sframe1.display_widget(Frame)

# button1 = Button(inner_frame, text="1", height=5)
# button2 = Button(inner_frame, text="2", height=5)
# button3 = Button(inner_frame, text="3", height=5)
# button4 = Button(inner_frame, text="4", height=5)
# button5 = Button(inner_frame, text="5", height=5)

# button1.grid(row=0)
# button2.grid(row=1)
# button3.grid(row=2)
# button4.grid(row=3)
# button5.grid(row=4)


# def choose_brand():
#     titleVar.set("廠牌: "+ str(box.current()+1)+". "+box.get())

# titleVar = StringVar()
# titleVar.set("廠牌: ")
# #建立標題 Label
# title1label = Label(root, textvariable=titleVar)
# title1label.grid(row=0, column=0, columnspan=2, sticky=W)

# #建立下拉式選單 Combobox
# box = ttk.Combobox(root, values=["BMW", "Mercedes Benz", "Audi"])
# box.grid(row=1, column=0, sticky=W)
# box.current(0)
# #建立按鈕Button
# Choose = Button(text="OK", command=choose_brand)
# Choose.grid(row=2, column=0, sticky=W)


#建立清單列表 Listbox
# listbox = Listbox(root)
# #加入列表選項
# listbox.insert(1,"A1")
# listbox.insert(2,"A3")
# listbox.insert(3,"A4")
# listbox.pack()

#宣告用於Listbox的文字
# listVar = StringVar()
# #建立list BMW
# BMW=["1 Series (F40)","1 Series (F52)","2 Series Gran Coupé","2 Series","3 Series","4 Series","5 Series","6 Series","7 Series","8 Series","X1","X2","X3","X4","X5","X6","X7","Z4","2 Series Active Tourer","i3 (G28)","i4","i7","iX1","iX3","iX"]
# Mercedes=["A-Class(Hatchbacks)","A-Class(Sedans)","C-Class","CLA","CLS","E-Class","EQE","EQS","S-Class","C-Class","CLA","E-Class","E-Class","EQA","EQB","EQC","G-Class","GLA","GLB","GLC","GLE","GLS","AMG GT","AMG GT 4-Door Coupé","AMG SL","AMG One","B-Class","Citan Van","Viano","EQV"]
# Audi=["A1","A3","A4","A5","A6","A7","A8","e-tron GT","TT","R8","Q2","Q3","2019","Q4 e-tron","2021","Q5","Q5 e-tron","Q6","Q7","Q8","e-tron"]
# #將多個選項內容存入 listVar
# listVar.set(BMW)
# #建立清單列表 Listbox
# listbox = Listbox(root, selectmode="extended", listvariable=listVar)
# listbox.grid(row=0, column=0)
#root.mainloop() 