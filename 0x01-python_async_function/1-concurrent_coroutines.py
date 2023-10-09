#!/usr/bin/env python3
"""
Yhis module define the function `wait_n`
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    create list and Returns a `Float`
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    tasks = [wait_random(max_delay) for _ in range(n)]

    results = await asyncio.gather(*tasks)

    sorted_results = sorted(results)

    return sorted_results
