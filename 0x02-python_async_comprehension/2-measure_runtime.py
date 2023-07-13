#!/usr?bin/env python3
"""task 2
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return the runtime of running a funct
    4 times using asyncio.gather
    """
    start_time = time.time()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
    )

    return time.time() - start_time
