import requests
from bs4 import BeautifulSoup
import time

# 要爬取的股票代碼列表
stock = ["1101", "2330"]

for i in range(len(stock)):
    stockid = stock[i]
    # Yahoo股市網址包含股票編號
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 定位股價 HTML 標籤（涵蓋平盤、上漲、下跌三種樣式）
    price = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ]).getText()
    
    # 組裝推播訊息
    message = f"股票 {stockid} 即時股價為 {price}"
    
    token = "8719766312"  # 填入 Bot Token
    chat_id = "8294056085"  # 填入 Telegram Chat ID
    
    # 發送 Telegram 訊息 API
    send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(send_url)
    
    # 每次請求間隔 3 秒
    time.sleep(3)

