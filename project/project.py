from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from email.mime.multipart import MIMEMultipart
import smtplib


import tkinter.ttk as ttk
root = Tk()
root.title("Shoes Gathering")
#儲存使用者的email及password(最後要寄帳單給使用者)
userInfo = [["email"],["password"]]

cost = [["money"]]

root.geometry("880x650")
def showdetail():
    detailWindow = Toplevel(root)
    detailWindow.geometry('850x250')

    table = ttk.Treeview(detailWindow, columns=['Unit Price', 'Quantity', 'Subtotal'])
    table.heading('#0', text='Product Name')
    table.heading('#1', text='Unit Price')
    table.heading('#2', text='Quantity')
    table.heading('#3', text='Subtotal')

    table.column('#0', width=250, anchor=CENTER)
    table.column('#1', anchor=CENTER)
    table.column('#2', anchor=CENTER)
    table.column('#3', anchor=CENTER)

    table.tag_configure('totalcolor', background='gray')

    subtotal1 = int(productnumber1["text"])*int(productprice1["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname1["text"], values=[productprice1["text"], productnumber1["text"],subtotal1])
    subtotal2 = int(productnumber2["text"])*int(productprice2["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname2["text"], values=[productprice2["text"], productnumber2["text"],subtotal2])
    subtotal3 = int(productnumber3["text"])*int(productprice3["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname3["text"], values=[productprice3["text"], productnumber3["text"],subtotal3])
    subtotal4 = int(productnumber4["text"])*int(productprice4["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname4["text"], values=[productprice4["text"], productnumber4["text"],subtotal4])
    
    total = subtotal1+subtotal2+subtotal3+subtotal4

    table.insert('',index='end',text='Total',values=['','', total], tag=('totalcolor'))

    table.pack()
    detailWindow.mainloop()

def createNewWindow():
    #建立新視窗 New Windows
    newWindow = Toplevel(root)
    #建立新label在New Windows 裡
    # click the button to add 1 to the number
    def add(numlabel, pricelabel):
        global cost
        cost[0] = str(money.get())
    # numlabel的text+1
        numlabel["text"] = int(numlabel["text"])+1
        price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
        total = int(totalval.get().split(":")[1].replace("元","").strip())
        money = total+price
        totalval.set("共消費: "+str(total+price)+" 元")
        # click the button to minus 1 to the number
        
    def minus(numlabel, pricelabel):
    # 當numlabel大於0時，才會進行減1
        if int(numlabel["text"])>0:
        # numlabel的text-1
            numlabel["text"] = int(numlabel["text"])-1
            price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
            total = int(totalval.get().split(":")[1].replace("元","").strip())
            totalval.set("共消費: "+str(total-price)+" 元")
        # 當numlabel小於0時，跳出警告訊息框
        else:
            messagebox.showwarning("showwarning", "The number of products can\'t be below 0.")

    val = StringVar()
    # row=0
    titleimg = Image.open("project/img/d63d5f27d6e46a6918a26f36a5f31c0f.jpg")
    titleimg = titleimg.resize((32,32))
    titleimg = ImageTk.PhotoImage(titleimg)
    titlelabel = Label(newWindow, image=titleimg, width=32, height=32)
    titlelabel.grid(row=0, column=0, sticky=W)
    sofabtn1 = Button(newWindow, text="籃球", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2,command=soccor)
    sofabtn1.grid(row=0, column=1, sticky=E+W)
    bedding= Button(newWindow, text="足球", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
    bedding.grid(row=0, column=2, sticky=E+W)
    kitchen = Button(newWindow, text="跑步", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
    kitchen.grid(row=0, column=3, sticky=E+W)
    loginbutton = Button(newWindow, text="會員登入/註冊", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=12, pady=2,command=login)
    loginbutton.grid(row=0, column=7, sticky=E+W, padx=5)
    
    def soccor():
        soccor = Toplevel(root)
        soccor.title("足球鞋(Soccor)")
        soccor.geometry("880x650")


    #點擊登入/註冊button的時候跳出新視窗(輸入gmail)
    def login():
        #把gmail and password存在userInfo
        global userInfo
        def signUp():
            global userInfo
            userInfo[0]=str(gmail.get())
            userInfo[1]=str(password2.get())
            Login.destroy()
        Login = Toplevel(root)
        Login.title("註冊")
        Login.geometry("550x200")
        ask = Label(Login, text="Please enter your Gmail.")
        ask.pack()
        gmail = Entry(Login, width=30, font=("Georgia",16))
        gmail.pack()
        ask2 = Label(Login, text="Please enter your password.")
        ask2.pack()
        password2 = Entry(Login, width=30, font=("Georgia",16))
        password2.pack()
        enter = Button(Login, text="Enter", command=signUp)
        enter.pack()
        Login.mainloop()

    # row=1
    bannerimg = Image.open("project/img/image.webp")
    bannerimg = bannerimg.resize((852,298))
    bannerimg = ImageTk.PhotoImage(bannerimg)
    bannerlabel = Label(newWindow, image=bannerimg, width=852, height=298)
    bannerlabel.grid(row=1, column=0, sticky=W, columnspan=8)
    # row=2
    shoe1img = Image.open("project/img/2d484182-8596-4d88-aa63-3d594d010d4a.webp")
    shoe1img = shoe1img.resize((202,200))
    shoe1img = ImageTk.PhotoImage(shoe1img)
    shoe1label = Label(newWindow, image=shoe1img, width=202, height=200)
    shoe1label.grid(row=2, column=0, sticky=W, padx=5, columnspan=2)

    shoe2img = Image.open("project/img/5883a335-2363-480b-b3e1-9e083311c247.webp")
    shoe2img = shoe2img.resize((202,200))
    shoe2img = ImageTk.PhotoImage(shoe2img)
    shoe2label = Label(newWindow, image=shoe2img, width=202, height=200)
    shoe2label.grid(row=2, column=2, sticky=W, padx=5, columnspan=2)

    shoe3img = Image.open("project/img/1fdaff44-67e1-4513-a10a-e8e78696e354.webp")
    shoe3img = shoe3img.resize((202,200))
    shoe3img = ImageTk.PhotoImage(shoe3img)
    shoe3label = Label(newWindow, image=shoe3img, width=202, height=200)
    shoe3label.grid(row=2, column=4, sticky=W, padx=5, columnspan=2)

    shoe4img = Image.open("project/img/9f68d99d-756c-4691-af9a-f02eaca628f3.webp")
    shoe4img = shoe4img.resize((202,200))
    shoe4img = ImageTk.PhotoImage(shoe4img)
    shoe4label = Label(newWindow, image=shoe4img, width=202, height=200)
    shoe4label.grid(row=2, column=6, sticky=W, padx=5, columnspan=2)
    # row=3
    productname1 = Label(newWindow, text="PG 6 EP", font=("Inter", 11), fg="#000000")
    productname2 = Label(newWindow, text="KD Trey 5 X EP", font=("Inter", 11), fg="#000000")
    productname3 = Label(newWindow, text="Air Jordan XXXVII PF", font=("Inter", 11), fg="#000000")
    productname4 = Label(newWindow, text="Air Jordan XXXVII PF2", font=("Inter", 11), fg="#000000")

    productname1.grid(row=3, column=0, sticky=W, padx=5, columnspan=2)
    productname2.grid(row=3, column=2, sticky=W, padx=5, columnspan=2)
    productname3.grid(row=3, column=4, sticky=W, padx=5, columnspan=2)
    productname4.grid(row=3, column=6, sticky=W, padx=5, columnspan=2)
    # row=4
    productprice1 = Label(newWindow, text="NT.3,800", font=("Inter", 10), fg="#000000")
    productprice2 = Label(newWindow, text="NT.3,600", font=("Inter", 10), fg="#000000")
    productprice3 = Label(newWindow, text="NT.5,200", font=("Inter", 10), fg="#000000")
    productprice4 = Label(newWindow, text="NT.6,700", font=("Inter", 10), fg="#000000")

    productprice1.grid(row=4, column=0, sticky=W, padx=5)
    productprice2.grid(row=4, column=2, sticky=W, padx=5)
    productprice3.grid(row=4, column=4, sticky=W, padx=5)
    productprice4.grid(row=4, column=6, sticky=W, padx=5)

    addbutton1 = Button(newWindow, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber1, productprice1))
    addbutton1.grid(row=4, column=1, sticky=E)
    productnumber1 = Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="#000000")
    productnumber1.grid(row=4, column=1)
    minusbutton1 = Button(newWindow, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber1, productprice1))
    minusbutton1.grid(row=4, column=1, sticky=W)

    addbutton2 = Button(newWindow, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber2, productprice2))
    addbutton2.grid(row=4, column=3, sticky=E)
    productnumber2 = Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="#000000")
    productnumber2.grid(row=4, column=3)
    minusbutton2 = Button(newWindow, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber2, productprice2))
    minusbutton2.grid(row=4, column=3, sticky=W)

    addbutton3 = Button(newWindow, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber3, productprice3))
    addbutton3.grid(row=4, column=5, sticky=E)
    productnumber3 = Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="#000000")
    productnumber3.grid(row=4, column=5)
    minusbutton3 = Button(newWindow, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber3, productprice3))
    minusbutton3.grid(row=4, column=5, sticky=W)

    addbutton4 = Button(newWindow, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber4, productprice4))
    addbutton4.grid(row=4, column=7, sticky=E)
    productnumber4 = Label(newWindow, text="0", font=("Inter", 12, "bold"), fg="#000000")
    productnumber4.grid(row=4, column=7)
    minusbutton4 = Button(newWindow, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber4, productprice4))
    minusbutton4.grid(row=4, column=7, sticky=W)

    #row = 5
    newWindow.rowconfigure(5,weight=2)
    detaillistbutton = Button(newWindow, text="詳細清單", font=("Inter", 10), fg="#1E1E1E", bg="#ECEDE7")
    detaillistbutton.grid(row=5, column=0, sticky=W+S, padx=5, pady=1)

    shoppingimg = Image.open("project/img/Shopping Cart.png")
    shoppingimg = shoppingimg.resize((30,30))
    shoppingimg = ImageTk.PhotoImage(shoppingimg)
    shoppinglabel = Label(newWindow, image=shoppingimg, width=30, height=30)
    shoppinglabel.grid(row=5, column=5, sticky=E+S)

    totalval = StringVar()
    totalval.set("共消費: 0 元")
    totalvallabel = Label(newWindow, textvariable=totalval, font=("Inter", 18), fg="#000000")
    totalvallabel.grid(row=5, column=6, columnspan=2, sticky=W+S)

    newWindow.rowconfigure(5,weight=2)
    checkoutbutton = Button(newWindow, text="結帳", font=("Inter", 10), fg="#1E1E1E", bg="#ECEDE7")
    checkoutbutton.grid(row=5, column=7, sticky=E+S, padx=5, pady=1)
    newWindow.mainloop()

def paywindow():
    paywindow = Toplevel(root)
    paywindow.geometry('850x250')

    table = ttk.Treeview(paywindow, columns=['Subtotal', '', ''])
    table.heading('#0', text='')
    table.heading('#1', text='Subtotal')
    table.heading('#2', text='')
    table.heading('#3', text='')

    table.column('#0', width=250, anchor=CENTER)
    table.column('#1', anchor=CENTER)
    table.column('#2', anchor=CENTER)
    table.column('#3', anchor=CENTER)

    table.tag_configure('totalcolor', background='gray')


    subtotal1 = int(productnumber1["text"])*int(productprice1["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname1["text"], values=[productprice1["text"], productnumber1["text"],subtotal1])
    subtotal2 = int(productnumber2["text"])*int(productprice2["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname2["text"], values=[productprice2["text"], productnumber2["text"],subtotal2])
    subtotal3 = int(productnumber3["text"])*int(productprice3["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname3["text"], values=[productprice3["text"], productnumber3["text"],subtotal3])
    subtotal4 = int(productnumber4["text"])*int(productprice4["text"].split(".")[1].replace(",","").strip())
    table.insert("", index="end", text=productname4["text"], values=[productprice4["text"], productnumber4["text"],subtotal4])
    
    total = subtotal1+subtotal2+subtotal3+subtotal4
    table.insert('',index='end',text='Total',values=['','', total], tag=('totalcolor'))

    table.pack()

    Button1 = Button(text="繼續加購")
    Button1.pack()
    paywindow.mainloop()


# click the button to add 1 to the number
def add(numlabel, pricelabel):
    # numlabel的text+1
    numlabel["text"] = int(numlabel["text"])+1
    price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
    total = int(totalval.get().split(":")[1].replace("元","").strip())
    totalval.set("共消費: "+str(total+price)+" 元")
# click the button to minus 1 to the number
def minus(numlabel, pricelabel):
    # 當numlabel大於0時，才會進行減1
    if int(numlabel["text"])>0:
        # numlabel的text-1
        numlabel["text"] = int(numlabel["text"])-1
        price = int(pricelabel["text"].split(".")[1].replace(",","").strip())
        total = int(totalval.get().split(":")[1].replace("元","").strip())
        totalval.set("共消費: "+str(total-price)+" 元")
    # 當numlabel小於0時，跳出警告訊息框
    else:
        messagebox.showwarning("showwarning", "The number of products can\'t be below 0.")
    

val = StringVar()

#點擊登入/註冊button的時候跳出新視窗(輸入gmail)
def login():
    #把gmail and password存在userInfo
    global userInfo
    def signUp():
        global userInfo
        userInfo[0]=str(gmail.get())
        userInfo[1]=str(password2.get())
        Login.destroy()
    Login = Toplevel(root)
    Login.title("註冊")
    Login.geometry("550x200")
    ask = Label(Login, text="Please enter your Gmail.")
    ask.pack()
    gmail = Entry(Login, width=30, font=("Georgia",16))
    gmail.pack()
    ask2 = Label(Login, text="Please enter your password.")
    ask2.pack()
    password2 = Entry(Login, width=30, font=("Georgia",16))
    password2.pack()
    enter = Button(Login, text="Enter", command=signUp)
    enter.pack()
    Login.mainloop()


# row=0
titleimg = Image.open("project/img/d63d5f27d6e46a6918a26f36a5f31c0f.jpg")
titleimg = titleimg.resize((32,32))
titleimg = ImageTk.PhotoImage(titleimg)
titlelabel = Label(root, image=titleimg, width=32, height=32)
titlelabel.grid(row=0, column=0, sticky=W)
sofabtn1 = Button(root, text="籃球", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
sofabtn1.grid(row=0, column=1, sticky=E+W)
bedding= Button(root, text="足球", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2, command=lambda: createNewWindow())
bedding.grid(row=0, column=2, sticky=E+W)
kitchen = Button(root, text="跑步", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=5, pady=2)
kitchen.grid(row=0, column=3, sticky=E+W)
loginbutton = Button(root, text="會員登入/註冊", font=("Inter", 12), fg="#1E1E1E", bg="#ECE8E7", width=12, pady=2,command=login)
loginbutton.grid(row=0, column=7, sticky=E+W, padx=5)

# row=1
bannerimg = Image.open("project/img/image.webp")
bannerimg = bannerimg.resize((852,298))
bannerimg = ImageTk.PhotoImage(bannerimg)
bannerlabel = Label(root, image=bannerimg, width=852, height=298)
bannerlabel.grid(row=1, column=0, sticky=W, columnspan=8)
# row=2
shoe1img = Image.open("project/img/2d484182-8596-4d88-aa63-3d594d010d4a.webp")
shoe1img = shoe1img.resize((202,200))
shoe1img = ImageTk.PhotoImage(shoe1img)
shoe1label = Label(root, image=shoe1img, width=202, height=200)
shoe1label.grid(row=2, column=0, sticky=W, padx=5, columnspan=2)

shoe2img = Image.open("project/img/5883a335-2363-480b-b3e1-9e083311c247.webp")
shoe2img = shoe2img.resize((202,200))
shoe2img = ImageTk.PhotoImage(shoe2img)
shoe2label = Label(root, image=shoe2img, width=202, height=200)
shoe2label.grid(row=2, column=2, sticky=W, padx=5, columnspan=2)

shoe3img = Image.open("project/img/1fdaff44-67e1-4513-a10a-e8e78696e354.webp")
shoe3img = shoe3img.resize((202,200))
shoe3img = ImageTk.PhotoImage(shoe3img)
shoe3label = Label(root, image=shoe3img, width=202, height=200)
shoe3label.grid(row=2, column=4, sticky=W, padx=5, columnspan=2)

shoe4img = Image.open("project/img/9f68d99d-756c-4691-af9a-f02eaca628f3.webp")
shoe4img = shoe4img.resize((202,200))
shoe4img = ImageTk.PhotoImage(shoe4img)
shoe4label = Label(root, image=shoe4img, width=202, height=200)
shoe4label.grid(row=2, column=6, sticky=W, padx=5, columnspan=2)
# row=3
productname1 = Label(root, text="PG 6 EP", font=("Inter", 11), fg="#000000")
productname2 = Label(root, text="KD Trey 5 X EP", font=("Inter", 11), fg="#000000")
productname3 = Label(root, text="Air Jordan XXXVII PF", font=("Inter", 11), fg="#000000")
productname4 = Label(root, text="Air Jordan XXXVII PF2", font=("Inter", 11), fg="#000000")

productname1.grid(row=3, column=0, sticky=W, padx=5, columnspan=2)
productname2.grid(row=3, column=2, sticky=W, padx=5, columnspan=2)
productname3.grid(row=3, column=4, sticky=W, padx=5, columnspan=2)
productname4.grid(row=3, column=6, sticky=W, padx=5, columnspan=2)
# row=4
productprice1 = Label(root, text="NT.3,800", font=("Inter", 10), fg="#000000")
productprice2 = Label(root, text="NT.3,600", font=("Inter", 10), fg="#000000")
productprice3 = Label(root, text="NT.5,200", font=("Inter", 10), fg="#000000")
productprice4 = Label(root, text="NT.6,700", font=("Inter", 10), fg="#000000")

productprice1.grid(row=4, column=0, sticky=W, padx=5)
productprice2.grid(row=4, column=2, sticky=W, padx=5)
productprice3.grid(row=4, column=4, sticky=W, padx=5)
productprice4.grid(row=4, column=6, sticky=W, padx=5)

addbutton1 = Button(root, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber1, productprice1))
addbutton1.grid(row=4, column=1, sticky=E)
productnumber1 = Label(root, text="0", font=("Inter", 12, "bold"), fg="#000000")
productnumber1.grid(row=4, column=1)
minusbutton1 = Button(root, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber1, productprice1))
minusbutton1.grid(row=4, column=1, sticky=W)

addbutton2 = Button(root, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber2, productprice2))
addbutton2.grid(row=4, column=3, sticky=E)
productnumber2 = Label(root, text="0", font=("Inter", 12, "bold"), fg="#000000")
productnumber2.grid(row=4, column=3)
minusbutton2 = Button(root, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber2, productprice2))
minusbutton2.grid(row=4, column=3, sticky=W)

addbutton3 = Button(root, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber3, productprice3))
addbutton3.grid(row=4, column=5, sticky=E)
productnumber3 = Label(root, text="0", font=("Inter", 12, "bold"), fg="#000000")
productnumber3.grid(row=4, column=5)
minusbutton3 = Button(root, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber3, productprice3))
minusbutton3.grid(row=4, column=5, sticky=W)

addbutton4 = Button(root, text="+", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: add(productnumber4, productprice4))
addbutton4.grid(row=4, column=7, sticky=E)
productnumber4 = Label(root, text="0", font=("Inter", 12, "bold"), fg="#000000")
productnumber4.grid(row=4, column=7)
minusbutton4 = Button(root, text="-", font=("Inter", 10), fg="#1E1E1E", bg="#E7E2E2",command=lambda: minus(productnumber4, productprice4))
minusbutton4.grid(row=4, column=7, sticky=W)

#row = 5
root.rowconfigure(5,weight=2)
detaillistbutton = Button(root, text="詳細清單", font=("Inter", 10), fg="#1E1E1E", bg="#ECEDE7", command=showdetail)
detaillistbutton.grid(row=5, column=0, sticky=W+S, padx=5, pady=1)

shoppingimg = Image.open("project/img/Shopping Cart.png")
shoppingimg = shoppingimg.resize((30,30))
shoppingimg = ImageTk.PhotoImage(shoppingimg)
shoppinglabel = Label(root, image=shoppingimg, width=30, height=30)
shoppinglabel.grid(row=5, column=5, sticky=E+S)

totalval = StringVar()
totalval.set("共消費: 0 元")
totalvallabel = Label(root, textvariable=totalval, font=("Inter", 18), fg="#000000")
totalvallabel.grid(row=5, column=6, columnspan=2, sticky=W+S)

root.rowconfigure(5,weight=2)
checkoutbutton = Button(root, text="結帳", font=("Inter", 10), fg="#1E1E1E", bg="#ECEDE7")
checkoutbutton.grid(row=5, column=7, sticky=E+S, padx=5, pady=1)



smtp = smtplib.SMTP(host = "smtp.gmail.com", port="587")

text = MIMEText("您好，您剛剛已在Nike Shop 消費了"+str(cost[0])+"元。")

content = MIMEMultipart()

content["subject"] = "2023 Python APP 創新城市春季班 (Demo)"
# 寄件者
content["from"] = "jopu7011@gmail.com"
# 收件者
content["to"] = str(userInfo[0])

content.attach(text)

root.mainloop()