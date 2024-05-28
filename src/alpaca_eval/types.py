import os
import pathlib
from typing import Any, Callable, Sequence, Union, Dict, List, Tuple

import datasets
import pandas as pd

# don't load from utils to avoid unnecessary dependencies
AnyPath = Union[str, os.PathLike, pathlib.Path]
AnyData = Union[Sequence[Dict[str, Any]], pd.DataFrame, datasets.Dataset]
AnyLoadableDF = Union[AnyPath, AnyData, Callable, list, tuple]
