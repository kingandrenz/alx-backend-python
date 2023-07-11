#!/usr/bin/env python3
""" the basic async module
"""

import asyncio
import random


async def wait_random(max_delay: int = 0)-> float:

    """ a function that awaits for a random
        routinten and returns it
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
