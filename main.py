import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from py_toggle import PyToggle

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(500, 500)

        self.container = QFrame()
        self.container.setObjectName("container")
        self.container.setStyleSheet("#container { background-color: #222}")
        self.layout = QVBoxLayout()

        self.toggle = PyToggle()
        self.toggle.setStyleSheet("color: #DC143C; font: 700 9pt 'Sergoe UI'")
        self.toggle.setText('123456789123456789')

        self.layout.addWidget(self.toggle, Qt.AlignCenter, Qt.AlignCenter)

        # SET CENTRAL WIDGET
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())