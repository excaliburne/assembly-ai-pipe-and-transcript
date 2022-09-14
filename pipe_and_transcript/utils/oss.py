# SYSTEM
import os
from pathlib import Path
from typing import Generator

# COMMON
from pipe_and_transcript.common import Paths


class Oss:

    @staticmethod
    def delete_temp_file(temp_file_name: str):
        """
        Deletes a file under the temp/ directory

        Args:
            temp_file_name (str)

        Returns:
            None
        """
        return os.remove(Paths.TEMP_DIRECTORY + f'/{temp_file_name}')

    def read_file(file_path: str, chunk_size = 5242880) -> Generator:
        with open(file_path, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data