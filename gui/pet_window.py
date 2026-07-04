from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget


class PetWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("HydraPet")

        self.resize(150, 150)



        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)