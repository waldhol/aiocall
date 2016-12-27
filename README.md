# aiocall
The missing call methods for [python asyncio](http://docs.python.org/3/library/asyncio).

I found that python asyncio is lacking some basic methods to invoke calls:
```python
call_soon_periodic(interval, callback, *args)
call_later_periodic(delay, interval, callback, *args)
```

This module provides these methods.

Example:
```python
def do_something(what):
    print('doing', what)

timer = call_later_periodic(0.5, 1.0, do_something, 'stuff')

loop = asyncio.get_event_loop()
loop.call_later(2.0, timer.cancel)
loop.call_later(3.0, loop.stop)
loop.run_forever()
loop.close()
```

Produces:
```
doing stuff
doing stuff
```
