#!/usr/bin/env python3
from typing import Union


def safe_first_element(lst: Union[list, None]) -> any:
    if lst:
        return lst[0]
    else:
        return None
