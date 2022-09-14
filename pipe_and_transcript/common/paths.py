# SYSTEM 
from pathlib import Path


class Paths:
    ROOT_DIR       = str(Path(__file__).parent.parent)
    TEMP_DIRECTORY = ROOT_DIR + '/temp'