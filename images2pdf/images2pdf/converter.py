"""
converter.py
وظائف تحويل الصور إلى PDF، معالجة دفعات، دعم أنواع الصور، وضغط الصور.
"""
import os
from PIL import Image
from tqdm import tqdm
from typing import List, Optional

SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.webp', '.heic')

# دعم HEIC إذا توفر pillow-heif
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass


def is_supported_image(filename: str) -> bool:
    return filename.lower().endswith(SUPPORTED_FORMATS)


def load_images(image_paths: List[str], jpeg_quality: int = 85) -> List[Image.Image]:
    """
    تحميل الصور من المسارات، مع ضغط JPEG إذا لزم.
    """
    images = []
    for path in image_paths:
        img = Image.open(path)
        if img.format == 'JPEG' and jpeg_quality < 100:
            img = img.convert('RGB')
        images.append(img)
    return images


def images_to_pdf(image_paths: List[str], output_pdf: str, page_size: str = 'A4', orientation: str = 'portrait', margin: int = 10, scale_mode: str = 'fit', jpeg_quality: int = 85, batch_size: int = 20, ocr: bool = False) -> None:
    """
    تحويل مجموعة صور إلى ملف PDF واحد مع خيارات متقدمة.
    """
    pdf_images = []
    for i in tqdm(range(0, len(image_paths), batch_size), desc="Processing batches"):
        batch = image_paths[i:i+batch_size]
        imgs = load_images(batch, jpeg_quality)
        # TODO: تطبيق خيارات الحجم والاتجاه والهوامش والـ scale_mode
        pdf_images.extend(imgs)
    if pdf_images:
        pdf_images[0].save(output_pdf, save_all=True,
                           append_images=pdf_images[1:], quality=jpeg_quality)

    # دعم OCR (اختياري)
    if ocr:
        try:
            from pytesseract import image_to_pdf_or_hocr
            with open(output_pdf, 'wb') as f:
                for img in pdf_images:
                    pdf_bytes = image_to_pdf_or_hocr(img, extension='pdf')
                    f.write(pdf_bytes)
        except ImportError:
            print("pytesseract غير مثبت. يرجى تثبيته لتفعيل OCR.")
