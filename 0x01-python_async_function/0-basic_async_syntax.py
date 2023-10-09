#!/usr/bin/env python3
"""
This module define an Asynchronous function `wait_random`
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    Returns `float`
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
