class Dicts:
    def __init__(self, _dict: dict = None):
        self._dict = _dict

    def filter_keys(self, keys: list) -> dict:
        """
        Filters/removes a list of keys from a dictionary

        Args:
            keys (list): Keys to filter

        Returns:
           (dict)
        """
        return {k: v for k, v in self._dict if k not in keys}

    def delete_none_values(self, _dict: dict) -> dict:
        """Delete None values recursively from all of the dictionaries"""
        for key, value in list(_dict.items()):
            if isinstance(value, dict):
                self.delete_none_values(value)
            elif value is None:
                del _dict[key]
            elif isinstance(value, list):
                for v_i in value:
                    if isinstance(v_i, dict):
                        self.delete_none_values(v_i)

        return _dict