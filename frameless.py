import sys
from PyQt5.QtCore import Qt
from pyqt_frameless_window import FramelessMainWindow
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class Window(FramelessMainWindow):
    def __init__(self):
        super().__init__()
        self.setTitleBarVisible(False)
        self.initUI()

    def initUI(self):
        pixmap = QPixmap("C:\\Users\\user\\Pictures\\Screenshots\\Screenshot 2024-01-06 090350.png")
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        s = 300
        self.resize(s, s)

    def keyPressEvent(self, event):
        key = event.key()
        if key==16777216: print('Esc'); self.close() # Got [Esc] key

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
