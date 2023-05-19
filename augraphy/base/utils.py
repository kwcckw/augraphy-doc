"""
This section stores all the options / methods in enum based class.

"""

class OverlayTypes(str, Enum):
    
    INK_TO_PAPER = "ink_to_paper"
    MIN = "min"
    MAX = "max"
    MIX = "mix"
    NORMAL = "normal"
    LIGHTEN = "lighten"
    DARKEN = "darken"
    ADDITION = "addition"
    SUBTRACT = "subtract"
    DIFFERENCE = "difference"
    SCREEN = "screen"
    DODGE = "dodge"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    HARD_LIGHT = "hard_light"
    GRAIN_EXTRACT = "grain_extract"
    GRAIN_MERGE = "grain_merge"
    OVERLAY = "overlay"

    
    