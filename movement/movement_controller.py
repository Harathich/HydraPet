from random import randint

from PySide6.QtCore import QObject, QTimer
from PySide6.QtGui import QGuiApplication

from utils.constants import PET_SPEED


class MovementController(QObject):
    def __init__(self, pet_window):
        super().__init__()

        self.pet_window = pet_window

        # Movement settings
        self.speed = PET_SPEED
        self.direction = 1
        self.is_moving = True

        # Timer for smooth movement (about 60 FPS)
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_pet)

        # Timer for changing behaviour
        self.behavior_timer = QTimer()
        self.behavior_timer.setSingleShot(True)
        self.behavior_timer.timeout.connect(self.toggle_behavior)

    def start(self):
        """Start movement and behaviour."""
        self.timer.start(16)
        self.schedule_next_behavior()

    def stop(self):
        """Stop all timers."""
        self.timer.stop()
        self.behavior_timer.stop()

    def move_pet(self):
        """Move the pet horizontally."""

        if not self.is_moving:
            return

        screen = QGuiApplication.primaryScreen()
        geometry = screen.availableGeometry()

        x = self.pet_window.x()
        y = self.pet_window.y()

        x += self.speed * self.direction

        margin = 20

        # Hit right edge
        if x + self.pet_window.width() >= geometry.right() - margin:
            x = geometry.right() - self.pet_window.width() - margin
            self.direction = -1

        # Hit left edge
        elif x <= geometry.left() + margin:
            x = geometry.left() + margin
            self.direction = 1

        self.pet_window.move(x, y)

    def toggle_behavior(self):
        """Switch between walking and standing."""

        self.is_moving = not self.is_moving

        if self.is_moving:
            print("🚶 Walking")
        else:
            print("😴 Idle")

        self.schedule_next_behavior()

    def schedule_next_behavior(self):
        """Choose how long to stay in the current behaviour."""

        if self.is_moving:
            # Walk between 3 and 7 seconds
            delay = randint(3000, 7000)
        else:
            # Idle between 2 and 5 seconds
            delay = randint(2000, 5000)

        self.behavior_timer.start(delay)