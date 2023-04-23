# from twilio.rest import Client

# account_sid = 'ACb5db8f8b98b4e759f22081b95017c903'
# auth_token = '[AuthToken]'
# client = Client(account_sid, auth_token)

# # print("Please")
# message = client.messages.create(
#     from_='+15076903393',
#     body='test',
#     to='+886989931977'
# )

# print(message.sid)


# # # 大多數常用操作，只需要用到 Path 這個類別
# # from pathlib import Path
# # # 引數傳入你要指向的位置，此例指向桌面
# # p = Path("./Desktop")
# # # 若沒有傳入引數，預設指向開啟 Python 的位置
# # p = Path()
# # # resolve() 找出絕對路徑
# # p.resolve()

# # print(p.resolve())

#引進pygsheets套件
import pygsheets
#設定google cloud用戶:讓googlesheets知道你的身分
gc = pygsheets.authorize(service_file="C:/Users/SP513-52N/Documents/Python_2023Spring/class7/midyear-castle-384601-388944a49d76.json")
#連接試算表:讓google sheets知道要更改哪個試算表
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/1j7v2ilnUviSTjFHeiPEyOE_nnZMZvvcCbxMp_Sgn8I0/edit#gid=0")

#利用Index選取工作表
#ws = sht[0]
#利用名字選取工作表
ws = sht.worksheet_by_title("工作表1")
#更改表中內容
ws.update_value("A1","Name")
ws.update_value("B1","Age")
ws.update_value("A2","Amy")
ws.update_value("A3","Peter")
ws.update_value("B2","18")
ws.update_value("B3","15")


import pandas as pd
#讀取成df
# df = pd.DataFrame(ws.get_all_records())
# print(df)

# dataframe to worksheet
# ws.set_dataframe(df, "A1")     #從欄位A1開始存入

# value = ws.get_value("A1")
# print("A1's value: "+value)

# A1 = ws.cell("A1")
# print("A1's value: "+A1.value)

# #清除sheet內所植
# ws.clear()


import requests
#不帶條件
r = requests.get("https://www.google.com/")
#有帶條件
# payload = {"key1":"value1", "key2":"value2"}
# r = requests.get("google.com", params=payload)

# r = requests.post("googlecom", data = {"key":"value"})

#列出文字
print(r.text)
#列出編碼
print(r.encoding)
#列出HTTP狀態碼
print(r.status_code)
#列出HTTP Response Headers
print(r.headers)
#印出Header中的Content-Type
print(r.headers["Content-Type"])
#如果娶得的是json格式資料，requests有內建解析函式
print(r.json)

import requests

#以TWD為基準
url = "https://api.exchangerate-api.com/v4/latest/TWD"
res = requests.get(url)
data = res.json()
print("日幣對台幣的匯率為"+str(data["rates"]["JPY"]))