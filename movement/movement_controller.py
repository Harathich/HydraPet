from PySide6.QtCore import QObject, QTimer
from PySide6.QtGui import QGuiApplication
from utils.constants import PET_SPEED


class MovementController(QObject):
    def __init__(self, pet_window):
        super().__init__()

        self.pet_window = pet_window

        # pixels per update
        self.speed = PET_SPEED

        # moving right
        self.direction = 1

        self.timer = QTimer()

        self.timer.timeout.connect(self.move_pet)

    def start(self):
        self.timer.start(16)

    def stop(self):
        self.timer.stop()

    def move_pet(self):
        screen = QGuiApplication.primaryScreen()
        geometry = screen.availableGeometry()

        x = self.pet_window.x()
        y = self.pet_window.y()

        # Move horizontally
        x += self.speed * self.direction

        # Right edge
        if x + self.pet_window.width() >= geometry.right():
            self.direction = -1

        # Left edge
        elif x <= geometry.left():
            self.direction = 1

        self.pet_window.move(x, y)