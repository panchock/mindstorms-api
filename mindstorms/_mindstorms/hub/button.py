class Button:
    def wait_until_pressed(self) -> None: ...
    def wait_until_released(self) -> None: ...
    def was_pressed(self) -> None: ...
    def is_pressed(self) -> bool: ...
    def is_released(self) -> bool: ...
