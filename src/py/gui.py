from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
import engine

class window(QMainWindow):

    def __init__(self, board_size, extra_space):
        super().__init__()
        print(engine.hello())

        # init variables
        self.board_size = board_size
        self.extra_space = extra_space

        # init gui
        self.init_gui()
        self.center()

    def init_gui(self):
        # init images
        square_size = QSize(self.board_size // 8, self.board_size//8)

        self.piece_images = [QPixmap('./images/pw.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/nw.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/bw.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/rw.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/qw.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/kw.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/pb.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/nb.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/bb.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/rb.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/qb.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation),
                             QPixmap('./images/kb.png').scaled(square_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                             ]

        # set frame variables
        self.setFixedSize(self.board_size + self.extra_space, self.board_size + 25)
        self.mainLayout = QHBoxLayout()

        # grid for the squares
        self.square_grid = QWidget()
        self.grid_layout = QGridLayout()
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setHorizontalSpacing(0)
        self.square_grid.setLayout(self.grid_layout)
        self.square_grid.setFixedSize(self.board_size, self.board_size)

        # init squares
        for i in range(8):
            for j in range(8):

                # do this to every square
                square = QPushButton()
                square.setFixedSize(square_size)
                color_index = (i+j)%2
                icon = QIcon(square.setStyleSheet("background-color: #2b85c4") if color_index % 2 == 0 else square.setStyleSheet("background-color: #757575"))
                square.setIcon(icon)
                square.setIconSize(square_size)
                self.grid_layout.addWidget(square, i, j)

        # extra space for labels for debugging
        self.extra_widget = QWidget()
        self.extra_widget_layout = QVBoxLayout()
        self.extra_widget.setLayout(self.extra_widget_layout)
        self.extra_widget.setFixedSize(self.extra_space, self.board_size)

        # add widgets to window
        self.mainLayout.addWidget(self.square_grid)
        self.mainLayout.addWidget(self.extra_widget)
        central = QWidget()
        central.setLayout(self.mainLayout)
        self.setCentralWidget(central)

    def draw_board(self, pieces):
        # draw board (expected 12*uint64)
        for i in range(8):
            for j in range(8):
                position = 1 << i*8+j
                for piece in range(12):
                    if (pieces[piece] & position)!=0:
                        button = self.grid_layout.itemAtPosition(i, j).widget()
                        if isinstance(button, QPushButton):
                            button.setIcon(QIcon(self.piece_images[piece]))
                            button.setIconSize(QSize(self.board_size // 8, self.board_size // 8))

    def request_legalMoves(self, idx):
        pass


    def center(self):
        # put the frame in the middle
        screen = self.screen().availableGeometry()
        frame = self.frameGeometry()
        frame.moveCenter(screen.center())
        self.move(frame.topLeft())
