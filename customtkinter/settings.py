import sys


class Settings:

    circle_font_is_ready = False
    preferred_drawing_method: str = None  # 'polygon_shapes', 'font_shapes', 'circle_shapes'
    radius_to_char_fine: dict = None  # set in self.init_font_character_mapping()
    cursor_manipulation_enabled = True
    deactivate_macos_window_header_manipulation = False
    deactivate_windows_window_header_manipulation = False
    deactivate_automatic_dpi_awareness = False

    @classmethod
    def init_font_character_mapping(cls):
        """ optimizations made for Windows 10, 11 only """

        radius_to_char_warped = {19: 'B', 18: 'B', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'B', 12: 'B', 11: 'B', 10: 'B',
                                 9: 'C', 8: 'D', 7: 'C', 6: 'E', 5: 'F', 4: 'G', 3: 'H', 2: 'H', 1: 'H', 0: 'A'}

        radius_to_char_fine_windows_10 = {19: 'A', 18: 'A', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'C', 12: 'C', 11: 'C', 10: 'C',
                                          9: 'D', 8: 'D', 7: 'D', 6: 'F', 5: 'D', 4: 'G', 3: 'G', 2: 'H', 1: 'H', 0: 'A'}

        radius_to_char_fine_windows_11 = {19: 'A', 18: 'A', 17: 'B', 16: 'B', 15: 'B', 14: 'B', 13: 'C', 12: 'C', 11: 'D', 10: 'D',
                                          9: 'E', 8: 'F', 7: 'C', 6: 'I', 5: 'E', 4: 'G', 3: 'P', 2: 'R', 1: 'R', 0: 'A'}

        if sys.platform.startswith("win"):
            if sys.getwindowsversion().build > 20000:  # Windows 11
                cls.radius_to_char_fine = radius_to_char_fine_windows_11
            else:  # < Windows 11
                cls.radius_to_char_fine = radius_to_char_fine_windows_10
        else:  # macOS and Linux
            cls.radius_to_char_fine = radius_to_char_fine_windows_10

    @classmethod
    def init_drawing_method(cls):
        """ possible: 'polygon_shapes', 'font_shapes', 'circle_shapes' """

        if sys.platform == "darwin":
            cls.preferred_drawing_method = "polygon_shapes"
        else:
            cls.preferred_drawing_method = "font_shapes"