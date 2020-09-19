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
from os.path import dirname, realpath

class JsonCourier:
    def __init__(self, json_folder):
        self.json_folder = json_folder

    # loads data from json file and returns it as Dict
    def get_dict_from_json(self, file_name):
        file_path_string = self.json_folder + file_name
        print(file_path_string)
        file_path = Path(dirname(realpath(sys.argv[0]))) / file_path_string
        loaded_dict = {}
        with suppress(OSError):
            with file_path.open() as f:
                loaded_dict = json.load(f)
        return loaded_dict
