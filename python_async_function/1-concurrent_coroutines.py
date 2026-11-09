#!/usr/bin/env python3
"""
importing wait_random async function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay) -> list[float]:
    """ recording returns after wait time, .gather respects sequence"""
    tasks = []
    times = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for finish in asyncio.as_completed(tasks):
        times.append(await finish)

    return (times)
