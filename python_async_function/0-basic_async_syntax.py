#!/usr/bin/env python3
"""
Asynchronus program that waits random from 0 to max returns the value
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This is now documented and returns delay time."""
    delay = random.uniform(0, max_delay)
    return (await asyncio.sleep(delay, result=delay))
