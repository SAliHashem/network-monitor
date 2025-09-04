# 🕵️‍♂️ Network Monitor (Python + Microservices)

Network Monitor بسيط مكتوب بالبايثون، يراقب اتصالات الشبكة ويعرض:
- البرامج المفتوحة + الـ IP + البورت.
- موقع الـ IP (الدولة/المدينة).
- استهلاك الشبكة بالوقت الفعلي.
- Logs محفوظة للاسترجاع لاحقًا.

## ⚙️ المميزات
- Microservices Architecture (كل خدمة مستقلة).
- GUI بواجهة سهلة (PyQt5).
- GeoIP Lookup باستخدام MaxMind.
- SQLite لتخزين السجلات.

## 📦 التثبيت
```bash
git clone https://github.com/YOUR_USERNAME/network-monitor.git
cd network-monitor
pip install -r requirements.txt
```

## ▶️ التشغيل
```bash
python run.py
```
## 🖼️ صور من البرنامج
![Network Monitor Screenshot](images/screenshot.png)


## 🛠️ التقنيات المستخدمة
- Python 3.x
- psutil
- geoip2
- FastAPI (للتواصل بين الخدمات)
- PyQt5

## ✨ المساهمة
- Fork المشروع.
- اعمل تغييراتك.
- افتح Pull Request.
