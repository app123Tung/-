print("=== 程式開始執行 ===", flush=True)

import requests
from bs4 import BeautifulSoup
import time

stock = ["1101", "2330"]
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

token = "8719766312:AAH8j6gNEK1vmVnL4Yeo-W0Q7LDzUsldClg"
chat_id = "8294056085"

for stockid in stock:
    print(f"開始抓取 {stockid}...", flush=True)
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW"
    
    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, 'html.parser')
        
        price_tag = soup.find('span', class_=[
            "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
            "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
            "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
        ])
        
        if price_tag:
            price = price_tag.getText()
            message = f"股票 {stockid} 即時股價為 {price}"
            send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
            res = requests.get(send_url, timeout=10)
            print(f"[{stockid}] Telegram 回傳結果：{res.text}", flush=True)
        else:
            print(f"[{stockid}] 失敗：無法抓到 HTML 標籤！", flush=True)
            
    except Exception as e:
        print(f"[{stockid}] 連線失敗或出錯：{e}", flush=True)
    
    time.sleep(3)

print("=== 程式執行完畢 ===", flush=True)

