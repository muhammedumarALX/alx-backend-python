#!/usr/bin/env python3
import asyncio
import random

"""
Asynchronous function `wait_random`
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    Returns `float`
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
