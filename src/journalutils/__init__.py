from pathlib import Path
import yaml

PROJECT_DIR = Path(__file__).parents[2].absolute()
config_path = PROJECT_DIR / "config.yaml"
with open(config_path, "r") as stream:
    try:
        CONFIG = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

DATA_PATH = PROJECT_DIR / "data"
