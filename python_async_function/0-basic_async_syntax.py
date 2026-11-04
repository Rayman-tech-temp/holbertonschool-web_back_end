#!/usr/bin/env python3
"""
Asynchronus program that waits random from 0 to max returns the value
"""
import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    return(await asyncio.sleep(delay, result=delay))
