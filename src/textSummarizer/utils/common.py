import os
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return a ConfigBox containing the data.

    Args:
        path_to_yaml (Path): Path like Input

    Raises:
        ValueError: if YAML file is empty
        e: empty files

    Returns:
        ConfigBox: ConfigBox containing the data from the YAML file
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
            logger.info(f'yaml_file: {path_to_yaml} loaded successfully')
            return ConfigBox(data)
    except BoxValueError as e:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories.

    Args:
        path_to_directories(list): List of path of directories
        ignore_log (bool, optional): ignore if multiple dirs to be created. Defaults to False.
    """
    for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'created directory at : {path}')



@ensure_annotations
def get_size(path: Path) -> str:
     """get size of a file in KB.

     Args:
         path (Path): Path of the file.

     Returns:
         str: size of the file in KB.
     """
     size_in_KB = round(os.path.getsize(path) / 1024)
     return f"~ {size_in_KB} KB" 


