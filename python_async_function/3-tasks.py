#!/usr/bin/env python3
"""
importing wait_random async function. to create task_wait_random task maker.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay) -> asyncio.Task:
    """creates task wait_random and return task object."""
    job = asyncio.create_task(wait_random(max_delay))

    return (job)
