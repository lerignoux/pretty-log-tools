import random
import re
import sys

RESET_COLOR = '\033[0m'

TERM_COLORATION = {
    'COLOR_RED': lambda x: '\033[91m{}\033[0m'.format(x),
    'COLOR_GREEN': lambda x: '\033[92m{}\033[0m'.format(x),
    'COLOR_YELLOW': lambda x: '\033[93m{}\033[0m'.format(x),
    'COLOR_LIGHT_PURPLE': lambda x: '\033[94m{}\033[0m'.format(x),
    'COLOR_PURPLE': lambda x: '\033[95m{}\033[0m'.format(x),
    'COLOR_CYAN': lambda x: '\033[96m{}\033[0m'.format(x),
    'COLOR_LIGHT_GRAY': lambda x: '\033[97m{}\033[0m'.format(x)
}

SOURCE_COLORS = {} # Colors attributed to this source

SOURCE_REG = "\[([\w.]+)\]"

def new_color():
    """
    We take the first available color.
    If none we randomly choose one.
    """
    for color in TERM_COLORATION:
        if color not in SOURCE_COLORS.values():
            return color
    return random.choice(TERM_COLORATION.keys())

if __name__ == "__main__":
    """
    Add a color to all each nyuki source inside `[``]`
    """
    for line in sys.stdin:
        found = None
        try:
            found = re.search(SOURCE_REG, line).groups()[0]
        except AttributeError, IndexError:
            # No source found in this line
            sys.stdout.write(line)
            continue
        SOURCE_COLORS[found] = SOURCE_COLORS.get(found, new_color())
        color = SOURCE_COLORS[found]
        line = re.sub(
            SOURCE_REG,
            TERM_COLORATION[color]('[%s]' % found),
            line, 1
        )
        sys.stdout.write(line)
