from .status_light import _StatusLight
from .button import _Button


class MSHub():
    PORT_A = "A"
    PORT_B = "B"
    PORT_C = "C"
    PORT_D = "D"
    PORT_E = "E"
    PORT_F = "F"

    def __init__(self) -> None:
        self.left_button = _Button()
        self.right_button = _Button()
        self.status_light = _StatusLight()
