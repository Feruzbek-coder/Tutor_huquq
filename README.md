# Tutor_huquq

Flask-based learning app prepared for deployment to Render.

Deploy instructions:

1. Link this GitHub repo to Render (https://render.com).
2. Create a new Web Service, select the repo and branch `main`.
3. Use the default build command and start command from `Procfile`.
# 📚 INGLIZ TILI O'RGANISH - LOCAL WEB ILOVA

## 🎯 LOYAHANING MAQSADI

Bu ilova xonadagi 6 ta kompyuterda ishlaydi va WiFi orqali bitta server kompyuterga ulanadi. 
**Offline rejimida to'liq ishlaydi** - internetni o'chirib qo'yish mumkin!

---

## 🚀 TEZKOR BOSHLASH

### 1️⃣ **SETUP (Birinchi Marta)**

```bash
# Python paketlarini o'rnatish
pip install -r requirements.txt
```

### 2️⃣ **SERVERNI ISHGA TUSHURISH**

```bash
# Bitta kompyuterda (SERVER):
python app.py
```

Natija: `Running on http://0.0.0.0:5000`

### 3️⃣ **BOSHQA KOMPYUTERLARGA ULANISH**

Bosh kompyuterning IP adresini topish:
```bash
# Windows:
ipconfig

# Qidiriladi: IPv4 Address (masalan: 192.168.1.5)
```

**Har bir klient kompyuterning brauzerida yozing:**
```
http://192.168.1.5:5000
```

---

## 📁 FAYL STRUKTURA

```
Tutor_assistant/
├── app.py                      # Flask backend (asosiy fayl)
├── requirements.txt            # Python paketlari
├── README.md                   # Bu fayl
│
├── data/                       # JSON ma'lumotlar
│   ├── questions.json          # Savollar
│   └── users.json              # Foydalanuvchi statistikasi
│
├── templates/                  # HTML sahifalar
│   ├── index.html              # Login sahifasi
│   ├── menu.html               # Bosh menyu
│   ├── vocabulary.html         # So'zlar bo'limi
│   ├── grammar.html            # Grammatika bo'limi
│   ├── practice.html           # Mashq rejimi
│   ├── test.html               # Test rejimi (20 savol)
│   ├── statistics.html         # Statistika
│   └── error.html              # Xato sahifasi
│
└── static/                     # Statik fayllar
    ├── css/
    │   └── style.css           # Asosiy CSS styling
    ├── js/                     # (Kengaytirish uchun tayyor)
    └── images/                 # (Kengaytirish uchun tayyor)
```

---

## 📚 FUNKSIYALAR VA JOYLAR

### **1. VOCABULARY (📖 So'zlar)**
- **Joylar:** `templates/vocabulary.html`
- **Ma'lumot:** `data/questions.json` (type: "vocabulary")
- **Xususiyatlari:**
  - Rasm, so'z, talaffuzi, tarjimasi, misol
  - Bosma-boss so'zni o'rganish

### **2. GRAMMAR (✏️ Grammatika)**
- **Joylar:** `templates/grammar.html`
- **Holati:** Tayorlash jarayonida (hozir placeholder)
- **Keyinchalik:** Qoidalar + misollar + mashqlar

### **3. PRACTICE (🎯 Mashq)**
- **Joylar:** `templates/practice.html`
- **Savollar:** Multiple choice + Fill in blanks
- **Xususiyatlari:**
  - Cheksiz random savollar
  - Har bir javobga tushuntirish
  - Ball avtomatik saqlanadi

### **4. TEST (🏆 Test Rejimi)**
- **Joylar:** `templates/test.html`
- **Tashkili:** 20 ta random savol
- **Natija:** 
  - Ballni ko'rsatish
  - Foizni hisoblash
  - Maslahat berish (90%+ = A'lo, 70%+ = Yaxshi, va h.k.)

### **5. STATISTIKA (📊 Progress)**
- **Joylar:** `templates/statistics.html`
- **Ko'rsatiladi:**
  - Jami savollarga javob
  - To'g'ri javoblar
  - Aniqlik foizi
  - Ro'yxatdan o'tgan sana

---

## 🔧 KOD STRUKTURASI

### **Backend (Flask - app.py)**

```
HELPER FUNCTIONS (Data Management)
├── load_json()           # JSON o'qish
├── save_json()           # JSON saqlash
├── get_user()            # Foydalanuvchi ma'lumoti
├── create_user()         # Yangi foydalanuvchi
└── update_user_score()   # Ball yangilash

ROUTES (Sahifalar)
├── / (index)             # Login
├── /menu                 # Bosh menyu
├── /vocabulary           # So'zlar
├── /grammar              # Grammatika
├── /practice             # Mashq
├── /test                 # Test
└── /statistics           # Statistika

API ENDPOINTS (Data Backend)
├── /api/user/create              # Yangi foydalanuvchi
├── /api/user/<username>          # Foydalanuvchi ma'lumoti
├── /api/questions                # Barcha savollar
└── /api/check-answer             # Javobni tekshirish
```

### **Frontend (HTML + JavaScript)**

**Komunikatsiya:**
- fetch() API ishlatiladi (modern JavaScript)
- JSON format
- Backend bilan o'zaro aloqa

---

## 📊 JSON DATA FORMATI

### **questions.json**

```json
{
  "questions": [
    {
      "id": 1,
      "type": "vocabulary",
      "word": "Hello",
      "pronunciation": "hə'ləʊ",
      "translation": "Salom",
      "example": "Hello, my name is John."
    },
    {
      "id": 4,
      "type": "multiple_choice",
      "question": "What is...?",
      "options": ["option1", "option2"],
      "correct_answer": "0",
      "explanation": "Tushuntirish..."
    }
  ]
}
```

### **users.json**

```json
{
  "username": {
    "name": "username",
    "score": 10,
    "total_questions": 25,
    "created_at": "2026-04-23T10:00:00",
    "results": [
      {
        "question_id": 1,
        "is_correct": true,
        "timestamp": "2026-04-23T10:05:00"
      }
    ]
  }
}
```

---

## 🌐 OFFLINE REJIMI

**Qanday ishlaydi?**
- Barcha ma'lumotlar JSON faylda saqlangan
- Brauzer kesh xotirasidan foydalanadi
- Internet bo'lmaganda ham to'liq ishlaydi

**Kengaytirish (Internet qo'shish):**
- Backend-ni database bilan almashtiring (MySQL, PostgreSQL)
- API endpoints o'zgarmas qoladi
- Frontend kodi o'zgarmas qoladi

---

## 🎨 RANGLAR VA DESIGN

**Tema:**
- Asosiy (Ko'k): `#2196F3`
- To'g'ri (Yashil): `#4CAF50`
- Noto'g'ri (Qizil): `#F44336`
- Warning (Sariq): `#FF9800`

**Layout:**
- Responsive (mobil, planshet, kompyuter)
- Katta tugmalar
- Tushunarli interfeys

---

## 🚀 KENGAYTIRISH IMKONIYATLARI

### Qo'shish Mumkin:
1. ✏️ **Grammar bo'limini yaratish**
   - Qoidalar + misollar
   - Harakat-harakatsiz test

2. 📷 **Rasmlar qo'shish**
   - `/static/images/` papkasiga qo'ying
   - `questions.json`-da joylashtiring

3. 🔊 **Audio qo'shish**
   - Talaffuzni tinglash (Web Audio API)

4. 👥 **Multi-user leaderboard**
   - Hammaning statistikasini ko'rish

5. 💾 **Database qo'shish**
   - Flask-SQLAlchemy orqali

6. 🎮 **Gamification**
   - Badges (medali)
   - Streaks (ketma-ket kunlar)

---

## 🐛 MUMKIN BO'LGI XatOLAR VA HAL QILISH

| XatO | SABAB | HAL QILISH |
|------|-------|-----------|
| **Connection refused** | Server ishlamagani | `python app.py` ni qayta ishga tushiring |
| **404 Not Found** | Noto'g'ri URL | IP va port tekshiring (192.168.x.x:5000) |
| **JSON error** | questions.json xato | JSON validity checker orqali tekshiring |
| **CORS error** | (keyin uchun) | Allow-Origin headers qo'shing |

---

## 💡 MASLAHATLAR

✅ **Do:**
- Qo'shimcha so'zlar qo'shing `questions.json`-ga
- Foydalanuvchi bahosi bilan o'ynang
- Interfeysi yaxsilang (ranglar, animatsiyalar)

❌ **Don't:**
- JSON strukturasini o'zgartirmang (API buziladi)
- Template file nomlarini o'zgartirmang
- app.py-ni o'chirib qo'ymang

---

## 👨‍💻 ARXITEKTURA DIAGRAMMA

```
CLIENT SIDE          NETWORK           SERVER SIDE
    Browser  -----> WiFi (5000) <----- Flask App
    (HTML)          (192.168.x)         |
    (CSS)                               ├── HTML Render
    (JS)                                ├── API Endpoints
                                        ├── JSON Files
                                        └── User Stats
```

---

## 📞 QANDAY ISHLAYDI?

1. **Startup:** `python app.py` 
2. **Client:** Brauzer orqali `192.168.1.5:5000` kirish
3. **Login:** Foydalanuvchi nomi kiritish
4. **Menu:** Bo'limlardan tanlash
5. **Learning:** Savollarni yechish
6. **Save:** Statistika avtomatik saqlanadi
7. **Logout:** Chiqish va qayta kirish mumkin

---

## 🎓 O'QUV JARAYONI

```
[Login] 
   ↓
[Menu] 
   ├─→ [Vocabulary] → Tekkoslash → Ball +
   ├─→ [Practice] → Random Q → Feedback → Ball +
   ├─→ [Test] → 20Q → Natija → Ball +
   ├─→ [Grammar] → (Keyinchalik)
   └─→ [Statistics] → Progress Ko'rish
```

---

## 📈 STATISTIKA SAQLASH

**Har bir javobdan keyin:**
```javascript
/api/check-answer:
  - question_id
  - is_correct (true/false)
  - timestamp
  ↓
users.json-ga saqlash
  ↓
Statistics sahifasida ko'rish
```

---

## ✅ KONTROL RO'YXATI

- [x] Flask server ishlamoqda
- [x] Login sahifasi ishlamoqda
- [x] Menu sahifasi ishlamoqda
- [x] Vocabulary bo'limi ishlamoqda
- [x] Practice bo'limi ishlamoqda
- [x] Test bo'limi (20Q) ishlamoqda
- [x] Statistics bo'limi ishlamoqda
- [x] JSON data saqlash ishlamoqda
- [x] Offline mode ishlamoqda
- [ ] Grammar bo'limini yaratish (qo'shimcha)
- [ ] Rasmlar qo'shish (qo'shimcha)

---

## 📝 LITSENZIYA

Bu loyaha taʼlim maqsadida yaratilgan. 
Erkin o'zgartirib, kengaytirib, tarqatsangiz bo'ladi.

---

**Muvaffaqiyatlar! 🎉 Siz tayyorsiz!**

Savollar bo'lsa - app.py-ga kommentlar yozing yoki kodni o'qing.
Kod tushunarli va oson o'zgartiriladi.
