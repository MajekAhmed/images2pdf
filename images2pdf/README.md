# images2pdf

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-Qt%20for%20Python-green?logo=qt)](https://wiki.qt.io/Qt_for_Python)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-MajekAhmed/images2pdf-blue?logo=github)](https://github.com/MajekAhmed/images2pdf)

> **برنامج احترافي لتحويل عدد غير محدود من الصور إلى ملف PDF واحد أو عدة ملفات PDF عبر واجهة رسومية حديثة أو سطر أوامر بسيط.**

---

## محتويات البرنامج

- **واجهة رسومية متقدمة:**

  - مبنية على PySide6 (Qt for Python)
  - تدعم السحب والإفلات للصور
  - معاينة مصغرات وترتيب الصور بالـ drag & drop
  - شريط تقدم أثناء التحويل
  - خيارات متقدمة: حجم الصفحة (A4, Letter)، الاتجاه، الهوامش، جودة الضغط، طريقة ملاءمة الصورة
  - دعم HEIC وWebP وPNG وJPEG
  - خيار تفعيل OCR لجعل PDF قابل للبحث

- **سطر أوامر (CLI):**

  - تحويل مجلد كامل من الصور إلى PDF بسهولة
  - دعم دفعات لتقليل استهلاك الذاكرة

- **إدارة الذاكرة:**

  - معالجة الصور على دفعات (batch) لعدد غير محدود من الصور

- **دعم OCR (اختياري):**
  - عبر pytesseract
  - تعليمات التثبيت بالأسفل

---

## المتطلبات

- Python >= 3.11
- PySide6
- Pillow
- tqdm
- (اختياري) pytesseract
- (اختياري) pillow-heif

---

## التثبيت

```bash
python -m venv .env
.\.env\Scripts\activate
pip install -r requirements.txt
```

### دعم HEIC:

```bash
pip install pillow-heif
```

### دعم OCR:

```bash
pip install pytesseract
```

#### تثبيت Tesseract (OCR):

- Windows: [تحميل](https://github.com/tesseract-ocr/tesseract)
- Linux: `sudo apt install tesseract-ocr`

---

## التشغيل

### الواجهة الرسومية:

```bash
python main.py
```

### سطر الأوامر:

```bash
python cli.py --input images_folder --output result.pdf
```

---

## البناء والتوزيع

لإنشاء ملف تنفيذي:

```bash
pyinstaller --onefile --windowed main.py --name images2pdf
```

---

---

## تواصل معي لتنفيذ مشاريع مشابهة!

أنا أعمل كـ **فريلانسر** ومتخصص في تطوير تطبيقات Python وواجهات المستخدم الاحترافية.

- 📧 Email: [owen.ar2002@gmail.com](mailto:owen.ar2002@gmail.com)
- 💼 LinkedIn: [ahmed-ragab-mohmed](https://www.linkedin.com/in/ahmed-ragab-mohmed/)
- 🐙 GitHub: [MajekAhmed](https://github.com/MajekAhmed)

> إذا أعجبك المشروع أو لديك فكرة مشابهة، لا تتردد في التواصل معي لتنفيذها باحترافية!
