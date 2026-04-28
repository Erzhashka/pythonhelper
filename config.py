"""Configuration file loader."""

from typing import Any, Dict


def load_config(config_file: str = "config.txt") -> Dict[str, Any]:
    """Load configuration from a text file.

    Args:
        config_file: Path to the configuration file.

    Returns:
        Dictionary containing configuration key-value pairs.

    Raises:
        FileNotFoundError: If the configuration file is not found.
    """
    config: Dict[str, Any] = {}

    try:
        with open(config_file, "r") as f:
            for line in f:
                line = line.strip()

                # Skip empty lines and comments
                if not line or line.startswith("#"):
                    continue

                # Parse KEY=VALUE pairs
                if "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()

                # Convert to appropriate types
                if value.lower() == "true":
                    config[key] = True
                elif value.lower() == "false":
                    config[key] = False
                elif value.isdigit():
                    config[key] = int(value)
                else:
                    config[key] = value

    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file '{config_file}' not found")

    return config
