import json
import os
from typing import Tuple


def read_retribution_preferences() -> Tuple[str, str]:
    # Using this as a fallback
    install = ""
    saved_games = ""
    pref_path = os.path.join(
        os.path.expanduser("~"), "AppData", "Local", "DCSRetribution"
    )
    pref_path = os.path.join(pref_path, "retribution_preferences.json")
    if os.path.exists(pref_path):
        with open(pref_path, "r") as file:
            try:
                json_dict = json.load(file)
                if "dcs_install_dir" in json_dict:
                    install = json_dict["dcs_install_dir"]
                if "saved_game_dir" in json_dict:
                    saved_games = json_dict["saved_game_dir"]
            except (KeyError, ValueError):
                # ValueError for decode errors (if the file is corrupted), KeyError in
                # case the format isn't what we expect.
                return "", ""
    return install, saved_games
