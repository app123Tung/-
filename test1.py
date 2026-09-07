import requests
from bs4 import BeautifulSoup
import time

# 要爬取的股票代碼列表
stock = ["1101", "2330"]

# 模擬一般瀏覽器 Header，防止被 Yahoo 伺服器阻擋
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for stockid in stock:
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"
    
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # 定位股價 HTML 標籤
    price_tag = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ])
    
    if price_tag:
        price = price_tag.getText()
        message = f"股票 {stockid} 即時股價為 {price}"
        
        token = "8719766312"
        chat_id = "8294056085"
        
        send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(send_url)
    else:
        print(f"無法取得 {stockid} 股價資訊")
    
    time.sleep(3)

