import requests
import time

TOKEN = "8733318399:AAEZs2dbrL9OscRvTOJxSIFZMOGRdb0BgZw"
CHAT_ID = "6081760514"

URL = "https://visa.vfsglobal.com/egy/en/nld/application-detail"

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "HTML"
    })

print("Hal towgad mwa3ed VFS")

while True:
    try:
        r = requests.get(URL, timeout=20)
        page = r.text.lower()

        if "book appointment – tourist visa" in page:
            send("🚨 مواعيد فيزا السياحة لهولندا ظهرت الآن!")
            print("towgad mwa3ed")
            break
        else:
            print("la towgad mwa3ed")

    except:
        print("مشكلة اتصال")

    time.sleep(120)