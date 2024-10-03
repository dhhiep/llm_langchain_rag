import toml
from pathlib import Path

def settings(key):
    if not hasattr(settings, "cached_settings"):
        settings_path = Path(__file__).parents[1] / "global_settings.toml"
        settings.cached_settings = toml.load(settings_path)

    return settings.cached_settings[key]

