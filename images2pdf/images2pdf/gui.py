"""
gui.py
واجهة المستخدم الرسومية الاحترافية باستخدام PySide6.
"""
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel,
    QFileDialog, QListWidget, QListWidgetItem, QProgressBar, QComboBox, QSpinBox,
    QHBoxLayout, QCheckBox
)
from PySide6.QtGui import QPixmap, QIcon, QDragEnterEvent, QDropEvent
from PySide6.QtCore import Qt
import os
from .converter import images_to_pdf, is_supported_image


class ImageListWidget(QListWidget):
    """قائمة الصور مع دعم السحب والإفلات والترتيب."""

    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setDragDropMode(QListWidget.InternalMove)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if is_supported_image(path):
                item = QListWidgetItem(os.path.basename(path))
                item.setData(Qt.UserRole, path)
                pixmap = QPixmap(path).scaled(64, 64, Qt.KeepAspectRatio)
                item.setIcon(QIcon(pixmap))
                self.addItem(item)


class MainWindow(QMainWindow):
    """النافذة الرئيسية للواجهة الرسومية."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("images2pdf - تحويل الصور إلى PDF")
        self.setMinimumSize(800, 600)
        central = QWidget()
        layout = QVBoxLayout()
        self.image_list = ImageListWidget()
        layout.addWidget(QLabel("اسحب الصور هنا أو اخترها:"))
        layout.addWidget(self.image_list)
        btn_add = QPushButton("إضافة صور")
        btn_add.clicked.connect(self.add_images)
        layout.addWidget(btn_add)
        # خيارات التحويل
        options_layout = QHBoxLayout()
        self.page_size = QComboBox()
        self.page_size.addItems(["A4", "Letter"])
        options_layout.addWidget(QLabel("حجم الصفحة:"))
        options_layout.addWidget(self.page_size)
        self.orientation = QComboBox()
        self.orientation.addItems(["portrait", "landscape"])
        options_layout.addWidget(QLabel("الاتجاه:"))
        options_layout.addWidget(self.orientation)
        self.margin = QSpinBox()
        self.margin.setRange(0, 100)
        self.margin.setValue(10)
        options_layout.addWidget(QLabel("الهامش:"))
        options_layout.addWidget(self.margin)
        self.scale_mode = QComboBox()
        self.scale_mode.addItems(["fit", "center", "cover"])
        options_layout.addWidget(QLabel("طريقة ملاءمة الصورة:"))
        options_layout.addWidget(self.scale_mode)
        self.jpeg_quality = QSpinBox()
        self.jpeg_quality.setRange(10, 100)
        self.jpeg_quality.setValue(85)
        options_layout.addWidget(QLabel("جودة JPEG:"))
        options_layout.addWidget(self.jpeg_quality)
        self.ocr_checkbox = QCheckBox("تفعيل OCR (اختياري)")
        options_layout.addWidget(self.ocr_checkbox)
        layout.addLayout(options_layout)
        # زر التحويل
        btn_convert = QPushButton("تحويل إلى PDF")
        btn_convert.clicked.connect(self.convert_to_pdf)
        layout.addWidget(btn_convert)
        # شريط التقدم
        self.progress = QProgressBar()
        layout.addWidget(self.progress)
        central.setLayout(layout)
        self.setCentralWidget(central)

    def add_images(self):
        files, _ = QFileDialog.getOpenFileNames(
            self, "اختر الصور", "", "Images (*.jpg *.jpeg *.png *.webp *.heic)")
        for path in files:
            if is_supported_image(path):
                item = QListWidgetItem(os.path.basename(path))
                item.setData(Qt.UserRole, path)
                pixmap = QPixmap(path).scaled(64, 64, Qt.KeepAspectRatio)
                item.setIcon(QIcon(pixmap))
                self.image_list.addItem(item)

    def convert_to_pdf(self):
        image_paths = [self.image_list.item(i).data(
            Qt.UserRole) for i in range(self.image_list.count())]
        if not image_paths:
            return
        output_pdf, _ = QFileDialog.getSaveFileName(
            self, "حفظ PDF", "output.pdf", "PDF Files (*.pdf)")
        if not output_pdf:
            return
        self.progress.setValue(0)
        # خيارات التحويل
        images_to_pdf(
            image_paths,
            output_pdf,
            page_size=self.page_size.currentText(),
            orientation=self.orientation.currentText(),
            margin=self.margin.value(),
            scale_mode=self.scale_mode.currentText(),
            jpeg_quality=self.jpeg_quality.value(),
            ocr=self.ocr_checkbox.isChecked()
        )
        self.progress.setValue(100)
        self.statusBar().showMessage("تم التحويل بنجاح!")


# نقطة الدخول للواجهة
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
