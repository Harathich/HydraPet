from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

from utils.constants import PET_IMAGE


class PetSprite(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_pixmap = None

        self.load_sprite()

    def load_sprite(self):
        self.current_pixmap = QPixmap(str(PET_IMAGE))

        if self.current_pixmap.isNull():
            raise FileNotFoundError(
                f"Unable to load pet image: {PET_IMAGE}"
            )

        self.setPixmap(self.current_pixmap)

        # Resize label to image
        self.resize(self.current_pixmap.size())

    def sprite_size(self):
        return self.current_pixmap.size()