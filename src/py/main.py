from PyQt5.QtWidgets import QApplication
import sys
import gui

class main():

    def __init__(self, board_size=800, extra_space=200):
        # init the frame
        app = QApplication(sys.argv)
        window = gui.window(board_size, extra_space)
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    game = main() 

