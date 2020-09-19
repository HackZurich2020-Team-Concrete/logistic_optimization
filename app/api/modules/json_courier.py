#      ____. _________________    _______    _________                     .__
#     |    |/   _____/\_____  \   \      \   \_   ___ \  ____  __ _________|__| ___________
#     |    |\_____  \  /   |   \  /   |   \  /    \  \/ /  _ \|  |  \_  __ \  |/ __ \_  __ \
# /\__|    |/        \/    |    \/    |    \ \     \___(  <_> )  |  /|  | \/  \  ___/|  | \/
# \________/_______  /\_______  /\____|__  /  \______  /\____/|____/ |__|  |__|\___  >__|
#                  \/         \/         \/          \/                            \/

""" The JsonCourier object is made to read and save to json files. Currently saving is not yet implemented.
November 2019 """

__author__ = "Manuel Galliker"
__maintainer__ = "Manuel Galliker, Fabian Kaiser"
__license__ = "GPL"

import json
import sys
from contextlib import suppress
from pathlib import Path


class JsonCourier:
    def __init__(self, json_path):
        self.json_path = json_path

    # loads data from json file and returns it as Dict
    def get_dict_from_json(self):
        loaded_dict = {}
        with suppress(OSError):
            with self.json_path.open() as f:
                loaded_dict = json.load(f)
        return loaded_dict
