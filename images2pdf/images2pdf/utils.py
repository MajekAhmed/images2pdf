"""
utils.py
دوال مساعدة مثل التحقق من أنواع الملفات، ترتيب الصور، إلخ.
"""


def validate_image_file(filename: str) -> bool:
    """التحقق من أن الملف صورة مدعومة."""
    return filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.heic'))

# يمكن إضافة دوال ترتيب أو معالجة إضافية هنا
