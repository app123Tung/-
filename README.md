import requests  # 請求工具[span_10](start_span)[span_10](end_span)
from bs4 import BeautifulSoup  # 解析工具[span_11](start_span)[span_11](end_span)
import time  # 用來暫停程式[span_12](start_span)[span_12](end_span)

# 要爬取的股票代碼列表[span_13](start_span)[span_13](end_span)
stock = ["1101", "2330"][span_14](start_span)[span_14](end_span)

for i in range(len(stock)):[span_15](start_span)[span_15](end_span)
    stockid = stock[i][span_16](start_span)[span_16](end_span)
    # Yahoo股市網址包含股票編號[span_17](start_span)[span_17](end_span)
    url = f"https://tw.stock.yahoo.com/quote/{stockid}.TW[span_18](start_span)"[span_18](end_span)
    
    r = requests.get(url)[span_19](start_span)[span_19](end_span)
    soup = BeautifulSoup(r.text, 'html.parser')[span_20](start_span)[span_20](end_span)
    
    # 定位股價 HTML 標籤（涵蓋平盤、上漲、下跌三種樣式）[span_21](start_span)[span_21](end_span)
    price = soup.find('span', class_=[
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
        "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"
    ]).getText()[span_22](start_span)[span_22](end_span)
    
    # 組裝推播訊息[span_23](start_span)[span_23](end_span)
    message = f"股票 {stockid} 即時股價為 {price}[span_24](start_span)"[span_24](end_span)
    
    token = "8719766312"  # 填入 BotFather 給的 Token[span_25](start_span)[span_25](end_span)
    chat_id = "8294056085"  # 填入 userinfobot 查到的 ID[span_26](start_span)[span_26](end_span)
    
    # 發送 Telegram 訊息 API[span_27](start_span)[span_27](end_span)
    send_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}[span_28](start_span)"[span_28](end_span)
    requests.get(send_url)[span_29](start_span)[span_29](end_span)
    
    # 每次請求間隔 3 秒[span_30](start_span)[span_30](end_span)
    time.sleep(3)[span_31](start_span)[span_31](end_span)

