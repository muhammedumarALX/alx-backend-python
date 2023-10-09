#!/usr/bin/env python3
"""
This module define the function `measure_time`
"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    calculate the time used in completing a Task
    and Returns a `float`
    """
    wait_n = __import__('1-concurrent_coroutines').wait_n

    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = end_time - start_time

    average_time_per_task = total_time / n

    return average_time_per_task
