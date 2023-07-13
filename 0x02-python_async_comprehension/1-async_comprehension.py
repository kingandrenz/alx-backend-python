#!/usr/bin/env python3
"""task 1
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """generates a list of random number from another function
    """

    return [x async for x in async_generator()]
