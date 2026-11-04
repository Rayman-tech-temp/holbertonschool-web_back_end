#!/usr/bin/env python3
"""
importing wait_random and wait_n async function. to create measure_time average.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay) -> int:
    """uses the wait_n function to average the wait values."""
    total_time = asyncio.run(wait_n(n, max_delay))
    total_time = sum(total_time)

    return (total_time / n)
