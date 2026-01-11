from configparser import ConfigParser
import os

def read_configuration(category, key):
    parser = ConfigParser()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_dir, "Configurations", "config.ini")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config.ini not found at: {config_path}")
    parser.read(config_path)

    if not parser.has_section(category):
        raise KeyError(f"Section '{category}' not found in config.ini")

    if not parser.has_option(category, key):
        raise KeyError(f"Key '{key}' not found under section '{category}'")

    return parser.get(category, key)