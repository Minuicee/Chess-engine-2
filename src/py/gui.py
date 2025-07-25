from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QHBoxLayout
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

SQUARE_IMAGES = ['../../images/square_w.png', '../../images/square_b.png']

class window(QMainWindow):

    def __init__(self, board_size, extra_space):
        super().__init__()

        # init variables
        self.board_size = board_size
        self.extra_space = extra_space
        self.squares = []

        # init gui 
        self.init_gui()

    def init_gui(self):
        # set frame variables
        self.setFixedSize(self.board_size + self.extra_space, self.board_size)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        # grid for the squares
        self.square_grid = QWidget()
        self.grid_layout = QGridLayout()
        self.square_grid.setLayout(self.grid_layout)

        # init squares
        for i in range(8):
            for j in range(8):

                # do this to every square
                square = QPushButton()
                position = ((i+1)+j*8) 
                square.setStyleSheet(f"background-image: url('{SQUARE_IMAGES[0] if position % 2 == 0 else SQUARE_IMAGES[1]}');")
                self.squares.append(square)
                self.grid_layout.addWidget(square, i, j)


        # add widgets to window
        self.layout.addWidget(self.square_grid)
