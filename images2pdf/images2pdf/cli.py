"""
cli.py
سطر أوامر بسيط لتحويل مجلد صور إلى PDF.
"""
import argparse
import os
from .converter import images_to_pdf, is_supported_image


def main():
    parser = argparse.ArgumentParser(description="تحويل مجلد صور إلى PDF")
    parser.add_argument('--input', required=True, help='مسار مجلد الصور')
    parser.add_argument('--output', required=True, help='اسم ملف PDF الناتج')
    parser.add_argument('--ocr', action='store_true',
                        help='تفعيل OCR (اختياري)')
    parser.add_argument('--quality', type=int, default=85,
                        help='جودة JPEG (افتراضي 85)')
    args = parser.parse_args()

    image_paths = [os.path.join(args.input, f) for f in os.listdir(
        args.input) if is_supported_image(f)]
    if not image_paths:
        print("لا توجد صور مدعومة في المجلد.")
        return
    images_to_pdf(
        image_paths,
        args.output,
        jpeg_quality=args.quality,
        ocr=args.ocr
    )
    print(f"تم إنشاء الملف: {args.output}")


if __name__ == "__main__":
    main()
