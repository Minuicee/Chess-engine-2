from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QMainWindow, QApplication, QLabel, QGridLayout, QWidget, QVBoxLayout, QPushButton, QColorDialog, QSlider, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import sys

class window(QMainWindow):
    def __init__(self, board_size=1000, extra_space=200):
        super().__init__()
        self.init_gui()

    def init_gui(self):
        self.setGeometry(board_size + extra_space, board_size)
