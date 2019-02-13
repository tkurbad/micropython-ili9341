# Avaliable fonts:
# Arrows_15
# Arrows_23
# Vera_10
# Vera_m10
# Arial_14
# Vera_15
# Vera_m15
# VeraMono_15
# VeraMono_m15
# Pitch_m15
# Pitch_m23
# VeraMono_m23
# Heydings_23
# Entypo_13
# Entypo_23

__all__ = []

def importing(font):
    if font == 'Arrows_15':
        try:
            from ili9341.fonts.arrows_15 import Arrows_15 as font
        except ImportError:
            from fonts.arrows_15 import Arrows_15 as font
    elif font == 'Arrows_23':
        try:
            from ili9341.fonts.arrows_23 import Arrows_23 as font
        except ImportError:
            from fonts.arrows_23 import Arrows_23 as font
    elif font == 'Vera_10':
        try:
            from ili9341.fonts.vera_10 import Vera_10 as font
        except ImportError:
            from fonts.vera_10 import Vera_10 as font
    elif font == 'Vera_m10': # Minimal Charset
        try:
            from ili9341.fonts.vera_m10 import Vera_m10 as font
        except ImportError:
            from fonts.vera_m10 import Vera_m10 as font
    elif font == 'Arial_14':
        try:
            from ili9341.fonts.arial_14 import Arial_14 as font
        except ImportError:
            from fonts.arial_14 import Arial_14 as font
    elif font == 'Vera_15':
        try:
            from ili9341.fonts.vera_15 import Vera_15 as font
        except ImportError:
            from fonts.vera_15 import Vera_15 as font
    elif font == 'Vera_m15':
        try:
            from ili9341.fonts.vera_m15 import Vera_m15 as font
        except ImportError:
            from fonts.vera_m15 import Vera_m15 as font
    elif font == 'VeraMono_15':
        try:
            from ili9341.fonts.veram_15 import VeraMono_15 as font
        except ImportError:
            from fonts.veram_15 import VeraMono_15 as font
    elif font == 'VeraMono_m15':
        try:
            from ili9341.fonts.veram_m15 import VeraMono_m15 as font
        except ImportError:
            from fonts.veram_m15 import VeraMono_m15 as font
    elif font == 'Pitch_m15':
        try:
            from ili9341.fonts.pitch_15 import Pitch_m15 as font
        except ImportError:
            from fonts.pitch_15 import Pitch_m15 as font
    elif font == 'Pitch_m23':
        try:
            from ili9341.fonts.pitch_23 import Pitch_m23 as font
        except ImportError:
            from fonts.pitch_23 import Pitch_m23 as font
    elif font == 'VeraMono_m23':
        try:
            from ili9341.fonts.veram_m23 import VeraMono_m23 as font
        except ImportError:
            from fonts.veram_m23 import VeraMono_m23 as font
    elif font == 'Heydings_23':
        try:
            from ili9341.fonts.heyd_23 import Heydings_23 as font
        except ImportError:
            from fonts.heyd_23 import Heydings_23 as font
    elif font == 'Entypo_13':
        try:
            from ili9341.fonts.etypo_13 import Entypo_13 as font
        except ImportError:
            from fonts.etypo_13 import Entypo_13 as font
    elif font == 'Entypo_23':
        try:
            from ili9341.fonts.etypo_23 import Entypo_23 as font
        except ImportError:
            from fonts.etypo_23 import Entypo_23 as font
    else:
        font = None
    return font
