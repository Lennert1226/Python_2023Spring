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
ws.update_value("A1","國家")
ws.update_value("A2","美國")
ws.update_value("A3","日本")
ws.update_value("A4","香港")
ws.update_value("B1","匯率(以台灣為基準)")
ws.update_value("B2","0.0327")
ws.update_value("B3","4.4")
ws.update_value("B4","0.257")