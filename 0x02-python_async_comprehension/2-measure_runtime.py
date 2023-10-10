#!/usr/bin/env python3
"""
Module defines an asynchronous function
"""
import asyncio
import time


async def measure_runtime() -> float:
    """
    function that measures runtime and returns a float
    """
    async_compre = __import__("1-async_comprehension").async_comprehension
    tasks = [async_compre() for _ in range(4)]

    start_time = time.time()

    await asyncio.gather(*tasks)

    end_time = time.time()

    total_runtime = end_time - start_time

    return total_runtime
