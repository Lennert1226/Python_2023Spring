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


# 建立下getvalue function
def getValue(a):

    # 取得RGB
    r = int(color_scale.get())
    g = int(color_scale2.get())
    b = int(color_scale3.get())

    # 數值轉換為16進位
    hex = "#{:02x}{:02x}{:02x}".format(r, g, b)

    #分別設定Label文字內容
    title1label1["text"]="R: "+str(color_scale.get())
    title1label2["text"]="G: "+str(color_scale2.get())
    title1label3["text"]="B: "+str(color_scale3.get())
    
    # 分別設定statusBar1背景
    statusBar1["bg"] = hex
    statusBar1["text"] = hex

# 建立標題 Label
title1label = Label(root, text="選擇顏色(R,G,B)")
title1label.grid(row=0, column=0, columnspan=2, sticky=W)

# 建立 Scale 元件
color_scale = Scale(root, from_=0, to=255, orient="horizontal", resolution=1, length=300, showvalue=True, command=getValue)
color_scale.grid(row=2, column=0, columnspan=3)

# 建立 Scale 元件
color_scale2 = Scale(root, from_=0, to=255, orient="horizontal", resolution=1, length=300, showvalue=True, command=getValue)
color_scale2.grid(row=4, column=0, columnspan=3)

# 建立 Scale 元件
color_scale3 = Scale(root, from_=0, to=255, orient="horizontal", resolution=1, length=300, showvalue=True, command=getValue)
color_scale3.grid(row=6, column=0, columnspan=3)

# 建立標題 Label
title1label1 = Label(root, text="R: 0")
title1label1.grid(row=1, column=0, columnspan=2, sticky=W)

# 建立標題 Label
title1label2 = Label(root, text="G: 0")
title1label2.grid(row=3, column=0, columnspan=2, sticky=W)

# 建立標題 Label
title1label3 = Label(root, text="B: 0")
title1label3.grid(row=5, column=0, columnspan=2, sticky=W)

# 建立 Label
statusBar1 = Label(root, text="", fg="white", bg="white", relief="sunken", bd=2, font=(20), anchor="center")
statusBar1.grid(row=7, column=0, columnspan=3, sticky=W+E+S)

root.mainloop()