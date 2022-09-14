# SYSTEM
from functools import wraps

# UTILS
from pipe_and_transcript.utils import Oss


def delete_temp_file_on_completion(temp_file_name: str) -> callable:
    """
    This decorator runs the decorated function then... 
    ...removes the provided file name from this package's /temp folder

    Args:
        temp_file_name (str)
    """

    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            
            # run the original decorated function
            func_response = fn(*args, **kwargs)
            # then, remove the temp file whatever the outcome of the function
            Oss.delete_temp_file(temp_file_name)

            return func_response

        return wrapper
    return inner