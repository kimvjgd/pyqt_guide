import sys
from PyQt5.QtCore import Qt, QBasicTimer, QTime, QDate, QDateTime, QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QMenu, QCheckBox, QLabel, QPushButton, QToolTip, \
    QHBoxLayout, QVBoxLayout, QRadioButton, QLineEdit, QComboBox, QProgressBar, QSlider, QDial, QSplitter, QGroupBox, \
        QSpinBox, QDoubleSpinBox, QTabWidget, QTimeEdit, QDateTimeEdit, QDateEdit, QCalendarWidget, QTextEdit, QTextBrowser, \
        QTableWidget, QInputDialog, QMessageBox, QFontDialog, QColorDialog, QFrame, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap, QFont, QColor
import urllib.request
import json
import requests
from pathlib import Path

class _________(QWidget):
    def __init__(self):
        super().__init__()
        self.UI초기화()
    
    def UI초기화(self):


        self.setWindowTitle('__________')
        self.setGeometry(x, y, w, h)
        self.show()
    
    


프로그램무한반복 = QApplication(sys.argv)
실행인스턴스 = _________()
프로그램무한반복.exec_()