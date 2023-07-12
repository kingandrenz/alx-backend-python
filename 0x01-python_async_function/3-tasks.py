#!/usr/bin/env python3
"""task3 module
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.task:
    """this function returns an asyncio task
    """

    return asyncio.create_task(wait_random(max_delay))
