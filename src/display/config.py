"""Read and check the settings in a Pac-Man configuration file.

This file contains the parser. The JSON file contains its input data.
load_config() returns a dictionary that the game can use.
Run this file directly to print the checked settings without starting a game.
"""

import json
import logging
import sys
from pathlib import Path


def strip_comments(text: str) -> str:
    """Remove whole comment lines, keeping the original line numbers."""
    lines = text.split("\n")
    clean_lines = []

    for line in lines:
        if line.lstrip().startswith("#"):
            clean_lines.append("")
        else:
            clean_lines.append(line)

    return "\n".join(clean_lines)


def read_integer(data: dict, key: str, default: int, minimum: int,
                 maximum: int, label: str) -> int:
    """Read one whole number, or return its default after a warning."""
    if key not in data:
        logging.warning("%s is missing. Using %s.", label, default)
        return default

    value = data[key]

    # True and False count as integers in Python. Reject them as settings.
    if isinstance(value, bool) or not isinstance(value, int):
        logging.warning(
            "%s must be an integer from %s to %s. Using %s.",
            label, minimum, maximum, default,
        )
        return default

    if value < minimum or value > maximum:
        logging.warning(
            "%s must be an integer from %s to %s. Using %s.",
            label, minimum, maximum, default,
        )
        return default

    return value


def validate_config(raw: object) -> dict:
    """Keep known settings and replace missing or invalid values."""
    if not isinstance(raw, dict):
        logging.warning("The config must be an object. Using defaults.")
        raw = {}

    config: dict = {}

    # This plan starts with exactly 3 lives, as explained in PARSING.md.
    config["lives"] = read_integer(raw, "lives", 3, 3, 3, "lives")

    seed = 42
    if "seed" not in raw:
        logging.warning("seed is missing. Using 42.")
    else:
        value = raw["seed"]
        if isinstance(value, bool) or not isinstance(value, int):
            logging.warning("seed must be a positive integer. Using 42.")
        elif value < 1:
            logging.warning("seed must be a positive integer. Using 42.")
        else:
            seed = value
    config["seed"] = seed

    config["level_max_time"] = read_integer(
        raw, "level_max_time", 90, 1, 600, "level_max_time",
    )
    config["points_per_pacgum"] = read_integer(
        raw, "points_per_pacgum", 10, 1, 10000, "points_per_pacgum",
    )
    config["points_per_super_pacgum"] = read_integer(
        raw, "points_per_super_pacgum", 50, 1, 10000,
        "points_per_super_pacgum",
    )
    config["points_per_ghost"] = read_integer(
        raw, "points_per_ghost", 200, 1, 10000, "points_per_ghost",
    )

    filename = "highscores.json"
    if "highscore_filename" not in raw:
        logging.warning(
            "highscore_filename is missing. Using highscores.json.")
    else:
        value = raw["highscore_filename"]
        # if "#" in value:
        #     logging.warning(
        #         "highscore_filename must be text. Using highscores.json.",
        #     )
        if not isinstance(value, str):
            logging.warning(
                "highscore_filename must be text. Using highscores.json.",
            )
        elif value.strip() == "" or "\x00" in value or "#" in value:
            logging.warning(
                "highscore_filename is invalid. Using highscores.json.",
            )
        else:
            filename = value
    config["highscore_filename"] = filename

    raw_levels = []
    if "level" not in raw:
        logging.warning("level is missing. Using default levels.")
    elif not isinstance(raw["level"], list):
        logging.warning("level must be a list. Using default levels.")
    else:
        raw_levels = raw["level"]

    levels = []
    number = 1
    for raw_level in raw_levels:
        label = "level[" + str(number) + "]"

        if not isinstance(raw_level, dict):
            logging.warning("%s must be an object. Skipping it.", label)
        else:
            level = {}
            level["width"] = read_integer(
                raw_level, "width", 15, 15, 25, label + ".width",
            )
            level["height"] = read_integer(
                raw_level, "height", 15, 15, 25, label + ".height",
            )
            levels.append(level)

        number = number + 1

    if len(levels) < 10:
        missing = 10 - len(levels)
        logging.warning(
            "level has fewer than 10 valid entries. Adding %s default levels.",
            missing,
        )

    while len(levels) < 10:
        level = {}
        level["width"] = 15
        level["height"] = 15
        levels.append(level)

    config["level"] = levels

    # Only known keys enter config, so unknown keys are ignored.
    return config


def reject_constant(value: str) -> None:
    """Reject NaN and Infinity, which are not standard JSON numbers."""
    raise ValueError("Invalid JSON constant: " + value)


def load_config(path: Path) -> dict:
    """Read the file, remove comments, decode JSON, and check settings."""
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    clean_text = strip_comments(text)
    raw = json.loads(clean_text, parse_constant=reject_constant)
    config = validate_config(raw)
    return config


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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
