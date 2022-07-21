from .light_matrix import LightMatrix
from .status_light import StatusLight
from .button import Button


class MSHub:
    PORT_A = "A"
    PORT_B = "B"
    PORT_C = "C"
    PORT_D = "D"
    PORT_E = "E"
    PORT_F = "F"

    def __init__(self) -> None:
        self.left_button = Button()
        self.right_button = Button()
        self.status_light = StatusLight()
        self.light_matrix = LightMatrix()
