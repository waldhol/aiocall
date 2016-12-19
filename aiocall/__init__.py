#! /usr/bin/env python3

import asyncio
import logging

def call_soon_periodic(interval, callback, *args, **kwargs):
    """Arrange for the `callback` to be called as soon as possible and
    periodically every `interval` seconds (either an int or float).

    `interval` is the delay between the end of one invocation of the callback
    and the start of the next invocation.

    An instance of `asyncio.Handle` is returned, which can be used to cancel
    the callback.

    The optional positional `args` will be passed to the callback when it is
    called. If you want the callback to be called with some named arguments,
    use a closure or `functools.partial()`.
    """
    return call_later_periodic(0, interval, callback, *args, **kwargs)

def call_later_periodic(delay, interval, callback, *args, **kwargs):
    """Arrange for the `callback` to be called after `delay` seconds
    periodically every `interval` seconds (both are either an int or float).

    `interval` is the delay between the end of one invocation of the callback
    and the start of the next invocation.

    An instance of `asyncio.Handle` is returned, which can be used to cancel
    the callback.

    The optional positional `args` will be passed to the callback when it is
    called. If you want the callback to be called with some named arguments,
    use a closure or `functools.partial()`.
    """
    async def coro():
        await asyncio.sleep(delay)
        while True:
            callback(*args)
            await asyncio.sleep(interval)
    return asyncio.Task(coro(), **kwargs)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    logger = logging.getLogger(__name__)
    loop = asyncio.get_event_loop()

    def do_something(what):
        logger.info('doing %s...', what)

    logger.info('setup timers')
    timer1 = call_soon_periodic(1.0, do_something, 'stuff')
    timer2 = call_later_periodic(0.5, 1.0, do_something, 'other stuff')
    loop.call_later(2.7, timer1.cancel)
    loop.call_later(2.8, timer2.cancel)
    loop.call_later(2.9, loop.stop)
    logger.info('starting loop')
    loop.run_forever()
    logger.info('loop done')

    loop.close()
