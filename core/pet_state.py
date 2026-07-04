from enum import Enum


class PetState(Enum):
    IDLE = "idle"
    WALKING = "walking"
    REMINDING = "reminding"
    HAPPY = "happy"