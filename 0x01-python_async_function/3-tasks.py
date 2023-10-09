#!/usr/bin/env python3
"""
This module define the function `task_wait_random`
"""
import asyncio
from typing import Callable


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and returns an `asycio.Task`
    """
    wait_random = __import__('0-basic_async_syntax').wait_random

    async def wrapper():
        return await wait_random(max_delay)

    return asyncio.ensure_future(wrapper())
