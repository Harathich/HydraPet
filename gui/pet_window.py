from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QWidget

from gui.pet_sprite import PetSprite
from utils.constants import WINDOW_TITLE
from movement.movement_controller import MovementController


class PetWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setup_window()
        self.setup_pet()
        self.movement = MovementController(self)

    def setup_window(self):
        self.setWindowTitle(WINDOW_TITLE)

        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground
        )

    def setup_pet(self):
        self.pet_sprite = PetSprite(self)

        # Resize window to fit sprite
        self.resize(self.pet_sprite.sprite_size())

    def position_pet(self):
        screen = QGuiApplication.primaryScreen()

        geometry = screen.availableGeometry()

        margin = 20

        x = geometry.x() + geometry.width() - self.width() - margin
        y = geometry.y() + geometry.height() - self.height() - margin

        self.move(x, y)

    def showEvent(self, event):
        super().showEvent(event)

        self.position_pet()
        self.movement.start()