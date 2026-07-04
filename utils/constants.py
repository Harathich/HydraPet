from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"

PET_IMAGE = ASSETS_DIR / "pet.png"

WINDOW_TITLE = "HydraPet"

DEFAULT_REMINDER_INTERVAL = 60

DEFAULT_SNOOZE_TIME = 10

DAILY_GOAL = 8