#!/usr/bin/env python3
"""measure time module
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the starting run time and end run time the divide it by n
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    tota_time = end_time - start_time

    return total_time / n
