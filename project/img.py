# import tkinter as tk

# # 假设以下是您的电子邮件和密码列表
# users = {
#     "user1@example.com": "password1",
#     "user2@example.com": "password2",
#     "user3@example.com": "password3"
# }

# def login():
#     email = email_entry.get()
#     password = password_entry.get()

#     if email in users and password == users[email]:
#         print("Login successful!")
#         # 在此处添加您的付款和结账逻辑
#         # ...
#         login_window.destroy()
#     else:
#         print("Incorrect email or password")

# # 创建主窗口
# root = tk.Tk()
# root.title("Online Shopping")

# # 创建一个登录按钮，并在点击时打开登录窗口
# login_button = tk.Button(root, text="Login", command=lambda: login_window.deiconify())
# login_button.pack()

# # 创建登录窗口
# login_window = tk.Toplevel(root)
# login_window.title("Login")
# login_window.withdraw()  # 窗口默认隐藏，直到点击登录按钮后才会显示

# # 创建电子邮件和密码标签和输入框
# email_label = tk.Label(login_window, text="Email:")
# email_label.pack()
# email_entry = tk.Entry(login_window)
# email_entry.pack()

# password_label = tk.Label(login_window, text="Password:")
# password_label.pack()
# password_entry = tk.Entry(login_window, show="*")  # 将密码隐藏
# password_entry.pack()

# # 创建登录按钮并将其添加到登录窗口
# login_button = tk.Button(login_window, text="Login", command=login)
# login_button.pack()

# # 运行主循环
# root.mainloop()
