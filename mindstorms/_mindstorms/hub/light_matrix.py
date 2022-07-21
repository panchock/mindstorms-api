class LightMatrix:
    def set_pixel(self, x: int, y: int, brightness: int = 100) -> None:
        """
        Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.

        Args:
            x [0 - 4]: Pixel position of the Light Matrix 5 columns, counting from the left.
            y [0 - 4]: Pixel position of the Light Matrix 5 rows, counting from the top.
            brightness [0 - 100]: Brightness of the specified pixel in percent
        """
        ...
