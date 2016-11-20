import ast
import json
import re
import sys


JSON_REG = "^[^{]*({.+})[^}]*$"
JSON_PADDING = 58


if __name__ == "__main__":
    """
    Try to prettify all dictionary or json data in the log line.
    """
    for line in sys.stdin:
        found = None
        try:
            found = re.search(JSON_REG, line).groups()
        except AttributeError:
            # no braquets
            sys.stdout.write(line)
            continue
        if found:
            try:
                data = json.loads(found[0])
                # It's a json
            except ValueError as e:
                try:
                    data = ast.literal_eval(found[0])
                    # It's a dictionary representation
                except Exception:
                    # Nothing good
                    sys.stdout.write(line)
                    continue
            line = re.sub(
                JSON_REG,
                json.dumps(data, sort_keys=True, indent=4),
                line
            )
            line = re.sub('^', ''.ljust(JSON_PADDING-1, '-'), line)
            line = re.sub('\n', '\n'.ljust(JSON_PADDING, '-'), line)
        sys.stdout.write(line + '\n')
