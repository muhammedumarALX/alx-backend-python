#!/usr/bin/env python3
"""
This module defines an asynchronous function
"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An aysnc generator function
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
