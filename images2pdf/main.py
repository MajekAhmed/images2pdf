"""
main.py
نقطة الدخول لتشغيل الواجهة الرسومية.
"""
from images2pdf.gui import MainWindow
import sys
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
