
from src.display.config import load_config
import logging
import sys
from pathlib import Path
import json


def main() -> int:
    """Accept one file path and print the checked settings."""
    logging.basicConfig(level=logging.WARNING, format="Warning: %(message)s")

    if len(sys.argv) != 2:
        print(
            "Usage: python3 " + str(Path(__file__).resolve()) + " CONFIG_FILE",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[1])

    try:
        config = load_config(path)
    except json.JSONDecodeError as error:
        print(
            "Error: invalid JSON at line " + str(error.lineno)
            + ", column " + str(error.colno) + ".",
            file=sys.stderr,
        )
        return 2
    except (OSError, UnicodeError, ValueError) as error:
        print("Error: " + str(error), file=sys.stderr)
        return 2

    print(json.dumps(config, indent=2))
    # print("{")

    # for key, value in config.items():
    #     print('  "' + key + '": ' + str(value) + ",")

    # print("}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
