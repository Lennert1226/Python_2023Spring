from twilio.rest import Client

account_sid = 'ACb5db8f8b98b4e759f22081b95017c903'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

# print("Please")
message = client.messages.create(
    from_='+15076903393',
    body='test',
    to='+886989931977'
)

print(message.sid)


# # 大多數常用操作，只需要用到 Path 這個類別
# from pathlib import Path
# # 引數傳入你要指向的位置，此例指向桌面
# p = Path("./Desktop")
# # 若沒有傳入引數，預設指向開啟 Python 的位置
# p = Path()
# # resolve() 找出絕對路徑
# p.resolve()

# print(p.resolve())