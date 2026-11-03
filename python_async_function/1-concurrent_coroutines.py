#!/usr/bin/env python3
"""
importing wait_random async function
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n, max_delay):
    times = []
    for i in range(n):
        delay = await wait_random(max_delay)
        times.append(delay)
    times.sort()
    return (times)
