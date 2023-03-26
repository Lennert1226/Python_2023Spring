# 引入MIMEText物件
from email.mime.text import MIMEText
# 如果想要再電子郵件中加入圖片，則須在Python專案中引入用MIMEImage類別，並且引入pathlib涵是褲來讀取圖片
from email.mime.image import MIMEImage
from pathlib import Path
# 引入MIMEMultipart物件
from email.mime.multipart import MIMEMultipart

# Python專案中的墊子郵件內容完成後，接下來就要設定Gmail的SMTP伺服器來傳送
# 引入smtplib物件
import smtplib

# 建立smtplib物件(host:伺服器位置, port: 連接埠號)
smtp = smtplib.SMTP(host = "smtp.gmail.com", port="587")

# 建立MIMEText物件
text = MIMEText("Demo-我是一封由python程式碼建立的信封信件!")

# 用read_bytes是為了以bytes的形式讀取圖片內容
image = MIMEImage(Path("C:/Users/SP513-52N/Documents/Python_2023Spring/class1/unnamed.png").read_bytes())

# 建立MIMEMuiltiple物件
content = MIMEMultipart()
# 郵件標題
content["subject"] = "2023 Python APP 創新城市春季班 (Demo)"
# 寄件者
content["from"] = "lennertyen1226@gmail.com"
# 收件者
content["to"] = "Vicky7011@yahoo.com.tw"

# 郵件內容使用MIMEMultipart物件的attach方法(Method)進行設定
# 郵件內容
content.attach(text)
# 郵件圖片內容
content.attach(image)


# 利用read模式打開password.txt並將檔案存放在f變數中
# 利用 with 來自動釋放資源
with open("class5\password.txt", "r") as f:
    mailToken = f.read()

# 利用with來自動釋放資源
with smtp:
    try:
        # 驗證SMTP伺服器
        smtp.ehlo()
        # 建立加密傳輸
        smtp.starttls()
        smtp.login("lennertyen1226@gmail.com", mailToken)
        # 寄送郵件
        smtp.send_message(content)
        print("Email is Sended completely!")
        smtp.quit()
    except Exception as e:
        print("Error message: ", e)