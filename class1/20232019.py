#引入 tkinter module
from tkinter import *
#引入 Pillow module
from PIL import Image, ImageTk
#引入ttk module, 並取名為ttk
import tkinter.ttk as ttk
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title("20232019")
#設定視窗大小為 300x100，視窗(左上角)在螢幕上的座標位置為(500，150)
root.geometry("1000x300+500+150")
#開啟圖片
img = Image.open("C:/Users/SP513-52N/Documents/Python_2023Spring/class1/unnamed.png")
tk_img = ImageTk.PhotoImage(img)
root.iconphoto(True, tk_img)

def Start():
    pass

# #建立 Label
# label1=Label(root, text="flat", relief="flat")

# #加入視窗
# label1.pack()
# label2=Label(root, text="flat", relief="groove")
# label2.pack()
# label3=Label(root, text="flat", relief="raised")
# label3.pack()
# label4=Label(root, text="flat", relief="ridge")
# label4.pack()
# label5=Label(root, text="flat", relief="solid")
# label5.pack()
# label6=Label(root, text="flat", relief="sunken")
# label6.pack()

Button1=Button(root, text="Start", fg="black", bg="white")
Button1.pack()

Button2=Button(root, text="Stop", fg="black", bg="white")
Button2.pack()

statusBar1 = Label(root, text="processing...", fg="black", bg="white", anchor=W, relief="sunken", bd=2)
#加入視窗
statusBar1.pack(side="bottom", fill="x")

# table = ttk.Treeview(root, columns=["Product Name", "Unit Price", "Quantity", "Subtotal"])
# #Create columns title
# table.heading("#0", text="Pruduct Name")
# table.heading("#1", text="Unit Price")
# table.heading("#2", text="Quantity")
# table.heading("#3", text="Subtotal")
# #set column type
# table.column("#0", width=250, anchor=CENTER)
# table.column("#1", anchor = CENTER)
# table.column("#2", anchor = CENTER)
# table.column("#3", anchor = CENTER)
# #建立內容，從total行是用淺藍色底
# table.tag_configure("totalcolor", background="#E7E2E2")

# table.insert('', index="end", text="Sofa", values=("20000", "2", "40000"))
# table.pack()
#執行主程式
root.mainloop()