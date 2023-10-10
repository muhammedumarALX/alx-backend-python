#!/usr/bin/env python3
"""
This module define an asynchronous function
"""
import asyncio


async def async_comprehension():
    """
    async comprehension list
    Return a random float
    """
    async_generator = __import__("0-async_generator").async_generator

    random_numbers = [value async for value in async_generator()]

    return random_numbers
